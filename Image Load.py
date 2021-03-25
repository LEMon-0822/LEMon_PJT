import numpy as np
import cv2

file_path = "F:/rabbit cornea experiment/Test data/Control/"
file_name = "Control.bmp_"
file_number = np.array(range(10))
file_type = ".bmp"

for i in file_number:
    Num = str(i)
    print(file_path+file_name+Num.zfill(4)+file_type)
# img = cv2.imread(file_path+file_name+str(file_number)+file_type,cv2.IMREAD_UNCHANGED)
# print(file_path+file_name+str(file_number)+file_type)
# cv2.imshow("contour", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()