import numpy as np
import cv2
import os
from PIL import Image
from os.path import isfile,join

def encodeVideoAsMJPEG(videoFile,duration):
    
    cap = cv2.VideoCapture(videoFile)

    destinationFolder="C:\\Users\\User\Desktop\\destination_folder"
    fps = cap.get(cv2.CAP_PROP_FPS)
    print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    second=duration*60

    frame_10min=second*fps
    print(frame_10min)
    count=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            if(count<frame_10min):

                os.chdir(r"C:\\Users\\User\Desktop\\destination_folder\\output_folder_uncompressed")
                cv2.imwrite('frame%d.jpg'% count , frame) 

                converted = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                pil_im = Image.fromarray(converted)
                os.chdir(r"C:\\Users\\User\Desktop\\destination_folder\\output_folder_compressed")
                out_frame=pil_im.save("Compressed_"+"frame%d.jpg"% count, "JPEG", optimize = True, quality = 10)
                
                count=count+1
                
        else:
            break
    cap.release()


    #out.release()
    cv2.destroyAllWindows()
    compressionRatio=0

    os.chdir(r"C:\\Users\\User\Desktop\\output_folder_uncompressed")
    video_size_uncompressed=sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)])
    print(video_size_uncompressed)

    os.chdir(r"C:\\Users\\User\Desktop\\output_folder")
    video_size_compressed=sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)])
 
    compressionRatio=video_size_uncompressed/video_size_compressed
 


    return (destinationFolder, compressionRatio)



videoFile = "D:\mmu subject\Multitech apps\\assignment1_Q3\surveillance_5.mp4";
folder,CR=encodeVideoAsMJPEG(videoFile,10) #10 minutes
