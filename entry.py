import os

from constant import AuditConstant
import service
from utils.date_util import DateTimeUtil
from utils.db_util import db_connect

if __name__ == '__main__':
    ct = AuditConstant()
    date_util = DateTimeUtil()
    date = date_util.get_last_month()
    root_path = ct.root+date+'/'+date+'/'


    # 获取源文件路径
    file_path_list = []
    for category in ct.category_list:
        directory_path = root_path+category
        if category != '6、首三推查询日志.xls':
            project_list = ct.jh_project_list[category]
            for project in project_list:
                file_path = directory_path+'/'
                if category == '1、金库':
                    file_path += project+date_util.date2filename(date_str=date,category=category)+'.xlsx'
                if category == '2、bes批量监控审计':
                    file_path += '苏州/'+project
                    start_date = date_util.get_last_month_start()
                    end_date = date_util.get_last_month_end()[4:8]
                    file_path += start_date+'-'+end_date+'.xlsx'
                if category == '3、密码探测':
                    file_path += date_util.date2filename(date_str=date,category=category)+project+'.xlsx'
                if category == '5、前台详单':
                    file_path += project+date+'.xlsx'
                file_path_list.append(file_path)
        else:
            file_path_list.append(directory_path)

    for file_path in file_path_list:
        print(file_path)

    # 上传审计数据
    db_connect = db_connect()
    log_file_path = root_path + 'log.txt'
    print('【金库前台异常申请理由】开始上传')
    service.upload_vault_reason(db_connect, file_path_list[1], date, log_file_path)
    print('【苏州bes批量监控审计】开始上传')
    service.upload_bes_pljk(db_connect, file_path_list[2], date, log_file_path)
    print('【苏州bes人员异常操作业务数据与全天占比超70%审计】开始上传')
    service.upload_bes_ycsj(db_connect, file_path_list[3], date, log_file_path)
    print('【苏州异常监控每人每个业务1分钟内大于3次汇总】开始上传')
    service.upload_bes_dsj(db_connect, file_path_list[4], date, log_file_path)
    print('【苏州异常时间过户、开户、补卡、复机汇总】开始上传')
    service.upload_bes_sum(db_connect, file_path_list[5], date, log_file_path)
    print('【密码探测登录失败明细统计】开始上传')
    service.upload_pw_detect_detail(db_connect, file_path_list[6], date, log_file_path)
    print('【全省前台客户服务密码探测表】开始上传')
    service.upload_pw_detect_sum(db_connect, file_path_list[7], date, log_file_path)
    print('【单个清单查询】开始上传')
    service.upload_order_query(db_connect, file_path_list[8], date, log_file_path)
    print('【首三推查询日志】开始上传')
    service.upload_sst_query(db_connect, file_path_list[9], date, log_file_path)
