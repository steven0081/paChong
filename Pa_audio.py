import requests
import json


headers={
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)" 
                  " Chrome/63.0.3239.132 Mobile Safari/537.36"
}

url = "https://www.ximalaya.com/revision/play/album?albumId=291718&pageNum=1&sort=1&pageSize=30"

response = requests.get(url, headers=headers).text
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

