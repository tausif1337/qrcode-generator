import qrcode

img = qrcode.make("www.facebook.com")
img.save("qrcode.png")