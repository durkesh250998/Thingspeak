import urllib.request
import requests
import threading
import json

import random

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val=random.randint(1,3)
    URl='https://api.thingspeak.com/update?api_key=&field1=0'
    KEY=''
    HEADER='&field1={}&field2={}&field3'.format(val,val)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)
    
if __name__ == '__main__':
    thingspeak_post()
