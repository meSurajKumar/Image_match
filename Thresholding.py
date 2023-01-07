import cv2 as cv
# import numpy as np 

original_image = cv.imread('images_train/gta sa.jpg',cv.IMREAD_REDUCED_COLOR_4)
template_image = cv.imread('images_train/gta_sa_car.jpg',cv.IMREAD_REDUCED_COLOR_4)

'''
Original_image : This is the source image on which we have to find the template image.
Template_image : This is the image we have to find. 

'''
#--------------------------------------###########################-------------------------------------------#
'''
cv.imshow('origanal image',original_image) 
cv.imshow('template image',template_image)


# Also You can check that it's working or not

'''
#------------------------Below code explanation is given in the bottom--------------------------------------#


result  = cv.matchTemplate(original_image,template_image,cv.TM_CCOEFF_NORMED)

# cv.imshow("result1",result)

min_val , max_val , min_loc , max_loc = cv.minMaxLoc(result)
print('This is the max value', max_val)
print('This is the max loc', max_loc)


temp_Img_w = template_image.shape[1]
temp_Img_h = template_image.shape[0]


top_left = max_loc
bottom_right = (top_left[0]+temp_Img_w ,top_left[1]+temp_Img_h)

threshold = 0.65 # MY max_val = 0.71
if max_val >=threshold:
    cv.rectangle(original_image,top_left ,bottom_right,color = (0,255,0),thickness=2,lineType=cv.LINE_4)
    cv.imshow('result',original_image)
    cv.imwrite('final_image.jpg',original_image)
    print('template found')
else:
    print('not found')
cv.waitKey()
