import requests

from lxml import etree
from lxml.etree import tostring


headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36",
    "referer": "https://www.mzitu.com/tag/ugirls"
}

url = 'https://www.mzitu.com/186386'

for i in range(1, 16):
    if i == 1 :
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url+ '/'+ str(i), headers=headers)
    html = etree.HTML(response.content)
    img_info = html.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')
    img_src = img_info[0]
    print(img_src)
    fileName = "mzitu\\" + str(i) + ".jpg"
    with open(fileName, "wb") as f:
        response = requests.get(img_src, headers=headers)
        f.write(response.content)
