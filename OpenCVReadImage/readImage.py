import cv2


def read_image():
    src_img = cv2.imread(r"C:\Users\Administrator\Desktop\1.jpg")
    cv2.namedWindow("TestImg", 0)
    cv2.imshow("TestImg", src_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


read_image()





