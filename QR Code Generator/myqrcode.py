#pip install this library
import pyqrcode
from pyqrcode import QRCode

link = "https://github.com/pradeepcho-exe"

url = pyqrcode.create(link)

url.svg("GitQRCode.svg", scale=8)
