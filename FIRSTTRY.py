import glob
import cv2
import numpy as np
import os
test = cv2.imread("TEST_1.tif")
key = int(input('Enter Key for encryption of Image : '))
print('Key for encryption : ', key)
for f in glob.iglob("database/*"):
    print(f)
    fin = open(f, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
	    image[index] = values ^ key

    fin = open(f, 'wb')	
    fin.write(image)
    fin.close()
    print('Encryption Done...')
    cv2.imshow("image"+f, cv2.resize(test, None, fx=1, fy=1))
#C:/Users/anany/Desktop/Python/FINGERPRINT/database/
