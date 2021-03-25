import numpy as np
import cv2

img = cv2.imread("F:/rabbit cornea experiment/Rabbit collagen sheet/2 weeks after/#8/2 weeks sample #8_XZ.png", cv2.IMREAD_UNCHANGED)
img2 = img.copy

# k1 = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# k2 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
k1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
k2 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

cv2.imshow("contour",img)
cv2.waitKey(0)

img = cv2.fastNlMeansDenoisingColored(img,None,12,12,6,21)
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

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k1)
# img2 =cv2.Canny(img, 50, 170)
#img2_erod = cv2.Canny(img,40,80)

merged = np.hstack((img,gradient))
cv2.imshow("contour",merged)
#cv2.imshow("erod", img2_erod)
cv2.waitKey(0)

img2 =cv2.Canny(merged, 50, 170)
cv2.imshow("contour",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

