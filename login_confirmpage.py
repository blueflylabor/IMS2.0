import hashlib
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pymysql
import homepage1
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string


def config_image_maker():
    chars = string.digits + string.ascii_letters
    chars = random.sample(chars, 4)
    print(chars)

    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    def rndChar(i):
        return chars[i]

    def rndColor2():
        return (random.randint(30, 120), random.randint(30, 120), random.randint(30, 120))

    height = 60
    width = 240
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf", 36)
    draw = ImageDraw.Draw(image)
    for i in range(width):
        for j in range(height):
            draw.point((i, j), fill=rndColor())

    for i in range(4):
        draw.text((60 * i + 10, 10), rndChar(i), font=font, fill=rndColor2())

    image = image.filter(ImageFilter.BLUR)
    image.save('./images/code.gif')
    # image.show()
    return chars


# 第1步，实例化object，建立窗口window


def main(frame):
    window = tk.Toplevel(frame)

    # 第2步，给窗口的可视化起名字
    window.title('文件存储系统V1.0')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('400x300+150+300')  # 这里的乘是小x

    # 第4步，加载 wellcome image
    canvas = tk.Canvas(window, width=500, height=140)

    image_file = tk.PhotoImage(file='./images/welcome.gif')

    canvas.create_image(200, 0, anchor='n', image=image_file)
    canvas.pack(side='top')
    tk.Label(window, text='Wellcome', font=('Arial', 16)).pack()
    window.iconbitmap('./images/tiicon.ico')
    # 第5步，用户信息
    tk.Label(window, text='Username:', font=('Arial', 14)).place(x=10, y=170)
    tk.Label(window, text='Password:', font=('Arial', 14)).place(x=10, y=210)

    # 第6步，用户登录输入框ntry
    # 用户名
    var_usr_name = tk.StringVar()
    # var_usr_name.set('admin')
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name.place(x=120, y=175)
    # 用户密码
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
    entry_usr_pwd.place(x=120, y=215)

    def openconfirmpage():
        window1 = tk.Toplevel(window)

        # 第2步，给窗口的可视化起名字
        window1.title('验证码')

        # 第3步，设定窗口的大小(长 * 宽)
        window1.geometry('400x300+750+300')  # 这里的乘是小x

        # 第4步，加载 wellcome image
        canvas = tk.Canvas(window1, width=500, height=140)
        chars = config_image_maker()
        image_file = tk.PhotoImage(file='./images/code.gif')

        canvas.create_image(200, 0, anchor='n', image=image_file)
        canvas.pack(side='top')
        tk.Label(window1, text='输入验证码(区分大小写)', font=('Arial', 16)).pack()
        window1.iconbitmap('./images/tiicon.ico')
        # 第5步，用户信息
        tk.Label(window1, text='验证码:', font=('Arial', 14)).place(x=10, y=170)
        var_usr_name = tk.StringVar()
        # var_usr_name.set('admin')
        entry = tk.Entry(window1, textvariable=var_usr_name, font=('Arial', 14))
        entry.place(x=120, y=175)

        def confirm():
            print(chars)
            gettemp = chars[0] + chars[1] + chars[2] + chars[3]
            print(entry.get())
            print('sss' + gettemp)
            if entry.get() == gettemp:
                window.destroy()
                window1.destroy()
                homepage1.main()

            else:
                tkinter.messagebox.showerror('错误', '验证码错误，请重试！')
                window.destroy()
                window1.destroy()
                config_image_maker()

        btn_sign_up = tk.Button(window1, text='提交', command=confirm)
        btn_sign_up.place(x=200, y=240)
        window1.mainloop()

    def connmysql(sql):
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               passwd='13503801568',
                               db='imagedb',
                               charset='utf8',
                               use_unicode=True,
                               cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        cursor = conn.cursor()
        # 注意使用Binary()函数来指定存储的是二进制
        try:
            cursor.execute(sql)
            # 提交，不然无法保存新建或者修改的数据
            conn.commit()
            print('Qurey OK!')
            data = cursor.fetchall()
            #print(data)
            return data
        except:
            print('ERROR!?')

        cursor.close()
        conn.close()

    def getmd5(pwd):
        m = hashlib.md5()
        m.update(pwd.encode(encoding='utf8'))
        pwd_md5 = m.hexdigest()
        return pwd_md5

    count = 0

    # 第8步，定义用户登录功能
    def usr_login():
        # 这两行代码就是获取用户输入的usr_name和usr_pwd
        usr_name = var_usr_name.get()
        usr_pwd = getmd5(var_usr_pwd.get())

        # 这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
        # 中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。
        # 如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗how are you? 加上你的用户名。
        def items(username):
            for i in usrs_info:
                if i['username'] == username:
                    return i

        sql = 'SElECT * FROM login WHERE username="{username}"'
        sql1 = sql.format(username=usr_name)
        usrs_info = connmysql(sql1)
        is_username = [i['username'] for i in usrs_info]
        if usr_name in is_username:
            if usr_pwd == usrs_info[0].get('password'):
                openconfirmpage()
                #tkinter.messagebox.showinfo(title='Welcome', message='Hello ' + usr_name)
                window.destroy()
                homepage1.main()
            # 如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
            if usr_pwd != usrs_info[0].get('password'):
                tkinter.messagebox.showerror(message='Sorry,your password error,you just have 3 chances!')
                nonlocal count
                count += 1
                print(count)
            if usrs_info != usrs_info[0].get('password') and count >= 3:
                tkinter.messagebox.showerror(message='拒绝访问！')
        else:  # 如果发现用户名不存在
            is_sign_up = tkinter.messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
            # 提示需不需要注册新用户
            if is_sign_up:
                usr_sign_up()

    # 第9步，定义用户注册功能
    def usr_sign_up():
        def sign_to_frame():
            # 以下三行就是获取我们注册时所输入的信息
            np = new_pwd.get()
            npf = new_pwd_confirm.get()
            nn = new_name.get()
            sql = 'SElECT * FROM login WHERE username="{username}"'
            sql1 = sql.format(username=nn)
            usrs_info = connmysql(sql1)
            is_username = [i['username'] for i in usrs_info]
            if np != npf:
                tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')

            # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
            elif nn in is_username:
                tkinter.messagebox.showerror('Error', 'The user has already signed up!')

            # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
            else:
                sql2 = "INSERT INTO login VALUES('{username}','{password}')"
                sql3 = sql2.format(username=nn, password=getmd5(npf))
                connmysql(sql3)
                tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
                # 然后销毁窗口。
                window_sign_up.destroy()

        # 定义长在窗口上的窗口
        window_sign_up = tk.Toplevel(window)
        window_sign_up.geometry('300x200')
        window_sign_up.title('Sign up window')

        new_name = tk.StringVar()  # 将输入的注册名赋值给变量
        # new_name.set('')  # 将最初显示定为'example@python.com'
        tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
        entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
        entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=130, y=50)

        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
        entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.place(x=130, y=90)

        # 下面的 sign_to_frame
        btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_frame)
        btn_comfirm_sign_up.place(x=180, y=120)

    # 第7步，login and sign up 按钮
    btn_login = tk.Button(window, text='Login', command=usr_login)
    btn_login.place(x=120, y=240)
    btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
    btn_sign_up.place(x=200, y=240)
    # 第10步，主窗口循环显示
    window.mainloop()


#if __name__ == '__main__':
    #main(0)
