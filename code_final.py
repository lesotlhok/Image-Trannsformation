# this is my DIP final project: 3121999299 Lesotlho Koorapetse
import tkinter as tk
from tkinter import filedialog

import cv2
import os
from os.path import isfile, join
import shutil

root = tk.Tk()
root.withdraw()





def pictures_to_video(pathIn, pathOut, fps, time):
    """this function converts image to video"""

    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    for i in range(len(files)):
        filename = pathIn + files[i]
        '''Reading images'''
        img = cv2.imread(filename)
        # img = cv2.rotate (img, rotateCode=3)


        img = cv2.resize(img, (1920, 1080))  # Resizing images to the required size'''
        height, width, layers = img.shape
        size = (width, height)

        for k in range(time):
            frame_array.append(img)

    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)  # Converting video format
    for i in range(len(frame_array)):
        out.write(frame_array[i])


        cv2.waitKey(1)

    out.release()


pathIn = filedialog.askdirectory(title='Select Directory') + '/'  # Selecting Image Dir and saving video to same path
# NB, this does not overwrite. always delete video file when rerunning the code.
pathOut = pathIn + 'video_output.avi'  # selection path to save output result
# pathOut = filedialog.asksaveasfile(title="Save File", filetypes =(('video files', '.avi'), ('all files', '*.*')))
print('Out video is saved here {} '.format(pathOut))

fps = 30
time = 20  # time for each image on video
pictures_to_video(pathIn, pathOut, fps, time)





