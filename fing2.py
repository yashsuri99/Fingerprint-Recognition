import cv2
import numpy as np
import os
import glob

test = cv2.imread("TEST_1.tif")
cv2.imshow("Original", cv2.resize(test, None, fx=1, fy=1))

cv2.waitKey(0)
cv2.destroyAllWindows()


key = int(input('Enter the security code'))
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
        print('Decryption completed')

        
for file in [file for file in os.listdir("database")]:
    fingerprint_database_image = cv2.imread("./database/"+file)
        

    sift = cv2.xfeatures2d.SIFT_create()
    
    KP1, DES1 = sift.detectAndCompute(test, None)
    KP2, DES2 = sift.detectAndCompute(fingerprint_database_image, None)



    matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), dict()).knnMatch(DES1, DES2, k=2)
    match_points = []
   
    for p, q in matches:
        if p.distance < 0.6*q.distance:
            match_points.append(p)
            keypoints = 0
            if len(KP1) <= len(KP2):
                keypoints = len(KP1)            
            else:
                keypoints = len(KP2)
            if (len(match_points) / keypoints)>0.99:
                print("match percentage: ", len(match_points) / keypoints * 100)
                print("Figerprint ID from database: " + str(file)) 
                result = cv2.drawMatches(test, KP1, fingerprint_database_image, KP2, match_points, None) 
                result = cv2.resize(result, None, fx=2.5, fy=2.5)
                cv2.imshow("result", result)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break;

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
    print('RE-encrypting images..........encrypted again')

