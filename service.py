import mapper
import datetime

from utils.db_util import db_connect

place_list = ['常熟', '吴江', '太仓', '张家港', '昆山', '姑苏', '相城', '吴中', '新区', '园区']


def is_county(org):
    for place in place_list:
        if org.find(place) != -1:
            return True
    return False

# def upload_vault_time(db_connect,file_path,exec_date,month):
# vault_time_list = mapper.vault_time_mapper(file_path,exec_date,month)
# cursor = db_connect.cursor()
# for vault_time in vault_time_list:
#     flag = is_county(vault_time.app_path)
#     if flag:
#         cursor.execute('select orgaid from renlh_4a_crm where staffid = %s and staffstatus =\'正常\'' %(vault_time.app_id))
#         recorg_id_list = cursor.fetchall()
#         if len(recorg_id_list) > 0:
#             org_id = recorg_id_list[0][0]
#             cursor.execute(
#             'insert into qdyy_data.JH_BUSI_INFO@szyy3 '
#             '(id, groupid, region_id, busi_id, rule_id, exec_date, recorgid, recopid, recdate,'
#             'oid, formnum, servnumber, COLUMN1, show_id, recdefid, einvoice_flag, orderid, cd_flag, recopname)')

def upload_vault_reason(db_connect, file_path, date):
    vault_reason_list = mapper.vault_reason_mapper(file_path, date)
    cursor = db_connect.cursor()
    for item in vault_reason_list:
        flag = is_county(item.app_path)
        if flag:
            cursor.execute(
                'select staffid,orgaid from renlh_4a_crm where telno = %s and staffstatus =\'正常\'' % (item.op_tele))
            recorg_id_list = cursor.fetchall()
            if len(recorg_id_list) > 0:
                print(item.op_tele)
                staff_id = recorg_id_list[0][0]
                org_id = recorg_id_list[0][1]
                rec_date = datetime.datetime.now()
                cursor.execute('insert into qdyy_data.JH_BUSI_INFO@szyy3 '
                               '(id, GROUPID, REGION_ID, BUSI_ID, RULE_ID, RECORGID, RECOPID, RECDATE, '
                               'SERVNUMBER, COLUMN1, COLUMN2, COLUMN3, COLUMN4, COLUMN5, COLUMN6, COLUMN7, COLUMN8, COLUMN9, COLUMN10, COLUMN11, '
                               'SHOW_ID,einvoice_flag,cd_flag,recopname)'
                               'values '
                               '(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24)'
                               , (int(item.id), item.group_id, item.region_id, item.busi_id, item.rule_id, org_id, str(staff_id),rec_date,
                                  item.op_tele, item.op_id, item.op_org, item.op_path, item.reason, item.op_time, item.app_name,item.app_id, item.app_tele,item.app_org,item.app_path, item.app_time,
                                  item.show_id, 0, 1, item.op_name))
    db_connect.commit()

def upload_bes_pljk(db_connect, file_path, date):
    bes_pljk_list = mapper.bes_pljk_mapper(file_path, date)
    cursor = db_connect.cursor()
    for item in bes_pljk_list:
        flag = is_county(item.org_path)
        if flag:
            cursor.execute(
                'select orgaid from renlh_4a_crm where staffid = %s and staffstatus =\'正常\'' % (item.staff_id))
            recorg_id_list = cursor.fetchall()
            if len(recorg_id_list) > 0:
                org_id = recorg_id_list[0][0]
                rec_date = datetime.datetime.now()
                cursor.execute('insert into qdyy_data.JH_BUSI_INFO@szyy3 '
                               '(id, GROUPID, REGION_ID, BUSI_ID, RULE_ID, RECORGID, RECOPID, RECDATE, '
                               'COLUMN1, COLUMN2, COLUMN3, COLUMN4, COLUMN5,COLUMN6'
                               'SHOW_ID,RECDEFID,einvoice_flag,cd_flag,recopname)'
                               'values '
                               '(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19)'
                               , (int(item.id), item.group_id, item.region_id, item.busi_id, item.rule_id, org_id, item.staff_id, rec_date,
                                  item.username, item.id_state,item.org_path,item.org,item.zh_type,item.query_cnt,
                                  item.show_id, item.type, 0, 1, item.zh_name))
    db_connect.commit()

