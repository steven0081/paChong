import requests
import lxml
from lxml import etree
from lxml.etree import tostring

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36",
    "referer": "https://www.mzitu.com"
}
response= requests.get("https://www.mzitu.com",headers=headers)

html = etree.HTML(response.content)
src_list = html.xpath('//*[@id="pins"]/li/span/a')
print(len(src_list))
for src in zip(src_list):
    describ = src[0].text
    img_src = src[0].get('href')
    print(describ)
    print(img_src)




