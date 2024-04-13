#!/usr/bin/env python3

import requests
import threading

url = "https://ngl.link/api/submit"


username = input("Enter your username : ")
txt = input("Enter Your text")



data = {
    'username': username,
    'question': txt, 
    'deviceId': '5adh65ye-b542-48g5-b76a-33765y242e59',
    'gameSlug': '' ,
    'referrer': '',
    }


def do_request():
  while True:
      response = requests.post(url, data=data).text
      print("<Message sent> ", )
    
threads = []

for i in range(50):
   t = threading.Thread(target = do_request)
   t.daemon = True
   threads.append(t)

for i in range(50):
   threads[i].start()

for i in range(50):
   threads[i].join()
