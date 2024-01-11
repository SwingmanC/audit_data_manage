import pandas as pd
import entity
import constant
import id_util as iu

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
        # vault_time.id = iu.generate_id(ct.busi_id_list[0],date,index+1)
        # vault_time.app_name = data['审批人姓名']
        # vault_time.app_id = data['审批人账号']
        # vault_time.app_path = data['审批人组织路径']
        # vault_time.op1_name = data['操作人1姓名']
        # vault_time.op1_p_id = data['操作人1主帐号']
        # vault_time.op1_path = data['操作人1组织路径']
        # vault_time.op1_s_id = data['操作人1从帐号']
        # vault_time.app1 = data['审批方式1']
        # vault_time.app1_time = data['审批时间1']
        # vault_time.op2_name = data['操作人2姓名']
        # vault_time.op2_p_id = data['操作人2主帐号']
        # vault_time.op2_path = data['操作人2组织路径']
        # vault_time.op2_s_id = data['操作人2从帐号']
        # vault_time.app2 = data['审批方式2']
        # vault_time.app2_time = data['审批时间2']
        # vault_time.flag = data['两个操作人是否同一组织']
        vault_time.busi_id = ct.busi_id_list[0]
        vault_time.rule_id = ct.rule_id_list[0]
        vault_time_list.append(vault_time)
    return vault_time_list

list = vault_time_mapper('D:/安全审计/202312/202312/1、金库/金库短时间地市12月份汇总.xlsx','202312')
print(list[0].id)

# def vault_reason_mapper():
#
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
