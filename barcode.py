## FOR STATIC IMAGE 
import cv2
import numpy as np
from pyzbar.pyzbar import  decode
#img=cv2.imread("Qrcode1.png")
#img=cv2.imread("bar2.jpg")
img=cv2.imread("test2.png")
code= decode(img)
print(code)


for barcode in decode(img):
    # print(barcode.rect)
    print(barcode.data)
    myData=barcode.data.decode('utf-8')
    print(myData)

