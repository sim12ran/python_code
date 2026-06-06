#  we have to import a module in python to generate qr code

import qrcode as qr
#we have to create an object of the QRCode class
img = qr.make("I am Simran kumari")
img.save("text.png")



