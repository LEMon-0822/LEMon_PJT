import numpy as np
import cv2

img = cv2.imread("F:/rabbit cornea experiment/Rabbit collagen sheet/2 weeks after/#8/2 weeks sample #8_XZ.png", cv2.IMREAD_UNCHANGED)
img2 = img.copy
k1 = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
k2 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

cv2.imshow("contour",img)
cv2.waitKey(0)

img = cv2.fastNlMeansDenoisingColored(img,None,12,12,7,13)
#img = cv2.GaussianBlur(img, (3,3), 0)


img = cv2.dilate(img, k1)
cv2.imshow("contour",img)
cv2.waitKey(0)


img = cv2.erode(img, k1)
cv2.imshow("contour",img)
cv2.waitKey(0)

cv2.imshow("contour",img)
cv2.waitKey(0)
#cv2.imshow("erod",img_erod)


img2 =cv2.Canny(img, 50, 170)
#img2_erod = cv2.Canny(img,40,80)


cv2.imshow("contour",img2)
#cv2.imshow("erod", img2_erod)
cv2.waitKey(0)
cv2.destroyAllWindows()

