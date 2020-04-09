#定义方法
def CheckUsername(username):
    '''
    判断用户名是否合规
    '''
    if len(username)>=5 and len(username)<=8:
        if username[0] in "qazwsxedcrfvtgbyhnujmikolp":
            return "ok"
        else:
            return "首字母要大写"
    else:
        return "长度不合规"

print(CheckUsername("asd"))