import cv2 as cv
import numpy as np

def find_stop(path):
    """" 
    
    This function aims to detects stop sign using HSV color space. 
    
    This function identifies red regions, filter them by contour area and shape.
    Flexibility has been satisfied by preventing to repetitions.
    
    Args:
    path : It takes an path way.

    """
    
    from pathlib import Path

    #Converting BGR image to blurred HSV image
    image = cv.imread(path)
    if image is None:
        print("There is no image for given path.")
        return None
    hsv_img = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    
    #Creating variables which correspond to red's boundaries
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    #Creating mask for identifying red regions
    mask1 = cv.inRange(hsv_img, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv_img, lower_red2, upper_red2)
    mask = cv.bitwise_or(mask1, mask2)

    #Finding all contours through built in OpenCV function 
    contours, hierarchies = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    rectangled = image.copy()

    #Filtering contours that are necessary
    for contour in contours: 
        area = cv.contourArea(contour)
        #Avoid noise
        if area > 1000:  
            peri = cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, 0.04 * peri, True)  
            
            #Filtering with respect to number of edges
            if 5 < len(approx) < 11:
                x,y,dx,dy = cv.boundingRect(contour)

                #Drawing filtered contours
                rectangled = cv.rectangle(image,(x,y),(x+dx,y+dy),(255,255,255),2)

                print(f"Center coordinates are that x:{(x+dx)/2} y:{(y+dy)/2}")

    path_ = Path(path)
    cv.imwrite(f"ProcessedImages/{path_.stem}_processed{path_.suffix}",rectangled)

    #Showing results
    cv.imshow("Stop Signed Image",rectangled)
    cv.waitKey(0)

find_stop("Original Images/photo5.jpg")

