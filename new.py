import cv2 as cv


original_image = cv.imread('images_train/gta sa.jpg',cv.IMREAD_REDUCED_COLOR_4)
template_image = cv.imread('images_train/gta_sa_car.jpg',cv.IMREAD_REDUCED_COLOR_4)
# cv.imshow("original_image",original_image)
# cv.imshow('template_image',template_image)

result = cv.matchTemplate(original_image,template_image,cv.TM_CCOEFF_NORMED)
# cv.imshow("result",result)

min_val , max_val , min_loc , max_loc = cv.minMaxLoc(result)

print("This is max value : " , max_val)
print("this is max_loc",max_loc)


temp_Img_w = template_image.shape[1]
temp_Img_h = template_image.shape[0]










cv.waitKey()