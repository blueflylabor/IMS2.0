import re

import pymysql


def getall():
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
    sql = "SELECT * FROM info ;"
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


def insert(_id_, _name_, _contact_, _ip_):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='13503801568',
        database='imagedb',
        charset='utf8'
    )
    # 获取一个光标
    cursor = conn.cursor()
    sql2 = "INSERT INTO info VALUES (%s,%s,%s,%s);"
    data = [(_id_, _name_, _contact_, _ip_)]  #
    cursor.executemany(sql2, data)
    conn.commit()
    cursor.close()
    conn.close()


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
        print(data)
        return data
    except:
        print('ERROR!?')

    cursor.close()
    conn.close()


def table_exists(table_name):
    connect = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='13503801568',
        db='imagedb',
        charset='utf8',
        use_unicode=True
    )
    con = connect.cursor()
    sql = "show tables;"
    con.execute(sql)
    tables = [con.fetchall()]
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        return 1
    else:
        return 0
    con.close()
    connect.close()


def table_list():
    connect = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='13503801568',
        db='imagedb',
        charset='utf8',
        use_unicode=True
    )
    con = connect.cursor()
    sql = "show tables;"
    con.execute(sql)
    tables = [con.fetchall()]
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    return table_list
    con.close()
    connect.close()
