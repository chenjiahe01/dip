import sys
import os
import cv2

from PIL import Image
# from PIL import Image


def CatchUsbVideo(window_name):
    
    cv2.namedWindow(window_name)
    imagepath = "D:\\‪5903040bf4146.jpg"
    print(os.path.exists(imagepath))
    image = cv2.imread(imagepath,0)
    
    #cv2.imshow("原图",image)
    classfier = cv2.CascadeClassifier(
        "D:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_alt2.xml")

    color = (0, 255, 0)
    #grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
    faces = classfier.detectMultiScale(
    image, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
    
    for(x,y,w,h) in faces:

     cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)

    #cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

    # 释放摄像头并销毁所有窗口
    # cap.release()
    #cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage:%s camera_id\r\n" % (sys.argv[0]))
    else:
        CatchUsbVideo("识别人脸区域")
