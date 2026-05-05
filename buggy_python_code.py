import sys 
import os
import yaml
import flask

app = flask.Flask(__name__)
from urllib.parse import urlparse

def is_safe_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and parsed.netloc == "www.google.com"

@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)

        
CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person(object):
    def __init__(self, name):
        self.name = name


#def print_nametag(format_string, person):
#   print(format_string.format(person=person))
#-> user input 그대로 .format()에 들어감. 공격자가 내부 변수 접근 가능. 내부 API 키 털릴 수 있음
def print_nametag(person):
    print(f"Name: {person.name}")

'''def fetch_website(urllib_version, url):
    # Import the requested version (2 or 3) of urllib
    exec(f"import urllib{urllib_version} as urllib", globals())
    # Fetch and print the requested URL
 
    try: 
        http = urllib.PoolManager()
        r = http.request('GET', url)
    except:
        print('Exception')'''
#exec 제거 + whitelist 방식
def fetch_website(urllib_version, url):
    if not is_safe_url(url):
        raise ValueError("Unsafe URL")

    import urllib3
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return r.data

#YAML Deserialization
def load_yaml(filename):
    stream = open(filename)
    #deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    deserialized_data =yaml.load(stream, Loader=yaml.SafeLoader) #safeLoader 사용
    return deserialized_data
    
'''def authenticate(password):
    # Assert that the password is correct: python 실행 옵션 -O 쓰면 assert 무시됨
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")'''
def authenticate(password):
    if password != "Iloveyou":
        raise ValueError("Invalid password!")
    print("Successfully authenticated!")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice  = input("Select vulnerability: ")
    if choice == "1": 
        new_person = Person("Vickie")  
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)

