import cv2

cap = cv2.VideoCapture(0)  # webcam

while cap.isOpened():
    ret, back = cap.read()  # reading from webcam
    if ret:
        # ret is if op is successful or not
        # back is what the camera is reading
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            # save the image
            cv2.imwrite('bgimage.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
