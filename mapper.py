import pandas as pd
import entity
import constant
from utils import id_util as iu


def vault_time_mapper(file_path,date):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='明细')
    index = 0
    vault_time_list = []
    df = df.loc[df['审批人地域'] == '苏州']
    arr = df.to_dict(orient='records')
    for data in arr:
        vault_time = entity.VaultTime(id=iu.generate_id(ct.busi_id_list[0],date,index+1),
                                      app_name=data['审批人姓名'],
                                      app_id=data['审批人账号'],
                                      app_path=data['审批人组织路径'],
                                      op1_name=data['操作人1姓名'],
                                      op1_p_id=data['操作人1主帐号'],
                                      op1_path=data['操作人1组织路径'],
                                      op1_s_id=data['操作人1从帐号'],
                                      app1=data['审批方式1'],
                                      app1_time=data['审批时间1'],
                                      op2_name=data['操作人2姓名'],
                                      op2_p_id=data['操作人2主帐号'],
                                      op2_path=data['操作人2组织路径'],
                                      op2_s_id=data['操作人2从帐号'],
                                      app2=data['审批方式2'],
                                      app2_time=data['审批时间2'],
                                      flag=data['两个操作人是否同一组织'])
        index += 1
        vault_time_list.append(vault_time)
    return vault_time_list

def vault_reason_mapper(file_path,date):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='明细')
    index = 0
    vault_reason_list = []
    df = df.loc[df['审批人地域'] == '苏州']
    arr = df.to_dict(orient='records')
    for data in arr:
        vault_reason = entity.VaultReason(id=iu.generate_id(ct.busi_id_list[1],date,index+1),
                                          op_name=str(data['操作人姓名']),
                                          op_id=str(data['操作人账号']),
                                          op_tele=str(data['操作人手机号']),
                                          op_org=str(data['操作人组织']),
                                          op_path=str(data['操作人组织路径']),
                                          reason=str(data['金库申请原因']),
                                          op_time=str(data['申请时间']),
                                          app_name=str(data['审批人姓名']),
                                          app_id=str(data['审批人账号']),
                                          app_tele=str(data['审核人手机号']),
                                          app_org=str(data['审批人组织']),
                                          app_path=str(data['审批人组织路径']),
                                          app_time=str(data['审批时间']))
        index += 1
        vault_reason_list.append(vault_reason)
    return vault_reason_list

def bes_pljk_mapper(file_path,date):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='Sheet1')
    index = 0
    bes_pljk_list = []
    arr = df.to_dict(orient='records')
    for data in arr:
        bes_pljk = entity.BesPljk(id=iu.generate_id(ct.busi_id_list[2],date,index+1),
                                  staff_id=str(data['人员ID']),
                                  username=str(data['账号名']),
                                  zh_name=str(data['中文名']),
                                  id_state=str(data['从账号状态']),
                                  org_path=str(data['组织机构树']),
                                  org=str(data['组织机构']),
                                  type=str(data['类型']),
                                  zh_type=str(data['中文类型']),
                                  query_cnt=str(data['查询次数']),
                                  time=str(data['查询次数']))
        index += 1
        bes_pljk_list.append(bes_pljk)
    return bes_pljk_list

def bes_ycsj_mapper(file_path,date):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='Sheet1')
    index = 0
    bes_ycsj_list = []
    arr = df.to_dict(orient='records')
    for data in arr:
        bes_ycsj = entity.BesYcsj(
            id=iu.generate_id(ct.busi_id_list[3],date,index+1),
            staff_id=str(data['人员ID']),
            username=str(data['账号名']),
            id_state=str(data['账号状态']),
            zh_name=str(data['中文名']),
            org_path=str(data['组织机构树']),
            org=str(data['组织机构']),
            time=str(data['统计时间']),
            op_cnt=str(data['异常时间操作业务统计']),
            op_sum=str(data['全天办理业务统计']),
            per=str(data['百分比']))
        index += 1
        bes_ycsj_list.append(bes_ycsj)
    return bes_ycsj_list

def bes_dsj_mapper(file_path,date):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='Sheet1')
    index = 0
    bes_dsj_list = []
    arr = df.to_dict(orient='records')
    for data in arr:
        bes_dsj = entity.BesDsj(
            id=iu.generate_id(ct.busi_id_list[4],date,index+1),
            staff_id=str(data['人员ID']),
            username=str(data['主账号']),
            id_state=str(data['账号状态']),
            zh_name=str(data['中文姓名']),
            org_path=str(data['组织机构树']),
            org=str(data['组织机构']),
            type=str(data['类型']),
            zh_type=str(data['中文类型']),
            time=str(data['统计时间']),
            cnt=str(data['次数']))
        index += 1
        bes_dsj_list.append(bes_dsj)
    return bes_dsj_list

