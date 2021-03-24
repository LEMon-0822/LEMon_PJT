import numpy as np
import cv2

img = cv2.imread("F:/rabbit cornea experiment/Rabbit collagen sheet/4 weeks after/#2/4 weeks sample #2_XZ.png", cv2.IMREAD_UNCHANGED)
img2 = img.copy
k = cv2.getStructuringElement(cv2.MORPH_RECT,(4,4))
img = cv2.fastNlMeansDenoisingColored(img,None,13,13,7,21)
img = cv2.GaussianBlur(img, (3,3), 0)
img = cv2.dilate(img, k)
img_erod = cv2.erode(img, k)

cv2.imshow("contour",img)
cv2.imshow("erod",img_erod)
cv2.waitKey(0)

img2 =cv2.Canny(img,80, 100)
img2_erod = cv2.Canny(img_erod,80,100)


cv2.imshow("contour",img2)
cv2.imshow("erod", img2_erod)
cv2.waitKey(0)
cv2.destroyAllWindows()

