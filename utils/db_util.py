import cx_Oracle

def db_connect():
    user = 'ydzw'
    password = 'YDzwi769hja6'
    host = '10.33.222.38:30022'
    service_name = 'psz'
    conn_str = f"{user}/{password}@{host}/{service_name}"
    connect = cx_Oracle.connect(conn_str)
    return connect

connect = db_connect()
cursor = connect.cursor()
cursor.execute('insert into qdyy_data.JH_BUSI_INFO@szyy3 (id,groupid,column1) values (1,1,1)')
connect.commit()

# print(cursor.fetchone())