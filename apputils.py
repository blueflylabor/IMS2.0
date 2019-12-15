import tkinter.messagebox
from time import ctime
from tkinter import ttk
from tkinter import *
from mysqlutils import *
from tkinter import filedialog

p1 = {'id': "1", 'name': 'YangGuoXu', 'contact': '13503801568', 'ip': '192.168.1.1'}

pc = getall()


def exist_id(_id_):
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
    sql = "SELECT * FROM info WHERE id=" + _id_ + ";"
    try:
        cursor.execute(sql)
        # 提交，不然无法保存新建或者修改的数据
        conn.commit()
        print('Qurey OK!')
        data = cursor.fetchall()
        # print(data)
        return data
    except:
        print('ERROR!?')

    cursor.close()
    conn.close()


'''添加模块'''


def addperson():
    # 定义长在窗口上的窗口
    addFrame = tk.Toplevel()
    addFrame.geometry('400x300+0+0')
    addFrame.title('注册窗口')
    addFrame.resizable(False, False)
    new_id = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(addFrame, text='帐号: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_id = tk.Entry(addFrame, textvariable=new_id)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_id.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(addFrame, text='姓名: ').place(x=10, y=50)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(addFrame, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=50)  # `entry`放置在坐标（150,10）.

    new_score = tk.StringVar()
    tk.Label(addFrame, text='联系方式: ').place(x=10, y=90)
    entry_usr_score = tk.Entry(addFrame, textvariable=new_score)
    entry_usr_score.place(x=130, y=90)

    new_ad = tk.StringVar()
    tk.Label(addFrame, text='域名地址: ').place(x=10, y=130)
    entry_usr_new_ad = tk.Entry(addFrame, textvariable=new_ad)
    entry_usr_new_ad.place(x=130, y=130)
    pc = getall()

    def add_frame():
        # 以下三行就是获取我们注册时所输入的信息
        nid = new_id.get()
        nname = new_name.get()
        ncontact = new_score.get()
        nip = new_ad.get()
        add_student(nid, nname, ncontact, nip, pc)
        print("add_model  %s" % ctime())
        addFrame.destroy()

    # 下面的 sign_to_frame
    btn_comfirm_add = tk.Button(addFrame, text='注册', command=add_frame)
    btn_comfirm_add.place(x=330, y=260)


def add_student(_id_, _name_, _contact_, _ip_, info):
    # stu_addtemp=stu1.copy()
    addtemp = p1.fromkeys(['id', 'name', 'contact', 'ip'])
    # 经调试发现漏洞，一旦误删示例p1（即操作删除示例数据），无法通过复制进行创建新的数据空间，故此处抛弃这种写法
    if len(exist_id(_id_)) is not 0:
        # print(len(exist_id(_id_)))
        tk.messagebox.showwarning('警告', '信息已存在')
    if _id_ is None:
        tk.messagebox.showerror('输入错误', '输入不能为空')
    if not _id_.isalnum():
        tk.messagebox.showerror('输入错误', '请输入一串数字')
    if len(_id_) > 12:
        tk.messagebox.showerror('输入错误', '输入数字长度非法')
    if not _name_.isalpha():
        tk.messagebox.showerror('输入错误', '非法输入')
    else:
        addtemp['id'] = _id_
        addtemp['name'] = _name_
        addtemp['contact'] = _contact_
        addtemp['ip'] = _ip_
        info.append(addtemp)
        insert(_id_, _name_, _contact_, _ip_)
        return info


'''删除模块'''

p1 = {'id': "1", 'name': 'YangGuoXu', 'contact': '13503801568', 'ip': '192.168.1.1'}

pc = getall()


# print('s')
# print(pc)


def delstu():
    delFrame = tk.Toplevel()
    delFrame.geometry('400x300+0+0')
    delFrame.title('删除窗口')
    delFrame.resizable(False, False)

    def delframe_confirm():
        is_id = [i['id'] for i in pc if i.get('id') == del_id.get()]
        # print(is_id)
        # print('*' * 30)
        # print(type(del_id.get()))
        if del_id.get() not in is_id:
            tk.messagebox.showerror('error', '学生不存在')
        else:
            conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='13503801568', db='imagedb',
                                   charset='utf8', use_unicode=True, cursorclass=pymysql.cursors.DictCursor)
            cursor = conn.cursor()
            # print(str() + '\n')
            sql = "DELETE FROM info WHERE id='{id}';"
            # print(sql.format(id=del_id.get()))
            cursor.execute(sql.format(id=del_id.get()))
            conn.commit()
            cursor.close()
            conn.close()
            tk.messagebox.showinfo('注意', '删除成功！')
            print("del_model  %s" % ctime())
            delFrame.destroy()

    del_id = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(delFrame, text='账号: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_del_id = tk.Entry(delFrame, textvariable=del_id)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_del_id.place(x=130, y=10)  # `entry`放置在坐标（150,10）.
    btn_confirm_delstu = tk.Button(delFrame, text='确定删除该学生', command=delframe_confirm)
    btn_confirm_delstu.place(x=260, y=260)
    pc = getall()


'''查询全部模块'''


def treeview1():
    pc = getall()
    Tuple = {'id': "1", 'name': 'YangGuoXu', 'contact': 99, 'ip': '192.168.1.1'}
    root = Tk()  # 初始框的声明
    columns = ('学号', "姓名", '联系方式', "IP地址")
    treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格
    treeview.column('学号', width=300, anchor='center')
    treeview.column("姓名", width=100, anchor='center')  # 表示列,不显示
    treeview.column('联系方式', width=100, anchor='center')
    treeview.column("IP地址", width=300, anchor='center')
    treeview.heading('学号', text='学号')
    treeview.heading("姓名", text="姓名")  # 显示表头
    treeview.heading('联系方式', text='联系方式')
    treeview.heading("IP地址", text="IP地址")
    treeview.pack(side=LEFT, fill=BOTH)
    id = [i['id'] for i in pc]
    name = [i['name'] for i in pc]
    concat = [i['contact'] for i in pc]
    ipcode = [i['ip'] for i in pc]
    data = [Tuple]
    for i in range(len(data)):
        id.append(data[i].get('stu_id'))
        name.append(data[i].get('stu_name'))
        concat.append(data[i].get('stu_score'))
        ipcode.append(data[i].get('stu_address'))
    for i in range(len(id) - 1):  # 写入数据
        treeview.insert('', i, values=(id[i], name[i], concat[i], ipcode[i]))
    # root.mainloop()  # 进入消息循环


# treeview()

def treeview(item):
    Tuple = {'id': "1", 'name': 'YangGuoXu', 'contact': 99, 'ip': '192.168.1.1'}
    root = Tk()  # 初始框的声明
    columns = ('学号', "姓名", '联系方式', "IP地址")
    treeview1 = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格
    treeview1.column('学号', width=300, anchor='center')
    treeview1.column("姓名", width=100, anchor='center')  # 表示列,不显示
    treeview1.column('联系方式', width=100, anchor='center')
    treeview1.column("IP地址", width=300, anchor='center')
    treeview1.heading('学号', text='学号')
    treeview1.heading("姓名", text="姓名")  # 显示表头
    treeview1.heading('联系方式', text='联系方式')
    treeview1.heading("IP地址", text="IP地址")
    treeview1.pack(side=LEFT, fill=BOTH)
    pc = [item]
    id = [i['id'] for i in pc]
    name = [i['name'] for i in pc]
    concat = [i['contact'] for i in pc]
    ipcode = [i['ip'] for i in pc]
    data = [Tuple]
    for i in range(len(data)):
        id.append(data[i].get('stu_id'))
        name.append(data[i].get('stu_name'))
        concat.append(data[i].get('stu_score'))
        ipcode.append(data[i].get('stu_address'))
    for i in range(len(id) - 1):  # 写入数据
        treeview1.insert('', i, values=(id[i], name[i], concat[i], ipcode[i]))
    # root.mainloop()  # 进入消息循环


# treeview()
'''修改模块'''

p1 = {'id': "1", 'name': 'YangGuoXu', 'contact': '13503801568', 'ip': '192.168.1.1'}

pc = getall()


def updateperson():
    # 定义长在窗口上的窗口
    updateFrame = tk.Toplevel()
    updateFrame.geometry('400x300+0+0')
    updateFrame.title('注册窗口')
    new_id = tk.StringVar()
    tk.Label(updateFrame, text='帐号: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    tk.Label(updateFrame, text='账号: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_del_id = tk.Entry(updateFrame, textvariable=new_id)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_del_id.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

    new_name = tk.StringVar()
    tk.Label(updateFrame, text='姓名: ').place(x=10, y=50)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(updateFrame, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=50)  # `entry`放置在坐标（150,10）.

    new_score = tk.StringVar()
    tk.Label(updateFrame, text='联系方式: ').place(x=10, y=90)
    entry_usr_score = tk.Entry(updateFrame, textvariable=new_score)
    entry_usr_score.place(x=130, y=90)

    new_ad = tk.StringVar()
    tk.Label(updateFrame, text='域名地址: ').place(x=10, y=130)
    entry_usr_new_ad = tk.Entry(updateFrame, textvariable=new_ad)
    entry_usr_new_ad.place(x=130, y=130)
    pc = getall()

    def update_frame():
        # 以下三行就是获取我们注册时所输入的信息
        nid = new_id.get()
        nname = new_name.get()
        ncontact = new_score.get()
        nip = new_ad.get()
        update_student(nid, nname, ncontact, nip)
        print('update_model  %s' % ctime())
        updateFrame.destroy()

    # 下面的 sign_to_frame
    btn_comfirm_add = tk.Button(updateFrame, text='注册', command=update_frame)
    btn_comfirm_add.place(x=330, y=260)


def update_student(_id_, _name_, _contact_, _ip_):
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = '13503801568'
    db = 'imagedb'
    charset = 'utf8'
    use_unicode = True
    sql2 = "UPDATE info SET name=%s,contact=%s,ip=%s WHERE id=%s;"
    is_id = [i['id'] for i in pc]
    data = [_name_, _contact_, _ip_, _id_]
    # print(data)
    if _id_ not in is_id:
        tk.messagebox.showwarning('输入错误', 'id不存在')
    if not _name_.isalpha():
        tk.messagebox.showwarning('输入错误', '非法输入')
    else:
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='13503801568', db='imagedb',
                               charset='utf8', use_unicode=True, cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        # print(str() + '\n')
        cursor.execute(sql2, data)
        conn.commit()
        cursor.close()
        conn.close()


'''查询单个模块'''
import pymysql
import tkinter as tk
import mysqlutils

p1 = {'id': "1", 'name': 'YangGuoXu', 'contact': '13503801568', 'ip': '192.168.1.1'}

pc = getall()


def serstu():
    serFrame = tk.Toplevel()
    serFrame.geometry('400x300+0+0')
    serFrame.title('查询窗口')
    serFrame.resizable(False, False)

    def return_items(id):
        pc = getall()
        for i in pc:
            if id == i['id']: return i

    def serframe_confirm():
        serid = ser_id.get()
        is_id = [i['id'] for i in pc]
        if serid not in is_id:
            tk.messagebox.showerror('error', '学生不存在')
        else:

            # sFrame = tk.Toplevel(serFrame)
            # sFrame.geometry('400x300')
            # sFrame.title('查询')
            # list_stu = tk.scrolledtext.ScrolledText(sFrame, font=('Arial', 12), width=50, height=5, bg='LightCyan')
            # list_stu.pack(side='right')
            # list_stu.insert(END, return_items(serid))
            print('search_single_model  %s' % ctime())
            treeview(return_items(serid))

    ser_id = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(serFrame, text='账号: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_del_id = tk.Entry(serFrame, textvariable=ser_id)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_del_id.place(x=130, y=10)  # `entry`放置在坐标（150,10）.
    btn_confirm_serstu = tk.Button(serFrame, text='查询', command=serframe_confirm)
    btn_confirm_serstu.place(x=260, y=260)


def choose_image_mission():
    window = tk.Tk()
    window.title('选择图像任务')
    window.geometry('400x400+0+0')
    value = 0
    var1 = tk.StringVar()
    l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
    l.pack()

    def print_selection():
        value = lb.get(lb.curselection())
        var1.set(value)

    b1 = tk.Button(window, text='print selection', width=15,
                   height=2, command=print_selection)
    b1.pack()

    var2 = tk.StringVar()
    lb = tk.Listbox(window, listvariable=var2)
    list_items = mysqlutils.table_list()
    list_items.remove('info')
    list_items.remove('login')
    list_items.remove('imager')
    list_items.remove('images')
    print(list_items)
    for item in list_items:
        lb.insert('end', item)
    lb.pack()

    def choose_model():
        window = tk.Tk()
        window.title('模式选择')
        window.geometry('400x400+0+0')
        b1 = tk.Button(window, text='上传图片', width=15,
                       height=2, command=insert_images)
        b1.pack()
        b2 = tk.Button(window, text='保存图片', width=15,
                       height=2, command=get_images)
        b2.pack()
        window.mainloop()

    def imagereader(id, ad):
        # 读取图片文件
        # blob最大只能存65K的文件

        # fp = open("test.jpg",'rb',encoding='utf-8')
        global cursor1
        fp = open(ad, 'rb')
        img = fp.read()
        fp.close()
        # 创建连接
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               passwd='13503801568',
                               db='imagedb',
                               charset='utf8')
        # 创建游标
        cursor = conn.cursor()
        # 注意使用Binary()函数来指定存储的是二进制
        # cursor.execute("INSERT INTO demo_pic_repo SET touxiang_data= %s" % pymysql.Binary(img))
        sql_get = "SELECT im FROM {tn} WHERE id='{id}'"
        sql_insert = "INSERT INTO {tn} VALUES  (%s,%s)"
        data = [id, img]
        data1 = [value, id]
        cursor.execute(sql_get.format(tn=value, id=id))
        conn.commit()
        get = cursor.fetchall()
        # print(len(get))
        if len(get) is 0:
            try:
                if id is None:
                    tk.messagebox.showerror('错误', '未输入账户！')
                else:
                    cursor1 = conn.cursor()
                    # cursor.execute(sql,datatemp)
                    cursor1.execute(sql_insert.format(tn=value), data)
                    # 提交，不然无法保存新建或者修改的数据
                    conn.commit()
                    print('query ok!')
            except:
                cursor1.close()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()

    def insert_images():
        def open_file():
            selectFile = tk.filedialog.askopenfilename(title='Select the diagnostic instrument  file',
                                                       initialdir='C:\\Windows')  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
            entry1.insert(0, selectFile)

        def upload_file():
            if not entry2.get().isalnum() and entry2.get() is None:
                tk.messagebox.showerror('错误', '未选择上传账户！')
            if entry1.get() is None:
                tk.messagebox.showerror('错误', '未选择图片！')
            else:
                imagereader(entry2.get(), entry1.get())
                root.destroy()

        root = tk.Toplevel()
        root.geometry('500x200+700+300')
        frm = tk.Frame(root)
        frm.grid(padx='20', pady='30')
        btn = tk.Button(frm, text='打开文件', command=open_file)
        btn.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
        btn_confi = tk.Button(frm, text='上传', command=upload_file)
        btn_confi.grid(row=1, column=2, ipadx='3', ipady='3', padx='10', pady='20')
        entry1 = tk.Entry(frm, width='40', )
        entry1.grid(row=0, column=1)
        label_id = tk.Label(frm, width='10', text='账户')
        label_id.grid(row=1, column=0)
        entry2 = tk.Entry(frm, width='10', )
        entry2.grid(row=1, column=1)
        root.mainloop()

    def downloadimager(ad, id):
        # 读取图片文件
        # blob最大只能存65K的文件

        # 创建连接
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               passwd='13503801568',
                               db='imagedb',
                               charset='utf8',
                               )
        # 创建游标
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        # 注意使用Binary()函数来指定存储的是二进制
        # cursor.execute("INSERT INTO demo_pic_repo SET touxiang_data= %s" % pymysql.Binary(img))
        sql_get = "SELECT im FROM {tn} WHERE id='{id}' "
        sql_count = "SELECT id FROM {tn} WHERE id='{id}'"
        cursor1.execute(sql_count.format(tn=value, id=id))
        cursor.execute(sql_get.format(tn=value, id=id))
        print(cursor1.fetchone())
        tag = (0,)
        if tag is cursor1.fetchone():
            tk.messagebox.showerror('错误', '无该图像')
        else:
            try:
                get = cursor.fetchall()[0][0]
                print(get)
                print(type(get))
                fp = open(ad + '/save.png', 'wb')
                fp.write(get)
                fp.close()
            except IOError:
                print('失败')
            if ad is None:
                tk.messagebox.showerror('错误', '请先选择保存地址！')


        # 关闭游标
        cursor.close()
        cursor1.close()
        # 关闭连接
        conn.close()

    def get_images():
        def open_file_ad():
            selectfoloder = tk.filedialog.askdirectory(title='Select the diagnostic instrument  file',
                                                       initialdir='C:\\Windows')
            '''selectFile = tk.filedialog.askopenfilename()
    '''  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
            entry1.insert(0, selectfoloder)

        def upload_file():
            if not entry2.get().isalnum() and entry2.get() is None:
                tk.messagebox.showerror('错误', '未选择下载账户！')
            if entry1.get() is None:
                tk.messagebox.showerror('错误', '未选择保存位置！')
            else:
                downloadimager(entry1.get(), entry2.get())
                root.destroy()

        root = tk.Toplevel()
        root.geometry('500x200+700+300')
        frm = tk.Frame(root)
        frm.grid(padx='20', pady='30')
        btn = tk.Button(frm, text='打开保存地址', command=open_file_ad)
        btn.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
        btn_confi = tk.Button(frm, text='保存', command=upload_file)
        btn_confi.grid(row=1, column=2, ipadx='3', ipady='3', padx='10', pady='20')
        entry1 = tk.Entry(frm, width='40', )
        entry1.grid(row=0, column=1)
        label_id = tk.Label(frm, width='10', text='账户')
        label_id.grid(row=1, column=0)
        entry2 = tk.Entry(frm, width='10', )
        entry2.grid(row=1, column=1)
        root.mainloop()

    def choose():
        nonlocal value
        value = lb.get(lb.curselection())
        choose_model()

    btn_comfirm_add = tk.Button(window, text='打开', command=choose)
    btn_comfirm_add.place(x=330, y=260)
    window.mainloop()


def create_image_mission():
    # 定义长在窗口上的窗口
    frame = tk.Toplevel()
    frame.geometry('400x300+0+0')
    frame.title('创建图片任务')
    new_mission = tk.StringVar()
    tk.Label(frame, text='任务名: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry = tk.Entry(frame, textvariable=new_mission)  # 创建一个注册名的`entry`，变量为`new_name`
    entry.place(x=130, y=10)  # `entry`放置在坐标（150,10）

    def create_missiontable(missionname):
        sql_create = "CREATE TABLE {0} (id varchar(12) PRIMARY KEY," \
                     "im mediumblob," \
                     "constraint fk FOREIGN KEY (id) " \
                     "references info(id) on delete cascade on update cascade);"
        if missionname is None:
            tk.messagebox.showwarning('错误', '未输入任务名')
        else:
            conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='13503801568', db='imagedb',
                                   charset='utf8', use_unicode=True, cursorclass=pymysql.cursors.DictCursor)
            cursor = conn.cursor()
            cursor.execute(sql_create.format(missionname))
            conn.commit()
            cursor.close()
            conn.close()

    def create():
        # 以下三行就是获取我们注册时所输入的信息
        nmission = new_mission.get()
        temp = mysqlutils.table_exists(nmission)
        if temp is 1:
            tk.messagebox.showwarning('警告', '该任务对象已创建！')
        if temp is 0:
            create_missiontable(nmission)
            frame.destroy()

    # 下面的 sign_to_frame
    btn_comfirm_add = tk.Button(frame, text='注册', command=create)
    btn_comfirm_add.place(x=330, y=260)
    frame.mainloop()


#choose_image_mission()
