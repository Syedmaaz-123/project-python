import qrcode as qr

img=qr.make("hello world")
img.save("qrcode.png")