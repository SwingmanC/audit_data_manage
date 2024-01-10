import cx_Oracle

user = 'ydzw'
password = 'YDzwi769hja6'
host = '10.33.222.38:30022'
service_name = 'psz'
conn_str = f"{user}/{password}@{host}/{service_name}"
connect = cx_Oracle.connect(conn_str)
cursor = connect.cursor()
cursor.execute(
    'select * from qdyy_data.jh_busi_info@szyy3 where recorgid = 11177671 limit 1')
msisdn_list = cursor.fetchall()

print(msisdn_list)