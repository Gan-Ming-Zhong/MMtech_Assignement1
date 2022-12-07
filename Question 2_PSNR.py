import numpy as np
import cv2
import math
import imageio
from matplotlib import pyplot as plt
path = 'C:/Users/User/Desktop/method1_frame'

def summarizeVideo(videoFile, duration):
    
    cap = cv2.VideoCapture(videoFile)
    framesList=[]
    total_mse=0
    PSNR=0
    
    ret, frame = cap.read()
    count=0
    #framesList.append(frame)
    cv2.imwrite("frame%d.jpg" % count, frame)
    
    while(cap.isOpened()):
        prev_frame=frame
        ret, frame = cap.read()

        if ret==True:
            i,j,c=frame.shape
            mse = np.mean(((frame - prev_frame) ** 2)/(c*i*j))
            #print("MSE= ",mse)
            
            # if mse==0, there is not much changes  
            if mse<= 1e-6 :
                PSNR+=100
            else:
                PIXEL_MAX = 255.0
                PSNR +=10 * math.log10((PIXEL_MAX **2)/ mse)
                count+=1
                cv2.imwrite("frame%d.jpg" % count, frame)
                framesList.append("frame%d.jpg" % count)
                cv2.imwrite(os.path.join(path , 'frame%d.jpg'% count), frame)
                
            
        else:
            break
            
    print("PSNR= ",PSNR)
    cap.release()


    return framesList



fig=plt.figure()

videoFile = 'surveillance_5.mp4'
framesList=summarizeVideo(videoFile,10) #10 minutes
# Visualize the first 20 frames

for i, imf in enumerate(framesList[:20]):
    
    fig.add_subplot(4, 5, 1+i)
    im=cv2.imread(imf)
    plt.imshow(im)
    plt.axis('off')
