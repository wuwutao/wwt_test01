"""
#版本一
class GirlFriend():

    #因为每个人初始化她的女朋友的属性肯定是不一样的，自定义
    def __init__(self):
        self.sex="女"
        self.high="170cm"
        self.weight="55kg"
        self.age="18"

    def jineng(self,num):
        print("身高为"+self.high+"体重为："+self.weight+"女盆友要开始她的才艺了：")
        if(num==1):
            print("i can fly")

        elif(num==2):
            print("i can sing")

        else:
            print("i can sleep")

    def chuyi(self):
        print("i can eat too much")

    def work(self):
        print("i can take car")

#对自己女朋友的属于的初始化
zhangsan=GirlFriend()

zhangsan.work()
zhangsan.jineng(1)


#版本二
class GirlFriend():

    #因为每个人初始化她的女朋友的属性肯定是不一样的，自定义
    def __init__(self,sex,high,weight,age):
        self.sex=sex
        self.high=high
        self.weight=weight
        self.age=age

    def jineng(self,num):
        print("身高为"+self.high+"体重为："+self.weight+"女盆友要开始她的才艺了：")
        if(num==1):
            print("i can fly")

        elif(num==2):
            print("i can sing")

        else:
            print("i can sleep")

    def chuyi(self):
        print("i can eat too much")

    def work(self):
        print("i can take car")

#对自己女朋友的属于的初始化，控制属性的变化  
zhangsan=GirlFriend("男","170","75kg","48")

zhangsan.work()
zhangsan.jineng(1)
print(zhangsan.sex)

"""

#版本三
class GirlFriend():

    #因为每个人初始化她的女朋友的属性肯定是不一样的，自定义
    def __init__(self,sex,high,weight,age):
        self.sex=sex
        self.high=high
        self.weight=weight
        self.age=age

    def jineng(self,num):
        print("身高为"+self.high+"体重为："+self.weight+"女盆友要开始她的才艺了：")
        if(num==1):
            print("i can fly")

        elif(num==2):
            print("i can sing")

        else:
            print("i can sleep")

    def chuyi(self):
        print("i can eat too much")

    def work(self):
        print("i can take car")

#继承：
#子类:Nvpengyou
#父类：GirlFriend
class Nvpengyou(GirlFriend):
    def chuyi(self):
        print("我的厨艺天下无敌。。。")

#object:祖宗类
#__init__ ,就是继承object类中的一个方法
zhansan = Nvpengyou("女","168cm","50kg","18")
zhansan.chuyi()