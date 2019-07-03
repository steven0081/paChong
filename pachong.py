import requests

from lxml import etree

headers={
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)" 
                  " Chrome/63.0.3239.132 Mobile Safari/537.36",
    "referer" : "https://www.mzitu.com/tag/ugirls"
}
# 1、请求妹子图片网站，拿到html数据
response= requests.get("https://www.mzitu.com/tag/ugirls",headers=headers)

# 2、抽取想要数据，图片链接
html = etree.HTML(response.content)
src_list = html.xpath('//img[@class="lazy"]/@data-original')
alt_list = html.xpath('//img[@class="lazy"]/@alt')

for src, alt in zip(src_list,alt_list):
    # 3、下载图片
    response = requests.get(src, headers=headers)
    # 4、保存图片
    fileName="img\\"+alt+".jpg"
    with open(fileName,"wb") as f:
        f.write(response.content)



