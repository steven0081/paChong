import requests
import json
from lxml import etree
from selenium import webdriver
import os, time
import socket


socket.setdefaulttimeout(20)

headers={
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)' 
                  ' Chrome/63.0.3239.132 Mobile Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie': '__guid=233007000.2418755580880336400.1563715342366.897; monitor_count=7',
    'Host': 'www.dt870.com',
    'Referer':'https://www.dt870.com/share/76jZncAqrdgXC6fY'
}

#下载视频文件
def  video_download(title, href):
    print(href)
    response = requests.get(href, headers=headers)
    time.sleep(3)
    html = etree.HTML(response.text)
    video_src = html.xpath('//video/@preload')
    print(video_src)
    response.close()
    '''
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
    '''

def video_src(title, href):
    response = requests.get(href, headers=headers)
    html = etree.HTML(response.text)
    iframe_src = html.xpath('//iframe/@src')
    print(title, 'iframe src = ',iframe_src[0])
    response.close()
    video_download(title, iframe_src[0])

url = "https://www.9527yy.com/mplay.php?mso=26757/1/3"
response = requests.get(url, headers=headers)
html = etree.HTML(response.text)
videotitle_list = html.xpath('//a[@class="am-btn am-btn-default lipbtn"]/text')
videohref_list = html.xpath('//a[@class="am-btn am-btn-default lipbtn"]/@href')
response.close()
for t ,h in zip(videotitle_list, videohref_list):
    href = 'https://www.9527yy.com/'+h
    video_src(t, href)
    #print(t, href)
