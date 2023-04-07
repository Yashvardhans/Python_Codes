import cv2


cam = cv2.VideoCapture(0)
cv2.namedWindow("Screen shot capture")

img_counter = 0


while True:
    ret , frame = cam.read()
    if not ret:
        print("Failed")
        break
    cv2.imshow("test" ,frame)
    
    k = cv2.waitKey(1)

    if k% 256 == 27:
        print("escape")
        break
    elif k % 256 == 32:

        img_name = "img_{}.jpg".format(img_counter)

        cv2.imwrite(img_name , frame)
        print("Captured")
        img_counter += 1 




cam.release()

cam.destroyAllWindows()

