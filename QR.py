#make a qrcode from python
import qrcode

img = qrcode.make("https://n2qp.github.io/k4x/")
img.save("Mywb.jpg")