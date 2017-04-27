import cv2
import os
import threading
import time
 
class video(threading.Thread):
	 def __init__(self,low,high):
         super(video, self).__init__()
         self.low=low
         self.high=high
         self.total=0
         
     def record_voice():
         os.system("arecord -D plughw:1,0 -d 10 -r 16000  -f S16_LE -c 1 record.wav")
         return "recorded for seconds"
         #os.system("arecord -D plughw:1,0 -d 5 -r 16000  -f S16_LE -c 1 record.wav >> test.text")

     def record_video():
         # find the webcam
         capture = cv2.VideoCapture(0)

         w=int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
         h=int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))
         # video recorder
         fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does no=t exist
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
         return ""
         
      
     def voice_play():
	     cap = cv2.VideoCapture('/home/pi/Desktop/output.avi')
	     while(cap.isOpened()):
		    ret, frame = cap.read()

		    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		    time.sleep(0.1)
		    cv2.imshow('frame',frame)
		    cv2.waitKey(1)

	     cap.release()
	     cv2.destroyAllWindows()
	     return "play the voice"

     def video_play():
	     os.system("aplay record.wav")
	     return "play the video"

