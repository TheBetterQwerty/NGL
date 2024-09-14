#!/usr/bin/env python3

import requests
import threading
import sys

url = "https://ngl.link/api/submit"

try:
    username = sys.argv[1]
except IndexError:
    print("No target was found !!\nEnter the script name then the target (Ex:python program.py targetname)")
    exit(0)

txt = input("Enter Text >>> ")

data = {
    'username': username,
    'question': txt, 
    'deviceId': '5adh65ye-b542-48g5-b76a-33765y242e59',
    'gameSlug': '' ,
    'referrer': '',
}

req = 0

def make_requests():
    global req
    while True:
        try:
            response = requests.post(url , data=data).text
            req += 1
            print(f"Message send to {username} : {req}")
        except KeyboardInterrupt:
            break

def main():
    threads = []
    for i in range(50):
        t = threading.Thread(target=make_requests)
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
