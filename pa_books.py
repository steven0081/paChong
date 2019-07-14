import requests
import lxml
from lxml import etree
from lxml.etree import tostring

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36",
    "referer": "https://www.95590.org/"
}

def get_charpter(title, src):
    response = requests.get(src, headers=headers)
    html = etree.HTML(response.content)
    src_list = html.xpath('//*[@id="category-64"]/div/ul/li[*]/a')
    print(len(src_list))
    for src in zip(src_list):
        charpter = src[0].text
        content_src = src[0].get('href')
        get_content(title, charpter, content_src)
        #print(describ)
        #print(img_src)

def get_content(title, charpter, src):
    response = requests.get(src, headers=headers)
    html = etree.HTML(response.content)
    src_list = html.xpath('//div[@class="entry-content"]/p')
    print(len(src_list))
    for src in zip(src_list):
        content = src[0].text
        print(content)

response= requests.get("https://www.95590.org/",headers=headers)

html = etree.HTML(response.content)
src_list = html.xpath('//*[@id="categories"]/ul/li[*]/a')
print(len(src_list))
for src in zip(src_list):
    describ = src[0].text
    img_src = src[0].get('href')
    print(describ)
    print(img_src)
    get_charpter(describ, img_src)




