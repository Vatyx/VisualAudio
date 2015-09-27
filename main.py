from flask import render_template
from flask import request
import json
import requests
from app import app

code = None
access_token = None
currentList = None

@app.route('/')
@app.route('/index')
def index():
    print("In side the get")
    return render_template('index.html')

@app.route('/woo', methods=['GET'])
def woo():
    code = request.args.get('code')
    req = requests.post("https://accounts.spotify.com/api/token", data={'grant_type': 'authorization_code', 'code': code, 'redirect_uri': 'https://flasktest-vatyx.c9.io/woo', 'client_id': '9344d5a91349489488cc51637d912e21', 'client_secret': '5cb043cf9fc546bebc91978ec8a95bc6'})
    res = req.json()
    access_token = res['access_token']
    print("This is the access_token " + access_token);
    
    payload1 = {'Authorization': 'Bearer ' +access_token}
    payload2 = {'q': 'px3'}
    req = requests.get("https://api.spotify.com/v1/search?q=px3&type=track", headers=payload1)
    
    reqJson = req.json()
    
    for thing in reqJson['tracks']['items']:
        print(thing['name'])
        
    trackId = reqJson['tracks']['items'][0]['id']
    
    req = requests.get("https://api.spotify.com/v1/tracks/" + trackId)
    reqJson = req.json()
    
    print(reqJson['preview_url'])
    
    print("About to return")
    return render_template('test.html', link=reqJson['preview_url'])

@app.route('/gettracks', methods=['GET'])
def listofTracks(query):
    payload1 = {'Authorization': 'Bearer ' +access_token}
    req = requests.get("https://api.spotify.com/v1/search?q=" + query + "&type=track", headers=payload1)
    currentList = req.json()
    
    return currentList['tracks']
    
def previewTrack(track_id):
    for thing in currentList['tracks']['items']:
        if track_id == thing['id']:
            return thing['preview_url']
    

#ab = requests.post("https://www.freesound.org/apiv2/oauth2/access_token/", data={'client_id': '5dc0cf6f3d88bf59f954', 'client_secret': "482b63ff00aef82733c1e1049a06837dbe558aee", 'grant_type': 'authorization_code', 'code': code})

# ret = requests.get("https://www.freesound.org/apiv2/sounds/14854/download/?token="+accessToken)
