import requests
from lxml import etree
import time
import socket
from selenium import webdriver

socket.setdefaulttimeout(20)
headers = {    'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
}

def get_content(title, charpter, src):
    try:
        #option = webdriver.ChromeOptions()
        #option.add_argument('headless')
        #brower = webdriver.Chrome(chrome_options=option)
        brower = webdriver.Chrome()
        brower.get(src)
        time.sleep(3)
        item_list = brower.find_elements_by_xpath('//div[@class="entry-content"]/p')
        for item in item_list:
            content = item.text
            if content is not None:
                content = content.encode('gbk', 'ignore').decode('gbk')
                file_name = '.\\books\\' + title + '.txt'
                with open(file_name, 'a') as f:
                    f.write(content + '\n')
    except Exception as e:
        print(e)
    brower.close()

def get_charpter(title, src):
    response = requests.get(src, headers=headers)
    html = etree.HTML(response.content)
    src_list = html.xpath('//div[@class="entry-content"]/ul/li[*]/a')
    # print(len(src_list))
    for src in zip(src_list):
        charpter = str(src[0].text).encode('gbk', 'ignore').decode('gbk')
        content_src = src[0].get('href')
        print(charpter, content_src)
        file_name = '.\\books\\' + title + '.txt'
        with open(file_name, 'a') as f:
            f.write(charpter + '\n')
        time.sleep(1)
        response.close()
        get_content(title, charpter, content_src)


response = requests.get("https://it.95590.org/", headers=headers)
html = etree.HTML(response.content)
title_list = html.xpath('//*[@id="categories"]/ul/li[*]/a/text()')
src_list = html.xpath('//*[@id="categories"]/ul/li[*]/a/@href')
book_list = ['刘强东·注定震惊世界', '任正非这个人', '雷军·人因梦想而伟大',
             '张亚勤·让智慧起舞', '华为狼道', 'IBM帝国缔造者']
# print(len(title_list))
for title, src in zip(title_list, src_list):
    title = str(title)[0:-5]
    print(title, src)
    if title not in book_list:
        file_name = '.\\books\\' + title + '.txt'
        with open(file_name, 'w') as f:
            f.write(title + '\n')
        response.close()
        get_charpter(title, src)





