#!\HackTX2015\freesound-python-master

import freesound, webbrowser, requests
#sys, os

webbrowser.open('https://www.freesound.org/apiv2/oauth2/authorize/?client_id=f5e77a2da299d11cbd32&response_type=code')

c = freesound.FreesoundClient()
c.set_token("bc4e71b01652c61a22573964e885253806b31839","token")

results = c.text_search(query="dubstep",fields="id,name,previews")

sound = results[1];
requests.post("https://www.freesound.org/apiv2/oauth2/access_token/")


sound.retrieve(".", sound.name+".mp3");
#sound.retrieve_preview(".",sound.name+".mp3")

"""
for sound in results:
    sound.retrieve_preview(".",sound.name+".mp3")
    print(sound.name)
""" 

https://www.freesound.org/apiv2/oauth2/access_token/client_id=f5e77a2da299d11cbd32&client_secret=bc4e71b01652c61a22573964e885253806b31839&grant_type=authorization_code&code=3160fc189580e4f0a2fb5d1e6c7622a7bdcb00bc