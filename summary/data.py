import os
import pandas as pd
import numpy as np
import build
import summary.constant as ct

def read_data(depart,project,index,date,start_date,end_date):
    df = None
    file_path = ''
    if index <= 3:
        file_path = build.get_jk_path(depart,project,date)
    if 4 <= index <= 7:
        file_path = build.get_bes_path(depart, project, date,start_date,end_date)
    if 8 <= index <= 9:
        file_path = build.get_order_path(depart, project, date)
    if 10 <= index <= 11:
        file_path = build.get_ip_or_plugin_path(depart, project, date)
    if index == 12:
        file_path = build.get_sst_path(depart, project, date)
    # print('文件路径：'+file_path)
    if os.path.exists(file_path):
        df = pd.read_excel(file_path,sheet_name=ct.sheet_list[index],dtype=str)
        if index != 9:
            df = df[df['区县'].notna()]
        else:
            df = df[df['地市'] == '苏州']
        if 4 <= index <= 7 or 10 <= index <= 11:
            df = df[df['操作原因反馈'].notna()]
        else:
            df = df[df[df.columns[-1]].notna()]
    return df

def upload_data(df,project,index,date,start_date,end_date):
    file_path = ''
    if index <= 3:
        file_path = build.output_jk_path(project, date)
    if 4 <= index <= 7:
        file_path = build.output_bes_path(project, date, start_date, end_date)
    if 8 <= index <= 9:
        file_path = build.output_order_path(project, date)
    if index == 10:
        file_path = build.output_ip_path(project, date)
    if index == 11:
        file_path = build.output_plugin_path(project, date)
    if index == 12:
        file_path = build.output_sst_path(project,date)

    target_dir = os.path.dirname(file_path)
    os.makedirs(target_dir, exist_ok=True)
    df.to_excel(file_path,sheet_name=ct.sheet_list[index],index=False)
