#判断
age = int(input())
if age>60:
    print("您已经很老了")
elif age>30:
    print("您还要继续努力")
elif age>20:
    print("您刚刚开始")
else:
    print("好好学习")

#判断符号
# ==，！= ，>,<,in,is,
a="你好"
if a in "你好呀":
    print(True)
else:
    print(False)

a=input("请输入")
if a in "0123456789":
    a=int(a)
    print(a)
else:
    print("请输入正确的年龄")
    exit()

b=10
if type(b) is int:
    print("是数字")
elif type(b) is str:
    print("是字符串")
else:
    print("其他")