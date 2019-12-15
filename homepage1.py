#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter

from PIL import ImageTk
import apputils
import clock
import game

PythonVersion = 3
from tkinter.ttk import *


# import tkinter.filedialog as tkFileDialog
# import tkinter.simpledialog as tkSimpleDialog    #askstring()


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('信息管理系统1.0')
        self.master.geometry('1181x722+400+200')
        self.master.resizable(False, False)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        # image_file = tkinter.PhotoImage(file='3.gif')

        # image = self.Picture1.create_image(200, 0, anchor='n', image=image_file)
        tkinter.Canvas('')
        # self.Picture1.place(relx=0., rely=0., relwidth=0.184, relheight=0.278)

        self.style.configure('Command1.TButton', font=('宋体', 11))
        self.Command1 = Button(self.top, text='提交信息', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0., rely=0.170, relwidth=0.184, relheight=0.057)

        self.style.configure('Command2.TButton', font=('宋体', 11))
        self.Command2 = Button(self.top, text='修改信息', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0., rely=0.240, relwidth=0.184, relheight=0.057)

        self.style.configure('Command3.TButton', font=('宋体', 11))
        self.Command3 = Button(self.top, text='删除信息', command=self.Command3_Cmd, style='Command3.TButton')
        self.Command3.place(relx=0., rely=0.310, relwidth=0.184, relheight=0.057)

        self.style.configure('Command4.TButton', font=('宋体', 11))
        self.Command4 = Button(self.top, text='查询信息', command=self.Command4_Cmd, style='Command4.TButton')
        self.Command4.place(relx=0., rely=0.380, relwidth=0.184, relheight=0.057)

        self.style.configure('Command5.TButton', font=('宋体', 11))
        self.Command5 = Button(self.top, text='显示所有信息', command=self.Command5_Cmd, style='Command5.TButton')
        self.Command5.place(relx=0., rely=0.450, relwidth=0.184, relheight=0.057)

        self.style.configure('Command6.TButton', font=('宋体', 11))
        self.Command6 = Button(self.top, text='计时器', command=self.Command6_Cmd, style='Command6.TButton')
        self.Command6.place(relx=0., rely=0.520, relwidth=0.184, relheight=0.057)

        self.style.configure('Command7.TButton', font=('宋体', 11))
        self.Command7 = Button(self.top, text='创建图片任务', command=self.Command7_Cmd, style='Command7.TButton')
        self.Command7.place(relx=0., rely=0.590, relwidth=0.184, relheight=0.057)

        self.style.configure('Command8.TButton', font=('宋体', 11))
        self.Command8 = Button(self.top, text='选择图片任务', command=self.Command8_Cmd, style='Command7.TButton')
        self.Command8.place(relx=0., rely=0.660, relwidth=0.184, relheight=0.057)

        self.style.configure('Command9.TButton', font=('宋体', 11))
        self.Command9 = Button(self.top, text='未完待续...', command=self.Command9_Cmd, style='Command7.TButton')
        self.Command9.place(relx=0., rely=0.730, relwidth=0.184, relheight=0.057)

        self.style.configure('Frame1.TLabelframe', font=('宋体', 11))
        self.Frame1 = LabelFrame(self.top, text='', style='Frame1.TLabelframe')
        self.Frame1.place(relx=0.19, rely=0.166, relwidth=0.75, relheight=0.7)
        l1 = Label(self.top, text='欢迎使用河南师范大学IMS1.0信息管理系统', font=('宋体', 20))
        l1.pack()
        text = '欢迎使用河南师范大学IMS1.0信息管理系统'
        clairtitle = '使用声明：'
        clairtext1 = '本系统系本人独立开发，仅供学习研究使用，未经本人授权不得使用'
        clairtext2 = '本系统使用python语言开发'
        clairtext3 = '配合使用MySQL数据库系统'
        clairtext4 = '目前版本仅支持PC端登录'
        clairtext5 = '提供两种登录方式：'
        clairtext6 = '传统密钥登录方式使用更安全的md5加密存储'
        clairtext7 = '人脸识别登录方式使用opencv开源库进行分类获取人脸对象并训练模型进行识别'
        clairtext8 = '技术仅供参考，谢谢使用'
        clairtextlist = [text, clairtitle, clairtext1, clairtext2, clairtext3, clairtext4, clairtext5, clairtext6,
                         clairtext7, clairtext8]
        for i in clairtextlist:
            label = Label(self.Frame1, text=i, font=('宋体', 18))
            label.pack()


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        apputils.addperson()

    def Command2_Cmd(self, event=None):
        apputils.updateperson()

    def Command3_Cmd(self, event=None):
        apputils.delstu()

    def Command4_Cmd(self, event=None):
        apputils.serstu()

    def Command5_Cmd(self, event=None):
        apputils.treeview1()

    def Command6_Cmd(self, event=None):
        clock.main()

    def Command7_Cmd(self, event=None):
        apputils.create_image_mission()

    def Command8_Cmd(self, event=None):
        apputils.choose_image_mission()

    def Command9_Cmd(self, event=None):
        game.main()


def main():
    top = tkinter.Toplevel()
    img = ImageTk.PhotoImage(file="images\\img2.jpg")
    canvas = tkinter.Canvas(top, width=720, height=420)
    canvas.create_image(300, 200, image=img)
    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    Application(top).mainloop()
    try:
        top.destroy()
    except:
        pass


#main()
