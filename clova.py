import os
import sys
import requests
import urllib.request
import json
from bs4 import BeautifulSoup
from api_key import *

'''
client_id = ""
client_secret = "" '''

# 유명인 얼굴인식
url = "https://openapi.naver.com/v1/vision/celebrity" 

files = {'image': open('test_img/1234.png', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,files=files, headers=headers)
rescode = response.status_code
response_data = response.json()
try:
    if(rescode==200):
        name = response_data['faces'][0]['celebrity']['value']
        confidence = response_data['faces'][0]['celebrity']['confidence']
        img_url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + name
        outfile = 'Star\{}.jpg'.format(name)
        r = requests.get(img_url)
        html = r.text
        soup = BeautifulSoup(html,'html.parser')
        try:
            face = soup.find("body")
            face1 = face.find("div",{"id":"wrap"})
            face2 = face1.find("div",{"id":"container"})
            face3 = face2.find("div",{"id":"content"})
            face4 = face3.find("div",{"id":"main_pack"})
            face5 = face4.find("div",{"id":"people_info_z"})
            face6 = face5.find("div",{"class":"cont_noline"})
            face7 = face6.find("div",{"class":"profile_wrap"})
            face8 = face7.find("div",{"class":"big_thumb"})
            face9 = str(face8.find("img"))
        except AttributeError:
            print("죄송해요 프로필 사진이 없어요 \n당신의 얼굴은 "'{0}'"하고 "'{1}'"% 닮은 것 같네요^^".format(name,round(confidence*100,2)))
        if not AttributeError:
            pass
        else:
            try:
                split_img = face9.split()
                splits_img = split_img[8]
                cut_url = splits_img[4:]
                return_url = cut_url[1:-1]
                if confidence*100 < 2:
                    print("당신의 얼굴은 "'{0}'"하고 "'{1}'"% 닮은 것 같네요^^".format(name,round(confidence*100,2)))
                    urllib.request.urlretrieve(return_url, outfile)
                else:
                    print("당신의 얼굴은 "'{0}'"하고 "'{1}'"% 닮았습니다.".format(name,round(confidence*100,2)))
                    urllib.request.urlretrieve(return_url, outfile)
            except NameError :
                pass
    else:
        print("Error Code:" + rescode)
except IndexError:
    print("얼굴을 못찾았습니다")