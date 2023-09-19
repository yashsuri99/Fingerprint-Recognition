import glob
import cv2
import numpy as np
import os
print('Note : Encryption key and Decryption key must be same.')
key = int(input('Enter Key for Decryption of Image : '))
print('Key for encryption : ', key)
for f in glob.iglob("database/*"):
        print('Key for Decryption : ', key)
        fin = open(f, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)
        for index, values in enumerate(image):
        	image[index] = values ^ key
        fin = open(f, 'wb')
        fin.write(image)
        fin.close()
        print('Decryption Done...')












