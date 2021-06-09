import requests, json
from bs4 import BeautifulSoup
from pprint import pprint
import csv, codecs
import re
from time import sleep

import os
import sys
import urllib.request

start = 1
# params = {
#     "display": 100,
#     "start": 1,
#     "sort": "date"
# }
pp = []

client_id = "rHEoGnfNxhPls5IGSdjH"
client_secret = "pOjyL0OiL3"
encText = urllib.parse.quote("귀농")
# params =  urllib.parse.quote('&display=100&start=1&sort=date HTTP/1.1')
while start <= 631445:
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText+ "&sort=date&display=100&start="+str(start)
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        rp = response_body.decode('utf-8')
        jsonData = json.loads(rp)
        print(rp)
        # for j in jsonData['items']:
        # # pprint(jsonData['postdate'])
        #     date = j['postdate']
        #     pp.append(date)
        start += 100
        sleep(1)
        # pprint(pp)
        # pp = rp.compile('.*postdate.*')
        # # if int(rp["postdate"]) <= 20200523:
        #     # pp.append(rp)
        # # print(len(pp))
    else:
        print("Error Code:" + rescode)


