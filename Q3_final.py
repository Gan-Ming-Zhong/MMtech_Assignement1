import numpy as np
import cv2
import os
from PIL import Image
from os.path import isfile,join
from moviepy.editor import *

def encodeVideoAsMJPEG(videoFile,duration):
    
    cap = cv2.VideoCapture(videoFile)

    destinationFolder="C:\\Users\\User\Desktop\\destination_folder"
    fps = cap.get(cv2.CAP_PROP_FPS)
    #print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    vid = VideoFileClip(videoFile)
    trim_vid = vid.subclip(0,duration*60)
    trim_vid.write_videofile(destinationFolder+"\\10min_surveillance.mp4", codec = 'libx264')
    #second=duration*60
    video_10min = cv2.VideoCapture(destinationFolder+"\\10min_surveillance.mp4")
    #frame_10min=second*fps
    #print(frame_10min)
    count=0
    while(video_10min.isOpened()):
        ret, frame = video_10min.read()
        if ret==True:

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



    cv2.destroyAllWindows()
    compressionRatio=0

    os.chdir(r"C:\\Users\\User\Desktop\\destination_folder\\output_folder_uncompressed")
    video_size_uncompressed=sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)])
    #print(video_size_uncompressed)

    os.chdir(r"C:\\Users\\User\Desktop\\destination_folder\\output_folder_compressed")
    video_size_compressed=sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)])
    #print(video_size_compressed)

    compressionRatio=video_size_uncompressed/video_size_compressed
 


    return (destinationFolder, compressionRatio)



videoFile = "D:\mmu subject\Multitech apps\\assignment1_Q3\surveillance_5.mp4";
folder,CR=encodeVideoAsMJPEG(videoFile,10) #10 minutes

print(CR)
