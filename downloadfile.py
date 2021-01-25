import requests
url = 'https://drive.google.com/open?id=1PIBW_0iapDv7ylFr8mzSotsHB-_Gylfo'
r = requests.get(url, allow_redirects=True)
open('class1stmarigold.pdf','wb').write(r, contents)