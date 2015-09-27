from flask import render_template, request, redirect, url_for, jsonify
import requests, json
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
    global access_token
    if access_token == None:
        code = request.args.get('code')
        req = requests.post("https://accounts.spotify.com/api/token", data={'grant_type': 'authorization_code', 'code': code, 'redirect_uri': 'http://localhost:8080/woo', 'client_id': '9344d5a91349489488cc51637d912e21', 'client_secret': '5cb043cf9fc546bebc91978ec8a95bc6'})
        res = req.json()
        access_token = res['access_token']
        print("This is the access_token " + access_token);
    
    # payload1 = {'Authorization': 'Bearer ' +access_token}
    # payload2 = {'q': 'px3'}
    # req = requests.get("https://api.spotify.com/v1/search?q=px3&type=track", headers=payload1)
    
    # reqJson = req.json()
    
    # for thing in reqJson['tracks']['items']:
    #     print(thing['name'])
        
    # trackId = reqJson['tracks']['items'][0]['id']
    
    # req = requests.get("https://api.spotify.com/v1/tracks/" + trackId)
    # reqJson = req.json()
    
    # print(reqJson['preview_url'])
    
    print("About to return")
    return render_template('test.html')

@app.route('/gettracks', methods=['GET'])
def gettracks():
    try:
        print("something happening")
        query = request.args.get('trackname')
        payload1 = {'Authorization': 'Bearer ' + access_token}
        print(access_token)
        req = requests.get("https://api.spotify.com/v1/search?q=" + query + "&type=track", headers=payload1)
        global currentList
        currentList = req.json()
        print(currentList)
    except Exception:
        print(Exception)
    print("Inside the get functions");
    
    return jsonify(currentList['tracks'])

@app.route('/previewtrack', methods=['GET'])
def previewtrack():
    query = request.args.get('id')
    
    for thing in currentList['tracks']['items']:
        if query == thing['id']:
            req = requests.get("https://api.spotify.com/v1/tracks/" + thing['id'])
            reqJson = req.json()
            return render_template('viz.html', message = reqJson['preview_url'])
            

#ab = requests.post("https://www.freesound.org/apiv2/oauth2/access_token/", data={'client_id': '5dc0cf6f3d88bf59f954', 'client_secret': "482b63ff00aef82733c1e1049a06837dbe558aee", 'grant_type': 'authorization_code', 'code': code})

# ret = requests.get("https://www.freesound.org/apiv2/sounds/14854/download/?token="+accessToken)
