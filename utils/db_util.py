import cx_Oracle

def db_connect():
    user = 'ydzw'
    password = 'YDzwi769hja6'
    host = '10.33.222.38:30022'
    service_name = 'psz'
    conn_str = f"{user}/{password}@{host}/{service_name}"
    connect = cx_Oracle.connect(conn_str)
    return connect
