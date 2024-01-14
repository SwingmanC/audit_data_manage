def write_log(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content+'\n')
    except Exception as e:
        print(f"日志文件创建/写入发生错误：{e}")