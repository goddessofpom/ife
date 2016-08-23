import requests

r = requests.get("https://raw.githubusercontent.com/sunbard/QRCode/master/a.plist")

print r.elapsed