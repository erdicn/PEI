#==================================================================================================================================
# Purpose  : Very simple color-based position tracking using Opencv/python : plot the center of a yellow colored object
#
# System   : OpenCV version: 4.5.3 and Python 3.7 (or later)
# Conda env: opencv  (macbook pro 2016)
#
# Comment  : * The code is freely enriched from [1].
#            * The mask must be calibrated manually based on color threshold of the target.
#            * The coordinates (in the pixel frame) are stored as a function of time in a csv file (and plotted).
#            * Output the video with tracking circle.
#
# Status   : no bug known,
#
# Released : v 0.1 (jcc) March 2022 (Sorbonne Université)
#
# Reference: [1] S. Hymel, "Color Object Detection with OpenCV and Python", Sep. 20, 2016  (url:https://www.sparkfun.com/news/2191)
#==================================================================================================================================
# TODO : you can explore complementary/alternatives here:
#   * https://stackoverflow.com/questions/39498771/python-opencv-get-bottom-most-value-of-mask
#   * https://answers.opencv.org/question/201032/how-can-i-use-opencv-to-find-the-center-of-mass/
#   * https://www.bluetin.io/opencv/object-detection-tracking-opencv-python/
#==================================================================================================================================
import cv2 # Importing the opencv module
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
import imutils

# Minimum required radius of enclosing circle of contour
MIN_RADIUS = 0
MAX_RADIUS = 10
# shown opencv version
print ("OpenCV version :  {0}".format(cv2.__version__))    # OpenCV version :  4.5.3
# choose video
cv2.namedWindow("preview")
filemane = "Test_TLD1.mov"
#####                                                                                                         #####
##### RGB Color range for color detection - A ajuster par l'utilisateur en fonction de la couleur de la cible #####
#####                                                                                                         #####
lower_rank = np.array([  8,230,55  ]) 
upper_rank = np.array([ 13,255,150])
# Convert to HSV
THRESHOLD_LOW  = np.array(lower_rank, dtype = "uint8")
THRESHOLD_HIGH = np.array(upper_rank, dtype = "uint8")
# load video
cap      = cv2.VideoCapture(filemane)
print ("open file: ",filemane)
# get framerate
framerate = cap.get(cv2.CAP_PROP_FPS)
print ('framerate: ',framerate, 'fps')
#Creating a Pandas DataFrame To Store Data Point
data_features = ['time', 'cx', 'cy']
data_pts     = pd.DataFrame(data = None, columns = data_features , dtype = float)
#i = 0
start = time.time()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out    = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
  
# INFINITE LOOP
while True:
  # take frame
    success, img = cap.read()
  # Reading The Current Time
    current_time = time.time() - start
  # break if video ends
    if (not success):
          break   
    img = imutils.resize(img, width=800)
    # Blur image to remove noise
    img_filter = cv2.GaussianBlur(img.copy(), (13, 13), 0)
    img_filter = cv2.GaussianBlur(img.copy(), (5, 5), 0)
    # Convert image from BGR to HSV
    img_filter = cv2.cvtColor(img_filter, cv2.COLOR_BGR2HSV)
   # Set pixels to white if in color range, others to black (binary bitmap)
    img_binary = cv2.inRange(img_filter.copy(), THRESHOLD_LOW, THRESHOLD_HIGH)
    # Dilate image to make white blobs larger
    mask = cv2.erode(img_binary, None, iterations=0)   
    mask = cv2.dilate(mask     , None, iterations=0)

    # Find center of object using contours instead of blob detection. From:
    # http://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
    img_contours = mask.copy()
    contours = cv2.findContours(img_contours, cv2.RETR_EXTERNAL, \
        cv2.CHAIN_APPROX_SIMPLE)[-2]
  # Find the largest contour and use it to compute the min enclosing circle
    center = None
    radius = 0
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if M["m00"] > 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if  int(M["m01"] / M["m00"]) > 1000   :
                  center = None
#           print (int(M["m01"] / M["m00"])           )
            #if radius < MIN_RADIUS:
            #    center = None
            #if radius > MAX_RADIUS:
            #    center = None
  # Print out the location and size (radius) of the largest detected contour
    if center != None:
        #print (str(center) + " " + str(radius)   )
       #Save The Data Points
        data_pts.loc[data_pts.size/3] = [current_time, M["m10"]/M["m00"], M["m01"]/M["m00"]]
  # Draw a green circle around the largest enclosed contour
    if center != None:
        cv2.circle(img, center, int(round(radius)), (255, 255, 0),2)
    #   cv2.circle(img, center, 10, (255, 255, 0),8)

  # display the frame 
    cv2.imshow('webcam', img)
    cv2.imshow('binary', img_binary)
   #cv2.imshow('contours', img_contours)​
  # save the video with the postion tracker
    out.write(img) 

  # quit if 'q' touch is pressed
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break

#print ("Number of dataframe:", cx.shape[0])
print ("Total time         :", current_time)
# close displaying windows
cap.release()
cv2.destroyAllWindows()
# Plot vertical position as a function of time
#plt.plot(data_pts['time'],-data_pts['cy'],'.-')
plt.plot(data_pts['time'],-data_pts['cx'],'.-')
plt.xlabel('time')
plt.ylabel('cy [pixel]')
plt.grid()
plt.show()
#Save plot and export data as csv file
plt.savefig('bouncing_ball.png')
data_pts.to_csv('data_position.txt', sep=" ")

# EOF
