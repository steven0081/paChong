import requests
import json
from lxml import etree
from selenium import webdriver
import os, time

headers={
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)" 
                  " Chrome/63.0.3239.132 Mobile Safari/537.36"
}

#下载视频文件
def  video_download(title, href):
    url = 'https://www.pearvideo.com/'+ href
    brower = webdriver.Chrome()
    brower.get(url)
    time.sleep(1)
    video_src = brower.find_element_by_xpath('//*[@id="JprismPlayer"]/video').get_attribute('src')
    brower.close()
    print(title, url, video_src)
    title = str(title)[0:4]
    fileName = "video\\" + title + ".mp4"
    with open(fileName, "wb") as f:
        try:
            response = requests.get(video_src, headers=headers)
            f.write(response.content)
        except Exception as e:
            print(e)

url = "https://www.pearvideo.com/category_1"

response = requests.get(url, headers=headers).text
html = etree.HTML(response)
videotitle_list = html.xpath('//*[@id="categoryList"]/li[*]/div/a/div[2]')
videohref_list = html.xpath('//*[@id="categoryList"]/li[*]/div/a/@href')
for t ,h in zip(videotitle_list, videohref_list):
    video_download(t.text, h)
    #print(t.text,h)
