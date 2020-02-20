
import cv2
image = cv2.imread("/home/user/Загрузки/fgd.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(image, 127, 255, 0)
cv2.imwrite("/home/user/Загрузки/fgd.jpg", threshold_image)
cv2.imshow("Gray", gray_image)
cv2.imshow("Threshold", threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
