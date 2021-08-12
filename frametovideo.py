import cv2 as cv
import os
import numpy as np
from os.path import isfile,join

def convert_pictures_to_video(pathIn,pathOut,fps,time):
    frame_array=[]
    files=[f for f in os.listdir(pathIn) if isfile(join(pathIn,f))]

    for i in range(len(files)):
        filename=pathIn+files[i]
        print(filename)
        # reading texts
        # img = np.loadtxt(filename,dtype=int)
        img=cv.imread(filename)
        # height=len(img)
        # width=len(img[0])
        
        height,width,layers=img.shape
        size=(width,height)
        for k in range(time):
            frame_array.append(img)
    print(len(frame_array))
    out=cv.VideoWriter(pathOut,cv.VideoWriter_fourcc(*'mp4v'),fps,size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
    
directory='D:\\Documents\\noveno\\tesis\\Classic FMM'
pathIn=directory+'\\Individual\\'
pathOut=directory+'\\videos\\video_fast4.avi'
fps=10
time=20
convert_pictures_to_video(pathIn,pathOut,fps,time)
