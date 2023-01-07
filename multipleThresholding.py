import cv2 as cv

original_image = cv.imread('images_train/candy_crush_image/Candy.JPG')
person_image = cv.imread('images_train/candy_crush_image/Beans.JPG')
# person_image = cv.imread('images_train/Chimny.JPG')
# person_image = cv.imread('images_train/gtatempsa.jpg',cv.IMREAD_REDUCED_COLOR_4)



## Finding this image in original image.....
result = cv.matchTemplate(original_image,person_image,cv.TM_CCOEFF_NORMED)
cv.imshow('RESULT ::' , result)
min_val , max_val , min_loc , max_loc = cv.minMaxLoc(result)
# print('min value ' , min_val)
# print('min loc ' , min_loc)
print('max value ' , max_val)
print('max loc ' , max_loc)

thresholdValue = max_val

perosn_img_w = person_image.shape[1]
perosn_img_h = person_image.shape[0]

print('person height',perosn_img_h)
print('person width',perosn_img_w)

top_left = max_loc
bottom_right = (top_left[0]+perosn_img_w , top_left[1]+perosn_img_h)

if(max_val>=thresholdValue):
    cv.rectangle(original_image,top_left , bottom_right , color=(0,255,0),thickness=2)
    # cv.circle(original_image,max_loc,15,(255,0,0),2)

cv.imshow('ORIGINAL_IMAGE ::' , original_image)
cv.imshow('PERSON_IMAGE ::' , person_image)
cv.waitKey()