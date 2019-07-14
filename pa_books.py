import requests
import lxml
from lxml import etree
from lxml.etree import tostring
import os

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36",
    "referer": "https://www.95590.org/"
}

def get_charpter(title, src):
    response = requests.get(src, headers=headers)
    html = etree.HTML(response.content)
    src_list = html.xpath('//*[@id="category-64"]/div/ul/li[*]/a')
    #print(len(src_list))
    for src in zip(src_list):
        charpter = src[0].text
        content_src = src[0].get('href')
        print(charpter)
        print(content_src)
        get_content(title, charpter, content_src)

def get_content(title, charpter, src):
    response = requests.get(src, headers=headers)
    html = etree.HTML(response.content)
    src_list = html.xpath('//div[@class="entry-content"]/p')
    #print(len(src_list))
    for src in zip(src_list):
        content = src[0].text
        print(content)

response= requests.get("https://www.95590.org/",headers=headers)
html = etree.HTML(response.content)
title_list = html.xpath('//*[@id="categories"]/ul/li[*]/a/text()')
src_list =  html.xpath('//*[@id="categories"]/ul/li[*]/a/@href')
#print(len(title_list))
for title, src in zip(title_list, src_list):
    print(title)
    print(src)
    if os.path.exists(title) == False:
        os.mkdir('.\\books\\'+title)
    get_charpter(title, src)




