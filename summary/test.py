# import pandas as pd
# df = pd.read_excel('D:/安全审计/202403/反馈后结果/姑苏/01-单个清单查询_202403.xlsx',sheet_name='明细')

import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_last_month_end(month_str=None):
    # 获取上一个月的最后一天
    '''
    param: month_str 月份，2021-04
    '''
    # return: 格式 %Y-%m-%d
    if not month_str:
        month_str = datetime.now().strftime('%Y-%m')
    year, month = int(month_str.split('-')[0]), int(month_str.split('-')[1])
    if month == 1:
        year -= 1
        month = 12
    else:
        month -= 1
    end = calendar.monthrange(year, month)[1]
    if month < 10:
        month = '0'+str(month)
    return '{}-{}-{}'.format(year, month, end)
    # return '{}{}{}'.format(year, month, end)

print(get_last_month_end())