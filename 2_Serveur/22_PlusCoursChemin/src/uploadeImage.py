
import base64
import requests
import qrcode

key_imgbb = "4f555dcb35f435943be57971b27ab3af"
with open("../image/resultatDuChemin.png", "rb") as file:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": key_imgbb,
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)
res = res.json()
url = res['data']["url"]

img = qrcode.make(url)
type(img)  # qrcode.image.pil.PilImage
img.show()
img.save("../image/QRcode.png")