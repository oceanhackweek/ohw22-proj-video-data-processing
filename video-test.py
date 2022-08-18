# Testing video functionalities in Python
# Myranda Shirk

import cv2
from datetime import datetime
from datetime import timedelta

# set a global variable wait time
wait_time = 0

pause_time = 0

interval = 100

click_flag = False



def main():
    # flag for detecting click event
    def mouseClickEvent(event, x, y, flags, param):
        global click_flag
        if event == cv2.EVENT_LBUTTONDOWN:
            print("Mouse click detected")
            '''
            # click flag is whether the button has already been pressed for pause
            # if click flag == 1, play the videol. Otherwise, pause the video
            #click_flag = param[0]
            
            # interval is the amount of time to wait between frames
            #interval = param[1]

            global pause_time, wait_time, interval, click_flag

            if click_flag == 0:
                print("Paused")
                #cv2.waitKey()
                pause_time = datetime.now()
                click_flag = 1
                print("click flag set to 1")
                cv2.waitKey()

            else:
                print("Play")
                current_time = datetime.now()
                elapsed_time = current_time - pause_time
                wait_time = timedelta(milliseconds=interval) + current_time
                cv2.imshow('sample-video', frame)
                cv2.waitKey(interval)
                print("click flag set to 0")
                click_flag = 0

            '''

            click_flag = not click_flag
        else:
            print("unknown event")
        

    # directories for saving frames and opening video
    frame_save_path = "./"
    video_path = "./turtle-sample-video.mp4"


    # index for each frame
    i = 1

    wait = 0

    interval = 100


    # open video
    video = cv2.VideoCapture(video_path)

    # check that video could open
    if video.isOpened() == False:
        print("Error opening file")
        return

    # create window to capture input
    cv2.namedWindow('sample-video')
    cv2.setMouseCallback('sample-video', mouseClickEvent)

    start_time = datetime.now()
    global wait_time
    pause_time = timedelta(milliseconds=0)

    while video.isOpened():

        while click_flag == False:
            ret, frame = video.read()
            font = cv2.FONT_HERSHEY_PLAIN

            if ret == True:
                print("Adding timestamp")
                #add timestamp
                video_time = (datetime.now() - timedelta(milliseconds=wait_time) - pause_time) - start_time
                cv2.putText(frame, str(video_time), (20, 40), font, 2, (255,255,255), 2, cv2.LINE_AA)
            
                cv2.namedWindow('sample-video')
                cv2.setMouseCallback('sample-video', mouseClickEvent)

                # sh    ow the video
                cv2.imshow('sample-video', frame)
            
                cv2.waitKey(interval)
                wait_time = interval



            else:
                print("no frames available")
                video.release()
                cv2.destroyAllWindows()

                return

        pause_start = datetime.now()
        while click_flag:
            
            cv2.waitKey(1)

        pause_end = datetime.now()
        pause_time = pause_end - pause_start

    video.release()
    cv2.destroyAllWindows()

main()
