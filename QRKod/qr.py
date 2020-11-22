#pip install pypng
#pip install pyqrcode
#pip install pillow
#pip install pyzbar

# Yukarıdaki komutlarla kütüphaneleri indirebilirsiniz.

# QR Kod okuma
from pyzbar.pyzbar import decode
from PIL import Image

d = decode(Image.open('qrcode2.png'))

print(d[0].data.decode('ascii'))



# QR Kod yaratma
import pyqrcode

qr = pyqrcode.create('instagram.com/yazilim.dehasi')
qr.png('qrcode2.png', scale=8)