def upload_bes_ycsj(db_connect, file_path, date):
    bes_ycsj_list = mapper.bes_ycsj_mapper(file_path, date)
    cursor = db_connect.cursor()
    for item in bes_ycsj_list:
        flag = is_county(item.org_path)
        if flag:
            cursor.execute(
                'select orgaid from renlh_4a_crm where staffid = %s and staffstatus =\'正常\'' % (item.staff_id))
            recorg_id_list = cursor.fetchall()
            if len(recorg_id_list) > 0:
                org_id = recorg_id_list[0][0]
                rec_date = datetime.datetime.now()
                cursor.execute('insert into qdyy_data.JH_BUSI_INFO@szyy3 '
                               '(id, GROUPID, REGION_ID, BUSI_ID, RULE_ID, RECORGID, RECOPID, RECDATE, '
                               'COLUMN1, COLUMN2, COLUMN3, COLUMN4, COLUMN5,COLUMN6,COLUMN7, COLUMN8'
                               'SHOW_ID,einvoice_flag,cd_flag,recopname)'
                               'values '
                               '(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20)'
                               , (int(item.id), item.group_id, item.region_id, item.busi_id, item.rule_id, org_id, item.staff_id, rec_date,
                                  item.username, item.id_state,item.org_path, item.org, item.time, item.op_cnt, item.op_sum, item.per,
                                  item.show_id, 0, 1, item.zh_name))
    db_connect.commit()

def upload_bes_dsj(db_connect, file_path, date):
    bes_dsj_list = mapper.bes_dsj_mapper(file_path, date)
    cursor = db_connect.cursor()
    for item in bes_dsj_list:
        flag = is_county(item.org_path)
        if flag:
            cursor.execute(
                'select orgaid from renlh_4a_crm where staffid = %s and staffstatus =\'正常\'' % (item.staff_id))
            recorg_id_list = cursor.fetchall()
            if len(recorg_id_list) > 0:
                org_id = recorg_id_list[0][0]
                rec_date = datetime.datetime.now()
                cursor.execute('insert into qdyy_data.JH_BUSI_INFO@szyy3 '
                               '(id, GROUPID, REGION_ID, BUSI_ID, RULE_ID, RECORGID, RECOPID, RECDATE, '
                               'COLUMN1, COLUMN2, COLUMN3, COLUMN4, COLUMN5, COLUMN6, COLUMN7'
                               'SHOW_ID,RECDEFID,einvoice_flag,cd_flag,recopname)'
                               'values '
                               '(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20)'
                               , (int(item.id), item.group_id, item.region_id, item.busi_id, item.rule_id, org_id, item.staff_id, rec_date,
                                  item.username, item.id_state,item.org_path,item.org,item.zh_type,item.time,item.cnt,
                                  item.show_id, item.type, 0, 1, item.zh_name))
    db_connect.commit()

def upload_bes_sum(db_connect, file_path, date):
    bes_sum_list = mapper.bes_sum_mapper(file_path, date)
    cursor = db_connect.cursor()
    for item in bes_sum_list:
        flag = is_county(item.org_path)
        if flag:
            cursor.execute(
                'select orgaid from renlh_4a_crm where staffid = %s and staffstatus =\'正常\'' % (item.staff_id))
            recorg_id_list = cursor.fetchall()
            if len(recorg_id_list) > 0:
                org_id = recorg_id_list[0][0]
                rec_date = datetime.datetime.now()
                cursor.execute('insert into qdyy_data.JH_BUSI_INFO@szyy3 '
                               '(id, GROUPID, REGION_ID, BUSI_ID, RULE_ID, RECORGID, RECOPID, RECDATE, '
                               'COLUMN1, COLUMN2, COLUMN3, COLUMN4, COLUMN5, COLUMN6'
                               'SHOW_ID,einvoice_flag,cd_flag,recopname)'
                               'values '
                               '(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18)'
                               , (int(item.id), item.group_id, item.region_id, item.busi_id, item.rule_id, org_id, item.staff_id, rec_date,
                                  item.username, item.id_state,item.org_path, item.org, item.time, item.cnt,
                                  item.show_id, 0, 1, item.zh_name))
    db_connect.commit()

def upload_pw_detect_detail(db_connect, file_path, date):
    pw_detect_detail_list = mapper.pw_detect_detail_mapper(file_path, date)
    cursor = db_connect.cursor()
    for item in pw_detect_detail_list:
        flag = is_county(item.org)
        if flag:
            cursor.execute(
                'select orgaid from renlh_4a_crm where staffid = %s and staffstatus =\'正常\'' % (item.staff_id))
            recorg_id_list = cursor.fetchall()
            if len(recorg_id_list) > 0:
                org_id = recorg_id_list[0][0]
                rec_date = datetime.datetime.now()
                cursor.execute('insert into qdyy_data.JH_BUSI_INFO@szyy3 '
                               '(id, GROUPID, REGION_ID, BUSI_ID, RULE_ID, RECORGID, RECOPID, RECDATE, '
                               'COLUMN1, COLUMN2, COLUMN3, COLUMN4, COLUMN5, COLUMN6, COLUMN7, COLUMN8, COLUMN9, COLUMN10, COLUMN11, COLUMN12, COLUMN13, '
                               'SHOW_ID,einvoice_flag,cd_flag,recopname)'
                               'values '
                               '(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25)'
                               , (int(item.id), item.group_id, item.region_id, item.busi_id, item.rule_id, org_id, item.staff_id, rec_date,
                                  item.db, item.org, item.mobile, item.ip, item.op_time, item.pw, item.cydl, item.dcn, item.fhtz, item.interval, item.op_cnt, item.repeat_per, item.remark,
                                  item.show_id, 0, 1, item.staff_name))
    db_connect.commit()

