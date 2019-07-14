import requests
from lxml import etree
import time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/75.0.3770.100 Safari/537.36",
    "referer": "https://www.95590.org/",
    "keep-live": "false"
}
def get_content(title, charpter, src):
    try:
        response = requests.get(src, headers=headers)
        html = etree.HTML(response.content)
        src_list = html.xpath('//div[@class="entry-content"]/p')
        #print(len(src_list))
        # for src in zip(src_list):
        content = src[0].text
        file_name = '.\\books\\' + title + '.txt'
        with open(file_name, 'a') as f:
            f.write(content + '\n')
        #print(content)
        response.close()
    except Exception as e:
        print(e)
    time.sleep(1)
    
def get_charpter(title, src):
    response = requests.get(src, headers=headers)
    html = etree.HTML(response.content)
    src_list = html.xpath('//div[@class="entry-content"]/ul/li[*]/a')
    #print(len(src_list))
    for src in zip(src_list):
        charpter = src[0].text
        content_src = src[0].get('href')
        print(charpter, content_src)
        file_name = '.\\books\\' + title + '.txt'
        with open(file_name, 'a') as f:
           f.write(charpter+'\n')
        time.sleep(3)
        response.close()
        get_content(title, charpter, content_src)


# 主程序入口， 先爬取官场小说
response= requests.get("https://www.95590.org/", headers=headers)
html = etree.HTML(response.content)
title_list = html.xpath('//*[@id="categories"]/ul/li[*]/a/text()')
src_list =  html.xpath('//*[@id="categories"]/ul/li[*]/a/@href')
#print(len(title_list))
for title, src in zip(title_list, src_list):
    title = str(title)[0: -5]
    print(title, src)
    file_name = '.\\books\\'+title+'.txt'
    with open(file_name, 'w') as f:
        f.write(title + '\n')
    response.close()
    get_charpter(title, src)





