def getVideoProperty(VideoFile):
    vid = cv2.VideoCapture(videoFile)
    
    #to obtain the frame rate per second
    vFrameRate=vid.get(cv2.CAP_PROP_FPS)
    
    #to obtain resolution
    resolution=(int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
    #to obtain the video size 
    frames = vid.get(cv2.CAP_PROP_FRAME_COUNT)
    
    seconds = round(frames / vFrameRate)
    
    bitrate=videoCapture.get(cv2.CAP_PROP_BITRATE)
    videoSize = seconds*bitrate
    videoSize=videoSize/(1024*8)
    
    return vFrameRate, resolution, videoSize;

videoFile="surveillance_5.mp4";
vFrameRate, resolution, videoSize = getVideoProperty(videoFile);

print("Frame Rate = %s frame per second\nResolution=%s\nVideo Size=%s Mbytes" % (vFrameRate,resolution,videoSize))