def bes_sum_mapper(file_path,date):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='汇总')
    index = 0
    bes_sum_list = []
    arr = df.to_dict(orient='records')
    for data in arr:
        bes_sum = entity.BesSum(
            id=iu.generate_id(ct.busi_id_list[5],date,index+1),
            staff_id=str(data['人员ID']),
            username=str(data['主账号']),
            id_state=str(data['账号状态']),
            zh_name=str(data['中文名']),
            org_path=str(data['组织机构树']),
            org=str(data['组织机构']),
            time=str(data['统计时间']),
            cnt=str(data['次数']))
        index += 1
        bes_sum_list.append(bes_sum)
    return bes_sum_list

def pw_detect_detail_mapper(file_path,date):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='明细')
    index = 0
    pw_detect_detail_list = []
    df = df.loc[df['地市'] == '苏州']
    arr = df.to_dict(orient='records')
    for data in arr:
        pw_detect_detail = entity.PwDetectDetail(
            id=iu.generate_id(ct.busi_id_list[6], date, index+1),
            db=str(data['数据库']),
            staff_id=str(data['操作员工号']),
            staff_name=str(data['操作员姓名']),
            org=str(data['组织机构']),
            mobile=str(data['探测手机号']),
            ip=str(data['IP地址']),
            op_time=str(data['操作时间']),
            pw=str(data['探测错误密码']),
            cydl=str(data['是否为常用登录IP']),
            dcn=str(data['是否在DCN网络归属段']),
            fhtz=str(data['是否符合探测密码特征']),
            interval=str(data['相邻两次操作间隔_分钟']),
            op_cnt=str(data['20min内操作次数']),
            repeat_per=str(data['重复密码率']),
            remark=str(data['备注']))
        index += 1
        pw_detect_detail_list.append(pw_detect_detail)
    return pw_detect_detail_list

def pw_detect_sum_mapper(file_path,date):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path, sheet_name='明细数据')
    df = pd.DataFrame(data=df.values[1:], columns=df.values[0])
    df = df.loc[df['地市'] == '苏州']
    index = 0
    pw_detect_sum_list = []
    arr = df.to_dict(orient='records')
    for data in arr:
        pw_detect_sum = entity.PwDetectSum(
            id=iu.generate_id(ct.busi_id_list[7], date, index + 1),
            org=str(data['营业厅']),
            staff_id=str(data['营业员工号']),
            staff_name=str(data['营业员姓名']),
            op_time=str(data['探测日期']),
            op_cnt=str(data['探测次数']),
            number_cnt=str(data['号码数']),
            remark=str(data['备注']))
        index += 1
        pw_detect_sum_list.append(pw_detect_sum)
    return pw_detect_sum_list

def order_query_mapper(file_path,date):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='明细')
    index = 0
    order_query_list = []
    df = df.loc[df['地市'] == '苏州']
    arr = df.to_dict(orient='records')
    for data in arr:
        order_query = entity.OrderQuery(
            id=iu.generate_id(ct.busi_id_list[8], date, index+1),
            op_time=str(data['操作时间']),
            staff_id=str(data['操作人员工号']),
            username=str(data['账号名']),
            zh_name=str(data['中文名']),
            op_path=str(data['操作员组织机构树']),
            op_org=str(data['操作员组织机构']),
            op_res=str(data['操作结果']),
            start_time=str(data['查询开始时间']),
            end_time=str(data['查询结束时间']),
            ob_id=str(data['操作对象ID']),
            order_type=str(data['清单类型']),
            telephone=str(data['手机号']))
        index += 1
        order_query_list.append(order_query)
    return order_query_list

def sst_query_mapper(file_path,date):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='SQL Results')
    index = 0
    sst_query_list = []
    arr = df.to_dict(orient='records')
    for data in arr:
        sst_query = entity.SstQuery(
            id=iu.generate_id(ct.busi_id_list[9], date, index+1),
            oper_time=str(data['OPER_TIME']),
            telephone=str(data['手机号']),
            staff_id=str(data['操作人员工号']),
            zh_name=str(data['账号名']),
            org=str(data['机构']),
            op_time=str(data['查询时间'])
            )
        index += 1
        sst_query_list.append(sst_query)
    return sst_query_list
