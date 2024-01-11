def generate_id(busi_id,date,index):
    res = str(busi_id)+date
    if index < 10:
        res += '0000'
    elif index < 100:
        res += '000'
    elif index < 1000:
        res += '00'
    elif index < 10000:
        res += '0'
    res += str(index)
    return res
