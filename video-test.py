# Testing video functionalities in Python
# Myranda Shirk

import cv2
from datetime import datetime

def main():
   
    # directories for saving frames and opening video
    frame_save_path = "./"
    video_path = "./turtle-sample-video.mp4"


    # index for each frame
    i = 1

    wait = 0

    # open video
    video = cv2.VideoCapture(video_path)

    # check that video could open
    if video.isOpened() == False:
        print("Error opening file")
        return

    start_time = datetime.now()

    while video.isOpened():
        ret, frame = video.read()
        font = cv2.FONT_HERSHEY_PLAIN

        if ret == True:
            print("Adding timestamp")
            #add timestamp
            video_time = datetime.now() - start_time
            cv2.putText(frame, str(video_time), (20, 40), font, 2, (255,255,255), 2, cv2.LINE_AA)
            
            # show the video
            cv2.imshow('sample-video', frame)
            cv2.waitKey(100)

        else:
            print("no frames available")
            break

    video.release()
    cv2.destroyAllWindows()

main()
