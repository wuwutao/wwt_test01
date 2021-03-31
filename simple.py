"""
#1.交换两个变量的值：
a=input("请输入第一个数：")
b=input("请输入第二个数：")
t=a
a=b
b=t
print("交换后的值为：{},{}".format(a,b))

#format的用法
print("name:{},url地址：url:{}".format("wwt12345","www.baidu.com"))

class   Test():
    def __init__(self,value):

        self.value = value

value = Test(6)
print("获取到的value为：{0.value}".format(value))


#2.设置将摄氏温度转换为华氏温度

#华氏摄氏度 = 1.8*摄氏温度+32
#摄氏温度 = (华氏温度-32)/1.8

#摄氏温度---->华氏温度：华氏摄氏度 = 1.8*摄氏温度+32
sheshi = float(input("请输入你要转换的摄氏温度："))
huashi = 1.8 * sheshi +32 
print("转化为华氏度是：",huashi,"华氏度")

huashi = float(input("请输入你要转换的华氏度："))
sheshi = (huashi-32)/1.8
print("华氏度转化为摄氏度是：",sheshi,"摄氏度")



#需要你输入带符号的温度值，来判断你需要做什么
#如果输入的是F、f,则判断是将华氏--->摄氏
#如果输入的是C,c,     就是将摄氏--->华氏
T=input("请输入带符号的温度值：")
if T[-1] in ['F','f']:           #T[-1]:代表的是取最后一个字符,判断
    C=(eval(T[:-1])-32)/1.8     #T[0:-1]:代表的就是去前面输入的所有，不包括最后一个数
    print("得到的摄氏温度值是：{}℃".format(C))

elif T[-1] in ['C','c']:
    C=(eval(T[:-1])+32)*1.8
    print("得到的华氏温度值是：{}F".format(C))

else:
    print("输入的格式有错误，请重新输入：") 
    

#判断用户输入的温度，转成他想要转换成的温度

username = input("请输入你需要转换的数字和单位:")

if username[-1] in ["F","f"]:
    #说明用户需要将华氏---->摄氏
    C=(eval(username[:-1]))/1.8-32
    print("得到的摄氏温度是：{}℃".format(C))
elif username[-1] in ["C","c"]:
    #说明要将摄氏---->华氏
    C=(eval(username[0:-1])+32)*1.8
    print("得到的华氏摄氏度是：{}F".format(C))

else:
    print("输入的格式出现问题,请重新输入")  

a="12+31"
b=eval(a)
print(type(b))
print(b)

a =10
g={'a':4}
#结果为5
print(eval("a+1",g))

a=10
b=20
c=30                        

g={'a':6,'b':8}              #a=6  b=8
t={'b':100,'c':10}           #b=100 c=10
                             #最后得出a=6,b=100,c=10,因为后面出来的100，会覆盖前面的b,所以被覆盖
#只输出g+t=a+b+c =6+100+10=116  所以最后的结果是116
print(eval('a+b+c',g,t))     

#求数中各位数之和：eg:123   :求个位+十位+百位之和：

shuzi = int(input("请输入一个三位数："))
a=int(shuzi/100)
b=int(shuzi/10%10)
c=int(shuzi%100%10)

print("各个位数之和是：",a+b+c)

a =int(input("请输入数字："))
sum=0
while a>0:
    b=a%10
    a=a//10
    sum =sum+b

print(sum)

#求各个位数之和：
a=int(input("请输入你需要计算各位数之和:"))     #a=212
sum=0
while a>0:                          
    b=a%10      #每次都取到个位数上的值:         #a=21 时 ，已经取了 1的值 ,a=21/10=2,b=2%10=2 所以2+1+2=5
    a=a//10      #每次计算完除以10，继续往左走一位，继续计算,如果是小数，自动取整    
    sum=sum+b   #将取余的值都进行累加

print("各个位数之和为：",sum)


num=int(input("请输入你要判断的数："))

flag = True
for i in range(2,num):           
    if num%i ==0:            #如何任意一个数能被输入的数整除的话，就说明这个数不是质数
        flag = False    
        break

if flag:                     
    print(num,"是质数")

else:
    print(num,"不是质数")
    


#输出2-100之间的所有质数：

zhishu=[]   #使用一个列表装着
for i in range(2,101):      #遍历2-100所有的数      
    for x in range(2,i):    #将i赋值全部赋值给x,只要能除尽任意一个数，就说明它不是个素数
        if i%x==0:
            break
    else:
        zhishu.append(i)
        
print(zhishu)    

zhansan=[]
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        zhansan.append(i)
print(zhansan)



#问题:编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，
#2000年至3200年(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。

for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,",",end="")

#问题:编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8
#则输出为:40320     8!=8*7*6*5*4*3*2*1

shuchu=int(input("请输入一个数："))

while shuchu>0:
    shuchu!=shuchu*(shuchu-1)

#问题:使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，该字典包含1到n之间的整数(两者都包含)。
#然后程序应该打印字典。假设向程序提供以下输入:8
#{1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}

dict={}

shuru=int(input("请输入一个数："))
for i in range(1,shuru+1):
    dict[i]=i*i
print(dict)

# 问题:编写一个程序，该程序接受控制台以逗号分隔的数字序列，并生成包含每个数字的列表和元组。假设向程序提供以下输入:
# 34岁,67年,55岁,33岁,12日,98年
# 则输出为:['34'， '67'， '55'， '33'， '12'， '98']
#         ('34'， '67'， '55'， '33'， '12'， '98')


x=input("请输入一组数据：")
b=[x]
print(b)


# 问题:定义一个至少有两个方法的类:        
# getString:从控制台输入获取字符串       
# printString::打印大写母的字符串。
# 还请包含简单的测试函数来测试类方法。

class Leiming():
    def __init__(self):
        pass

    def getString(self,a):
        return a
    def printString(self,b):   
        return b.upper()

a=input("请输入一串字符串：")        
huoqu=Leiming()
x = huoqu.getString(a)
print(x)

b=input("请输入一串字符,打印成大写:")
y=huoqu.printString(b)
print(y)

# 编写一个程序，根据给定的公式计算并打印值:Q=\sqrt{[(2*C*D)/H]}。
# 以下是C和H的固定值:C是50。H是30。D是一个变量，它的值应该以逗号分隔的序列输入到程序中。
# 例子假设程序的输入序列是逗号分隔的:100，150，180，
# 程序输出为:18，22，24

import math

C =50
H =30
        #遇到问题：如何用逗号隔开
D=[100,150,180]
# D=input("请输入D的值:")
print(D)
for i in range(D[0],D[1],D[2]):
    Q =int(math.sqrt(2*C*i/H))

print(Q)

# 问题:编写一个程序，以2位数字，X,Y作为输入，生成一个二维数组。数组的第i行和第j列中的元素值应该是i*j。
# 注意:i= 0,1 . .,X - 1;    j = 0, 1,­Y-1。
# 例子假设程序有以下输入:3、5
# 则程序输出为:[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]

a=int(input("请输入行数："))
b=int(input("请输入列数："))

x=[]
y=[]

for i in range(1,a+1):
    for j in range(1,b+1):
        print(y[j])


# 题：写一个可以计算数字平方值的方法

# 提示： 使用**运算符

a=int(input("请输入一个数："))
print("他的平方是：",a**2)


def jisuan(num):
    return num**2

zhansa=jisuan(int(input("请输入一个数:")))
print(zhansa)


# 题： Python有许多内置函数，如果您不知道如何使用它，您可以在线阅读文档或查找一些书籍。
#      但是Python为每个内置函数都有一个内置的文档函数。
#      请编写一个程序来打印一些Python内置函数文档，例如abs（），int（），raw_input（）
#      并为您自己的功能添加文档

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def see(num):
    return num**2

print(see(2))
print(see.__doc__)


# 题：定义一个类，它具有类参数并具有相同的实例参数。
# 提示：定义一个实例参数，需要在__init__方法中添加它。您可以使用构造参数初始化对象，也可以稍后设置该值

class Person():
    name="yef"               #person 内部定义的局部变量,不会被改变
    def __init__(self,name=None):       #name=aas   
        self.name =name
    
wwt=Person("wwt")           #实例化wwt, 向Person 传递一个参数:aas    
                        #打印的是person里的值：/ 打印的是person传的值
print("%s is name %s" % (Person.name,wwt.name))     #因为wwt定义的实例是向类中传递了一个name的值叫aas
                                    #调用的是实例化的属性，传进去的值

nico = Person("hyf")                             
# nico.name = "Nico"            
print("%s name is %s" % (Person.name, nico.name))


# 题：编写一个程序来计算输入中单词的频率。 按字母顺序对键进行排序后输出。
# 假设为程序提供了以下输入：
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 然后，输出应该是：
# 2:2
# 3.:1
# 3?:1 
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# danci=input("请输入需要计算的单词:")
f={}
a="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
b=a.split()             #将a的输入的值按空格来划分，以列表的方式来存储
for i in b:             # 遍历列表中所有的元素           
    f[i]=f.get(i,0)+1   #将所有的元素存储到字典中

x= sorted(f.keys())    #将f字典中素有所有的单词进行排序，     

for w in x:                     #再遍历x    输出w,字典中出现的次数
    print("%s:%d"%(w,f[w]))



# 题：编写一个程序来计算输入中单词的频率。 按字母顺序对键进行排序后输出。
# 假设为程序提供了以下输入：
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 然后，输出应该是：


#wod e sod dssk a ss ss x d dx x ws s xx dp as sd sa ss e ss sad sad ssa as ds 
a=input("请输入一连串数据:")

lists={}
b=a.split()
for i in b:
    lists[i]=lists.get(i,0)+1
words=sorted(lists.keys())
for wo in words:
    print("%s:%d" % (wo,lists[wo]))


# 机器人从原点（0,0）开始在平面中移动。 
# 机器人可以通过给定的步骤向上,向下，向左和向右移动。 机器人运动的痕迹如下所示：
# UP 5
# DOWN 3
# LETF 3
# RIGHT 2
# 方向之后的数字是步骤。 请编写一个程序来计算一系列运动和原点之后距当前位置的距离。
# 如果距离是浮点数，则只打印最接近的整数。
# 例：如果给出以下元组作为程序的输入：
# UP 5
# DOWN 3
# LETF 3
# RIGHT 2
# 然后，程序的输出应该是：2


import math             #最后需要开根号进行计算最后的距离
pos = [0,0]             #初始位置为0
print("请输入：")          #输入你要进行的操作
while True:
    s = input()             #s存储你输入的内容
    # if not s:               #如果没有输入内容，跳出循环
    #     break
    movement = s.split(" ")     #将输入的内容按空格进行分割 up 5，以列表的方式进行存储：
  #  print(movement)
    direction = movement[0]         #方向=列表中的第0个元素
    steps = int(movement[1])        #走的距离就等于列表中的第1个元素
    if direction=="UP":             #如果向上：说明它走的距离就是正的，反之则是向下，减去他的距离
        pos[0]+=steps               #pos中第0个位置 = 它当前位子+走的步长
    elif direction=="DOWN":         #pos中第0个位置 = 它当前位子-走的步长
        pos[0]-=steps
    elif direction=="LEFT":         #pos中第1个位置 = 它当前位子-走的步长
        pos[1]-=steps
    elif direction=="RIGHT":        #pos中第1个位置 = 它当前位子+走的步长
        pos[1]+=steps
    else:                           
        pass
 
print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))     #计算最后的距离和原点的距离 



# 机器人从原点（0,0）开始在平面中移动。 
# 机器人可以通过给定的步骤向上,向下，向左和向右移动。 机器人运动的痕迹如下所示：
# UP 5
# DOWN 3
# LETF 3
# RIGHT 2
# 方向之后的数字是步骤。 请编写一个程序来计算一系列运动和原点之后距当前位置的距离。
# 如果距离是浮点数，则只打印最接近的整数。
# 例：如果给出以下元组作为程序的输入：
# UP 5
# DOWN 3
# LETF 3
# RIGHT 2
# 然后，程序的输出应该是：2

import math

pos=[0,0]
input("请输入要执行的操作:")
while True:
    s=input("")
    if not s:
        break
    move=s.split()
    step=move[0]    
    dection = int(move[1])
    if step=="UP":
        pos[0]+=dection
    
    elif step=="DOWN":
        pos[0]-=dection
    
    elif step=="LEFT":
        pos[1]-=dection
    
    elif step=="RIGHT":
        pos[1]+=dection

    else:
        pass

print(input(round(math.sqrt(pos[0]**2+pos[1]**2))))


# 题：使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。

# 提示：考虑使用yield。

class Fibonaiterator(object):
    def __init__(self,n):
        self.n=n
        self.index=0
        self.num1 = 0
        self.num2 = 1
        
    def __next__(self):
        if self.index < self.n:
            num = self.num1
            self.num1,self.num2=self.num2,self.num1+self.num2
            self.index+=1
            #最后需要获取到得到的结果，需要return
            return num
        else:
            raise StopIteration
    def __iter__(self):       
        return self

if __name__=="__main__":    
    f = Fibonaiterator(20)
    for num in f:
        print(num,end=" ")
        

def feibo_func(n):
    current_index = 0
    num1, num2 = 0, 1
    while current_index < n:

        #  1. 假如函数中有yield，则不再是函数，而是生成器
        #  2. yield 会产生一个断点,返回数据后暂时阻塞在此
        #  3. 假如yield后面紧接着一个数据，就会把数据返回，
        #     作为next()函数或者for ...in...迭代出的下一个值

        yield num1
        num1, num2 = num2, num1 + num2
        current_index += 1
 
 
gen = feibo_func(10)
print(gen)
for num in gen:
    print(num, end=' ')

"""

def fu():
    for i in range(6):
        arg = yield i
        print(arg)

print(fu())            #<generator object fu at 0x000002C2CFB43A20>
print(next(fu()))       
gu=fu()
print(next(gu))
c=gu.send("aaa")
print(c)