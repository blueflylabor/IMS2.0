''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)
	==> Faces will be stored on a directory: dataset/ (if does not exist, pls create one)
	==> Each face will have a unique numeric integer ID as 1, 2, 3, etc                       



'''

import cv2
import os
import tkinter as tk


def dataset(face_id):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    # face_id = input('\n enter user id end press <return> ==>  ')

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0

    while True:

        ret, img = cam.read()
        img = cv2.flip(img, 1)  # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 10)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("../dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 500:  # Take 30 face sample and stop video
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()


def buildwin():
    delFrame = tk.Tk()
    delFrame.geometry('400x300+700+200')
    delFrame.title('创建人脸对象')
    delFrame.resizable(False, False)
    del_id = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(delFrame, text='账号: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_del_id = tk.Entry(delFrame, textvariable=del_id)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_del_id.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

    def confirm():
        face_id = entry_del_id
        delFrame.destroy()
        dataset(del_id.get())

    btn_confirm_delstu = tk.Button(delFrame, text='确定', command=confirm)
    btn_confirm_delstu.place(x=260, y=260)
    delFrame.mainloop()


def main():
    buildwin()


#main()
dataset(13)
