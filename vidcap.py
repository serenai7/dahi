import cv2
import numpy as np
import pytesseract
import os
import time
from PIL import Image

#açılacak videonun ismi
vidname = "{}.mp4".format("")

#soruların yazdıralacağı dosyanın ismi
file = open("{}.txt".format(""), "w")

#beyaz renk BGR 
boundaries = ([175, 175, 175], [255, 255, 255])

sorular = []

def oku(img, boundaries):
    lower = np.array(boundaries[0], dtype = "uint8")
    upper = np.array(boundaries[1], dtype = "uint8")
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask = mask)
	
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, output)
    text = pytesseract.image_to_string(Image.open(filename), lang = "tur")
    return [text, filename, output]
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(vidname)
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
    print("Error opening video stream or file")

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

n = 0
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        n += 1
        if n % 150 == 0: #burayı adam edicem şu an yaklaşık 6 saniyede bir görüntü alıyor 
            #fps = cap.get(cv2.CAP_PROP_FPS)
        		#cv2.imshow('Frame',frame)
            result, img = cap.read()
            #img = cv2.QueryFrame(cap)
            text, filename, out_img = oku(img, boundaries)
            if "?" in text:
                sorular.append(text)
                cv2.imwrite("{}.png".format(str(n)), out_img)
                #cevap verici
                #time.sleep(10)           
            print(n)
    else:
        break

			
		
    # Press Q on keyboard to  exit
    #if cv2.waitKey(25) & 0xFF == ord('q'):
        #break
 

 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

file.write(str(sorular))
file.close()


print(sorular)
