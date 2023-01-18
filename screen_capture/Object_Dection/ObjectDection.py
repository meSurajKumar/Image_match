import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def findTargetPosition(targetImagePath,originalImage , threshold=0.30 , markers_options = None):

    
    temp_image = cv.imread(targetImagePath,cv.IMREAD_UNCHANGED)
    method = cv.TM_CCOEFF_NORMED

    ## Finding this image in original image.....
    result = cv.matchTemplate(originalImage,temp_image,method)
    cv.imshow('RESULT ::' , result)
    min_val , max_val , min_loc , max_loc = cv.minMaxLoc(result)

    temp_img_w = temp_image.shape[1]
    temp_image_h = temp_image.shape[0]
    # thresholdValue = max_val - 0.68

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    # print('data ::',locations)

    # We are creating group of rectangle here (x,y,w,h)
    rectangles = []
    for loc in locations:
        rect =[int(loc[0]),int(loc[1]),temp_img_w,temp_image_h] 
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, weights = cv.groupRectangles(rectangles,1,0.5)
    # print("rect :",rectangles)

    points = []
    if len(rectangles):
        print('image found ::')

        line_color = (0,0,255)
        line_type = cv.LINE_4
        rectangle_color = (0,255,0)
        marker_color = (255,0,0)
        marker_type = cv.MARKER_CROSS
        marker_size = 20

        for (x,y,w,h) in rectangles:
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            points.append((center_x,center_y))

            if markers_options == 'rectangles':
                top_left = (x,y)
                bottom_right = (x+w ,y+h)
                # cv.rectangle(originalImage,top_left , bottom_right , color=rectangle_color,lineType=line_type,thickness=2)
                cv.rectangle(originalImage,top_left , bottom_right , (0,255,0),cv.LINE_4,2)

            elif markers_options == 'points':
                cv.drawMarker(originalImage,(center_x,center_y),color=marker_color,markerType=marker_type,markerSize=marker_size,thickness=2)
    if markers_options:
        cv.imshow('ORIGINAL_IMAGE ::' , originalImage)
        # cv.waitKey()
    return points

# points = findTargetPosition('flower.JPG','farm3.jpg',markers_options='points')

# points = findTargetPosition('flower.JPG','farm3.jpg',markers_options='rectangles')

print('Working Fine')