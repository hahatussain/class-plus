import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Closing")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "admn_no_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} Registered!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()