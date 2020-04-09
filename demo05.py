#异常捕获
try:
    print(2+"123")
except:
    print("出问题了")

#异常类  定位问题
try:
    print(2+jdfg)
except Exception as e:
    print("出问题了",e)

#代码的方法
#包--模块--类--方法--变量
#导入自带包
import time
import random
for i in range(10):
    time.sleep(1) #停顿一秒后再进行下一个操作
    print(i)
a=random.randint(1,100)
print(a)

#第三方包
'''
cmd中输入 pip3 list 查看已有的包
        pip3 install 安装包
'''

