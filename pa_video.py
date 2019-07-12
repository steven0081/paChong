import requests
import json
from lxml import etree
from selenium import webdriver
import os, time

headers={
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)" 
                  " Chrome/63.0.3239.132 Mobile Safari/537.36"
}

def video_download(title,href):
    url = 'https://www.pearvideo.com/'+ href
    print(url)
    brower = webdriver.Chrome()
    brower.get(url)
    time.sleep(1)
    video_src = brower.find_element_by_xpath('//*[@id="JprismPlayer"]/video').get_attribute('src')
    #print(item.get_attribute('src'))
    response = requests.get(video_src, headers=headers)
    fileName = "video\\" + title + ".mp4"
    with open(fileName, "wb") as f:
        f.write(response.content)
    brower.close()
'''
    response = requests.get(url, headers=headers).text
    //print(response)
    html = etree.HTML(response)
    src = html.xpath('//*[@id="JprismPlayer"]/video/@src')
    print(src)
    '''




url = "https://www.pearvideo.com/category_1"

response = requests.get(url, headers=headers).text
html = etree.HTML(response)
videotitle_list = html.xpath('//*[@id="categoryList"]/li[*]/div/a/div[2]')
videohref_list = html.xpath('//*[@id="categoryList"]/li[*]/div/a/@href')
for t ,h in zip(videotitle_list, videohref_list):
    video_download(t.text, h)
    print(t.text,h)


'''
audio_data = json.loads(response)["data"]["tracksAudioPlay"]

for audio_info in audio_data:
    music_url = audio_info["src"]
    music_name = audio_info["trackName"]
    # music_name = music_url.split("/")[-1]
    response = requests.get(music_url,headers=headers)
    # fileName = "audio\\" + music_name + ".m4a"
    with open("audio/{}".format(music_name + ".m4a"), "wb") as f:
        f.write(response.content)

# print(audio_data)

'''