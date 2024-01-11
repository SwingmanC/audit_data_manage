class JhBusi:
    def __init__(self,id):
        self.id = id

class VaultTime:
    group_id = 1
    region_id = 11
    def __init__(self,id,app_name,app_id,app_path,op1_name,op1_p_id,op1_path,op1_s_id,
                 app1,app1_time,op2_name,op2_p_id,op2_path,op2_s_id,app2,app2_time,flag):
        self.id = id
        self.app_name = app_name
        self.app_id = app_id
        self.app_path = app_path
        self.op1_name = op1_name
        self.op1_p_id = op1_p_id
        self.op1_path = op1_path
        self.op1_s_id = op1_s_id
        self.app1 = app1
        self.app1_time = app1_time
        self.op2_name = op2_name
        self.op2_p_id = op2_p_id
        self.op2_path = op2_path
        self.op2_s_id = op2_s_id
        self.app2 = app2
        self.app2_time = app2_time
        self.flag = flag

class VaultReason:
    def __init__(self,id,op_name,op_tele,op_org,op_path,reason,op_time,
                 app_name,app_id,app_tele,app_org,app_path,app_time):
        self.id = id
        self.op_name = op_name
        self.op_tele = op_tele
        self.op_org = op_org
        self.op_path = op_path
        self.reason = reason
        self.op_time = op_time
        self.app_name = app_name
        self.app_id = app_id
        self.app_tele = app_tele
        self.app_org = app_org
        self.app_path = app_path
        self.app_time = app_time

class BesPljk:
    def __init__(self,person_id,region_id,username,zh_name,id_state,org_path,org,type,zh_type,query_cnt,time):
        self.person_id = person_id
        self.region_id = region_id
        self.username = username
        self.zh_name = zh_name
        self.id_state = id_state
        self.org_path = org_path
        self.org = org
        self.type = type
        self.zh_type = zh_type
        self.query_cnt = query_cnt
        self.time = time

class BesYcsj:
    def __init__(self,person_id,region_id,username,id_state,zh_name,org_path,org,time,op_cnt,op_sum,per):
        self.person_id = person_id
        self.region_id = region_id
        self.username = username
        self.zh_name = zh_name
        self.id_state = id_state
        self.org_path = org_path
        self.org = org
        self.time = time
        self.op_cnt = op_cnt
        self.op_sum = op_sum
        self.per = per

class BesDsj:
    def __init__(self,person_id,region_id,username,id_state,zh_name,org_path,org,type,zh_type,time,cnt):
        self.person_id = person_id
        self.region_id = region_id
        self.username = username
        self.id_state = id_state
        self.zh_name = zh_name
        self.org_path = org_path
        self.org = org
        self.time = time
        self.type = type
        self.zh_type = zh_type
        self.cnt = cnt

class BesSum:
    def __init__(self,person_id,region_id,cnt,username,id_state,zh_name,org_path,org,time):
        self.person_id = person_id
        self.region_id = region_id
        self.cnt = cnt
        self.username = username
        self.id_state = id_state
        self.zh_name = zh_name
        self.org_path = org_path
        self.org = org
        self.time = time

class PwDetectDetail:
    def __init__(self,id,db,region_id,staff_id,staff_name,org,mobile,ip,op_time,
                 pw,cydl,dcn,fhtz,interval,op_cnt,repeat_per,remark):
        self.id = id
        self.db = db
        self.region_id = region_id
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.org = org
        self.mobile = mobile
        self.ip = ip
        self.op_time = op_time
        self.pw = pw
        self.cydl = cydl
        self.dcn = dcn
        self.fhtz = fhtz
        self.interval = interval
        self.op_cnt = op_cnt
        self.repeat_per = repeat_per
        self.remark = remark

class PwDetectItem:
    def __init__(self,org,staff_id,staff_name,op_time,op_cnt,number_cnt,remark):
        self.org = org
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.op_time = op_time
        self.op_cnt = op_cnt
        self.number_cnt = number_cnt
        self.remark = remark

class OrderQueryItem:
    def __init__(self,id,region_id,op_time,staff_id,username,zh_name,op_path,
                 op_org,op_res,start_time,end_time,ob_id,order_type,telephone):
        self.id = id
        self.region_id = region_id
        self.op_time = op_time
        self.staff_id = staff_id
        self.username = username
        self.zh_name = zh_name
        self.op_path = op_path
        self.op_org = op_org
        self.op_res = op_res
        self.start_time = start_time
        self.end_time = end_time
        self.ob_id = ob_id
        self.order_type = order_type
        self.telephone = telephone

class SstQueryItem:
    def __init__(self,id,oper_time,telephone,staff_id,zh_name,org,op_time):
        self.id = id
        self.oper_time = oper_time
        self.telephone = telephone
        self.staff_id = staff_id
        self.zh_name = zh_name
        self.org = org
        self.op_time = op_time


