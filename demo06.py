#类的实现
#类名首字母必须大写
'''
面向对象编程
类里所有的方法必须传self参数

类定义了一个对象的整体概念，其属性、方法
实例化类：整体概念的某个具体对象
可以调用该类下的所有属性、方法

类的特点
继承，重写/多态

'''
class GirlFriend():
    '''
    女朋友
    '''
    def __init__(self,sex,height,weight,hair,age):
        self.sex=sex
        self.height=height
        self.weight=weight
        self.hair=hair
        self.age=age
    
    def like(self,num):
        print("性别为"+self.sex+"的人开始了",end="")
        if num==1:
            print("吹箫")
        elif num==2:
            print("绘画")
        else:
            print("游戏")
    def skill(self):
        print("厨艺")
    def work(self):
        print("设计师")

#类的实例化
candy=GirlFriend("女","170","100","black","20")
candy.like(1)
candy.work()
print(candy.hair)


#类的继承、重写   子类继承父类的所有属性、方法
class GirlFriend2(GirlFriend):
    def work(self):
        print("市长")

mary=GirlFriend2("男","170","100","black","20")  
mary.like(1)
mary.work()
print(mary.hair)  



