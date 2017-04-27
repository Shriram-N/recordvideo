import numpy as np
import cv2
import time
import threading
import os


def play_voice():
	os.system("mplayer record.wav")
	
	return "play the video"

def play_video():
	cap = cv2.VideoCapture('/home/pi/video/output.avi')
	
	while(cap.isOpened()):
		ret, frame = cap.read()

		#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		time.sleep(0.12)
	
		cv2.imshow('frame',frame)
		cv2.waitKey(1)

	cap.release()
	cv2.destroyAllWindows()
	return "play the voice"


pvo = threading.Thread(name='play_voice', target=play_voice)
pvi = threading.Thread(name='play_video', target=play_video)
#w2 = threading.Thread(target=worker)  use default name

pvo.start()
pvi.start()

