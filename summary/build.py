from summary import constant

def get_jk_path(depart,project,date):
    file_name = project+date[5:6]+'月份汇总.xlsx'
    return constant.root+date+'/反馈后结果/'+depart+'/'+file_name
# def get_qt_op_path(depart,project,date):
#     file_name = project+date[4:6]+'月份汇总.xlsx'
#     return constant.root+date+'/反馈后结果/'+depart+'/'+file_name
# def get_qt_set_path(depart,project,date):
#     file_name = project+date[4:6]+'月份汇总.xlsx'
#     return constant.root+date+'/反馈后结果/'+depart+'/'+file_name
# def get_qt_reason_path(depart,project,date):
#     file_name = project+date[4:6]+'月份汇总.xlsx'
#     return constant.root+date+'/反馈后结果/'+depart+'/'+file_name
def get_bes_path(depart,project,date,start_date,end_date):
    file_name = project+start_date+'-'+end_date[4:]+'.xlsx'
    return constant.root+date+'/反馈后结果/'+depart+'/'+file_name
# def get_bes_op_path(depart,project,date,start_date,end_date):
#     file_name = project+start_date+'-'+end_date[4:]+'.xlsx'
#     return constant.root+date+'/反馈后结果/'+depart+'/'+file_name
# def get_yc_jk_path(depart,project,date,start_date,end_date):
#     file_name = project+start_date+'-'+end_date[4:]+'.xlsx'
#     return constant.root+date+'/反馈后结果/'+depart+'/'+file_name
# def get_yc_time_path(depart,project,date,start_date,end_date):
#     file_name = project+start_date+'-'+end_date[4:]+'.xlsx'
#     return constant.root+date+'/反馈后结果/'+depart+'/'+file_name
def get_order_path(depart,project,date):
    file_name = project+date+'.xlsx'
    return constant.root+date+'/反馈后结果/'+depart+'/'+file_name
# def get_multi_order_path(depart,project,date):
#     file_name = project+date+'.xlsx'
#     return constant.root+date+'/反馈后结果/'+depart+'/'+file_name
def get_ip_or_plugin_path(depart,project,date):
    file_name = project+date+'.xls'
    return constant.root + date + '/反馈后结果/' + depart + '/' + file_name
def get_sst_path(depart,project,date):
    file_name = project+date+'.xlsx'
    return constant.root+date+'/反馈后结果/'+depart+'/'+file_name

def output_jk_path(project,date):
    file_name = project+date[5:6]+'月份汇总.xlsx'
    return (constant.root+date+'/'+constant.output_directory+date+'/'+constant.category_list[0]+'/'+file_name)
# def output_qt_op_path(project,date):
#     file_name = project+date[4:6]+'月份汇总.xlsx'
#     return (constant.root+date+'/'+constant.output_directory+'/'+constant.category_list[0]+'/'+file_name)
# def output_qt_set_path(project,date):
#     file_name = project+date[4:6]+'月份汇总.xlsx'
#     return (constant.root+date+'/'+constant.output_directory+'/'+constant.category_list[0]+'/'+file_name)
# def output_qt_reason_path(project,date):
#     file_name = project+date[4:6]+'月份汇总.xlsx'
#     return (constant.root+date+'/'+constant.output_directory+'/'+constant.category_list[0]+'/'+file_name)
def output_bes_path(project,date,start_date,end_date):
    file_name = project+start_date+'-'+end_date[4:]+'.xlsx'
    return (constant.root+date+'/'+constant.output_directory+date+'/'+constant.category_list[1]+'/苏州/'+file_name)
# def output_bes_op_path(project,date,start_date,end_date):
#     file_name = project+start_date+'-'+end_date[4:]+'.xlsx'
#     return (constant.root+date+'/'+constant.output_directory+'/'+constant.category_list[1]+'/苏州/'+file_name)
# def output_yc_jk_path(project,date,start_date,end_date):
#     file_name = project+start_date+'-'+end_date[4:]+'.xlsx'
#     return (constant.root+date+'/'+constant.output_directory+'/'+constant.category_list[1]+'/苏州/'+file_name)
# def output_yc_time_path(project,date,start_date,end_date):
#     file_name = project+start_date+'-'+end_date[4:]+'.xlsx'
#     return (constant.root+date+'/'+constant.output_directory+'/'+constant.category_list[1]+'/苏州/'+file_name)
def output_order_path(project,date):
    file_name = project+date+'.xlsx'
    return (constant.root+date+'/'+constant.output_directory+date+'/'+constant.category_list[2]+'/'+file_name)
# def output_multiple_order_path(project,date):
#     file_name = project+date+'.xlsx'
#     return (constant.root+date+'/'+constant.output_directory+'/'+constant.category_list[2]+'/'+file_name)
def output_ip_path(project,date):
    file_name = project+date+'.xlsx'
    return (constant.root + date + '/' + constant.output_directory + date + '/' + constant.category_list[
        3] + '/' + file_name)

def output_plugin_path(project,date):
    file_name = project+date+'.xlsx'
    return (constant.root + date + '/' + constant.output_directory + date + '/' + constant.category_list[
        4] + '/' + file_name)

def output_sst_path(project,date):
    file_name = project+date+'.xlsx'
    return (constant.root + date + '/' + constant.output_directory + date + '/' + file_name)