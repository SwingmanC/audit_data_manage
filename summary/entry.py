import pandas as pd
import os

from utils.date_util import DateTimeUtil
import summary.constant as ct
import summary.data as data

date_util = DateTimeUtil()
date = date_util.get_last_month(number=1)
start_date = date_util.get_last_month_start()
end_date = date_util.get_last_month_end()

# jk_dsj_df,qt_op_df,qt_set_df,qt_reason_df,bes_jk_df,bes_op_df,yc_jk_df,yc_time_df,single_order_df,multi_order_df = None,None,None,None,None,None,None,None,None,None
df_list = [None,None,None,None,None,None,None,None,None,None,None,None,None]

for depart in ct.depart_list:
    index = 0
    for project in ct.project_list:
        print('正在读取：【'+depart+'】项目：'+project)
        df = data.read_data(depart=depart, project=project, index=index, date=date, start_date=start_date, end_date=end_date)
        if df is not None:
            if df_list[index] is None:
                df_list[index] = df
            else:
                df_list[index] = df_list[index]._append(df,ignore_index=True)
        index += 1

index = 0
for df in df_list:
    if df is not None:
        data.upload_data(df, ct.project_list[index], index, date, start_date, end_date)
    index += 1