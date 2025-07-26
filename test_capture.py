from window_capture import WindowCapture
import cv2

cap = WindowCapture()
frame = cap.get_screenshot()

cv2.imshow("Mac Screenshot Test", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
