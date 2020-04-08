# while循环 
a=["张三","李四","王五","孙六"]
b=[]
c={}
d={}
index=0
while index<len(a):
    b.append(int(input("请输入"+a[index]+"成绩")))
    c[a[index]]=b[index]
    if c[a[index]]<60:
        d[a[index]]=c.pop(a[index])
    index=index+1
print(c)
print(d)

# for循环 --遍历
a="你好呀，今天怎么样"
a=[1,2,3,4,5,6]
for i in a:
    print(i)

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"*",i,"=",i*j,end=" ")
    print()
#模拟红绿灯功能，红灯30次，黄灯3次，绿灯35次
light={
    "红灯":30,
    "绿灯":35,
    "黄灯":3
}
for i in light:
    for j in range(light[i]):
        print(i,"倒计时还有",light[i]-j,"秒")


# 跳出循环
#continue -- 停止本轮循环，进行下一轮循环
for i in range(10):
    if i==4:
        continue
    print(i)
#break -- 跳出最近一层的循环