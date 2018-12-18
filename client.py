import requests

url = "http://172.19.4.225:5000/upload"
files = {'files': open('hatispa.wav', 'rb')}
r = requests.post(url, files=files)
