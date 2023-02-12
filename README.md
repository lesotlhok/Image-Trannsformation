# Image-Trannsformation
Image transformation using python 

The code is a function that converts a series of images into a video. The function starts by creating an empty list called "frame_array" to hold all the frames in the video. It then loops through each image file in the given path and verifies if it's a valid image. If it's not, it moves on to the next one until there are no more files. All the valid image files are then added to "frame_array" as individual frames with their filenames and paths. The function then creates another list of filenames and iterates over them, adding each filename to "frame_array" as an individual frame. The function takes in the path to the image directory, the path where the video will be saved, and the fps (frames per second). The frames are then stored in "frame_array" and converted into a video. The code rotates and resizes each image and saves the video as an MP4 file with a fourcc of mp4v. The code asks the user to select a directory and title for the video file, and saves the video file as an .avi file in the chosen directory.