import cv2
import os
import threading
import time
timeout = time.time() + 10

def record_voice():
   print threading.currentThread().getName(), 'voice Starting'
   os.system("arecord -D plughw:1,0 -d 10 -r 16000  -f S16_LE -c 1 record.wav")
   print threading.currentThread().getName(), 'voice exiting'
   return "recorded for seconds"
#os.system("arecord -D plughw:1,0 -d 5 -r 16000  -f S16_LE -c 1 record.wav >> test.text")

def record_video():
    # find the webcam
    print threading.currentThread().getName(), 'video Starting'
    capture = cv2.VideoCapture(0)

    w=int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
    h=int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))
    # video recorder
    fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
    video_writer = cv2.VideoWriter("output.avi", fourcc, 25, (w, h))

    # record video
    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret and time.time() < timeout:
            video_writer.write(frame)
            cv2.imshow('Video Stream', frame)

        else:
            break

    capture.release()
    video_writer.release()
    cv2.destroyAllWindows()
    print threading.currentThread().getName(), 'video exiting'
    return ""


rvi = threading.Thread(name='record_video', target=record_video)
rvo = threading.Thread(name='record_voice', target=record_voice)
#w2 = threading.Thread(target=worker)  use default name

rvo.start()
rvi.start()

