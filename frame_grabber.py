import numpy as np
import cv2
import os

# return list of videos in the directory
videos = os.listdir('Data')

# save each from from each video in the list
for i in range(0, len(videos)):
	# frame incrementor
	count = 0
	# define our input file path
	file_path = os.path.join('Data', videos[i])
	# start the video capture
	cap = cv2.VideoCapture(file_path)

	while (cap.isOpened()):

	    # Capture frame-by-frame
	    ret, frame = cap.read()
	    
	    if ret == True:
	        print('Read %d frame: ' % count, ret)
	       	file_name = videos[i]
	       	frame = cv2.cvtColor(frame.astype(np.uint8), cv2.COLOR_RGB2GRAY)
	       	# left to right is x, top to bottom is y
	       	# images are 800 x 600
	       	# top left corner is (0,0), bottom right corner is (800, 600)
	       	# these values are based off of trial and error:
	       	# for cropping: x1, y1 = 100, 60 
	       	# for cropping: x2, y2 = 800, 600
	       	frame = frame[60:600+1, 100:800+1]
	        cv2.imwrite(os.path.join('Output', '{}_frame{:d}.jpg'.format(file_name[:-4], count)), frame)  # save frame as JPEG file
	        count += 1
	    else:
	        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
