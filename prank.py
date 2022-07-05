import pyqrcode
from pyqrcode import QRCode
x = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
url = pyqrcode.create(x)
url.svg("qr.svg", scale=8)