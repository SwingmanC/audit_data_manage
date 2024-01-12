import pandas as pd
import entity
import constant
from utils import id_util as iu


def vault_time_mapper(file_path,exec_date,month):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='明细')
    index = 0
    vault_time_list = []
    df = df.loc[df['审批人地域'] == '苏州']
    arr = df.to_dict(orient='records')
    for data in arr:
        vault_time = entity.VaultTime(id=iu.generate_id(ct.busi_id_list[0],month,index+1),
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
        vault_time.exec_date = exec_date
        vault_time_list.append(vault_time)
    return vault_time_list

def vault_reason_mapper(file_path,exec_date,month):
    ct = constant.AuditConstant()
    df = pd.read_excel(file_path,sheet_name='明细')
    index = 0
    vault_reason_list = []
    df = df.loc[df['审批人地域'] == '苏州']
    arr = df.to_dict(orient='records')
    for data in arr:
        vault_reason = entity.VaultReason(id=iu.generate_id(ct.busi_id_list[1],month,index+1),
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
        vault_reason.exec_date = exec_date
        vault_reason_list.append(vault_reason)
    return vault_reason_list

# def bes_pljk_mapper():
#
# def bes_ycsj_mapper():
#
# def bes_dsj_mapper():
#
# def bes_sum_mapper():
#
# def pw_detect_detail_mapper():
#
# def pw_detect_item_mapper():
#
# def order_query_item_mapper():
#
# def sst_query_item_mapper():

