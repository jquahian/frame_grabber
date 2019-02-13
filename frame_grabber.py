import numpy as np
import cv2
import os

dirpath = 'D:/auto_focus/subc4'

outpath = 'D:/auto_focus/subc4/frames'

# return list of videos in the directory
videos = os.listdir(dirpath)

# save each from from each video in the list
for i in range(0, len(videos)):
	# frame incrementor
	count = 0

	# define our input file path
	file_path = os.path.join(dirpath, videos[i])

	# start the video capture
	cap = cv2.VideoCapture(file_path)

	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

	print(f"video width: {width} \nvideo height: {height}")

	while (cap.isOpened()):

	    # Capture frame-by-frame
	    ret, frame = cap.read()
	    
	    if ret == True:
	        print('Read %d frame: ' % count, ret)
	       	file_name = videos[i]
	       	frame = cv2.cvtColor(frame.astype(np.uint8), cv2.COLOR_RGB2GRAY)
	       	frame = frame[:height, :width]
	        cv2.imwrite(os.path.join(outpath, '{}_frame{:d}.jpg'.format(file_name[:-4], count)), frame)
	        count += 1
	    else:
	        break

cap.release()
cv2.destroyAllWindows()