def upload_pw_detect_sum(db_connect, file_path, date):
    pw_detect_sum_list = mapper.pw_detect_sum_mapper(file_path, date)
    cursor = db_connect.cursor()
    for item in pw_detect_sum_list:
        cursor.execute(
            'select orgaid from renlh_4a_crm where staffid = %s and staffstatus =\'正常\'' % (item.staff_id))
        recorg_id_list = cursor.fetchall()
        if len(recorg_id_list) > 0:
            org_id = recorg_id_list[0][0]
            rec_date = datetime.datetime.now()
            cursor.execute('insert into qdyy_data.JH_BUSI_INFO@szyy3 '
                           '(id, GROUPID, REGION_ID, BUSI_ID, RULE_ID, RECORGID, RECOPID, RECDATE, '
                           'COLUMN1, COLUMN2, COLUMN3, COLUMN4, COLUMN5, '
                           'SHOW_ID,einvoice_flag,cd_flag,recopname)'
                           'values '
                           '(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17)'
                           ,(int(item.id), item.group_id, item.region_id, item.busi_id, item.rule_id, org_id, item.staff_id, rec_date,
                              item.org, item.op_time, item.op_cnt, item.number_cnt, item.remark,
                              item.show_id, 0, 1, item.staff_name))
    db_connect.commit()

def upload_order_query(db_connect, file_path, date):
    order_query_list = mapper.order_query_mapper(file_path, date)
    cursor = db_connect.cursor()
    for item in order_query_list:
        flag = is_county(item.org_path)
        if flag:
            cursor.execute(
                'select orgaid from renlh_4a_crm where staffid = %s and staffstatus =\'正常\'' % (item.staff_id))
            recorg_id_list = cursor.fetchall()
            if len(recorg_id_list) > 0:
                org_id = recorg_id_list[0][0]
                rec_date = datetime.datetime.now()
                cursor.execute('insert into qdyy_data.JH_BUSI_INFO@szyy3 '
                               '(id, GROUPID, REGION_ID, BUSI_ID, RULE_ID, RECORGID, RECOPID, RECDATE, '
                               'COLUMN1, COLUMN2, COLUMN3, COLUMN4, COLUMN5,COLUMN6,COLUMN7, COLUMN8, COLUMN9,'
                               'SHOW_ID,RECDEFID,einvoice_flag,cd_flag,recopname)'
                               'values '
                               '(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23)'
                               ,(int(item.id), item.group_id, item.region_id, item.busi_id, item.rule_id, org_id, item.staff_id, rec_date,
                                  item.op_time, item.username, item.op_path,item.op_org,item.op_res,item.start_time, item.end_time, item.ob_id, item.telephone,
                                  item.show_id, item.order_type, 0, 1, item.zh_name))
    db_connect.commit()

def upload_sst_query(db_connect, file_path, date):
    sst_query_list = mapper.sst_query_mapper(file_path, date)
    cursor = db_connect.cursor()
    for item in sst_query_list:
        flag = is_county(item.org)
        if flag:
            cursor.execute(
                'select orgaid from renlh_4a_crm where staffid = %s and staffstatus =\'正常\'' % (item.staff_id))
            recorg_id_list = cursor.fetchall()
            if len(recorg_id_list) > 0:
                org_id = recorg_id_list[0][0]
                rec_date = datetime.datetime.now()
                cursor.execute('insert into qdyy_data.JH_BUSI_INFO@szyy3 '
                               '(id, GROUPID, REGION_ID, BUSI_ID, RULE_ID, RECORGID, RECOPID, RECDATE, '
                               'COLUMN1, COLUMN2, COLUMN3, COLUMN4, '
                               'SHOW_ID,einvoice_flag,cd_flag,recopname)'
                               'values '
                               '(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16)'
                               , (int(item.id), item.group_id, item.region_id, item.busi_id, item.rule_id, org_id, item.staff_id, rec_date,
                                  item.oper_time, item.telephone, item.org, item.op_time,
                                  item.show_id, 0, 1, item.zh_name))
    db_connect.commit()


# upload_vault_reason(db_connect=connect,
#                     file_path='D:/安全审计/202312/202312/1、金库/金库前台异常申请理由12月份汇总.xlsx',
#                     exec_date='20240112', month='202312')



