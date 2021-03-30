
"""
a = input("输入a:")
b = input("输入b:")

if a>b:
    print("a大于b")

else:
    print("b更大")


age = int(input("请输入你的年龄："))
if age > 59:
    print("退休")

elif age < 20:
    print("你还年轻")

else:
   print("不知道你输入的是什么")

hish = {}
low = {}

list = ["张三","王武","莱尔","布莱顿","哈顿","科莱丽","来恩施","吉特迈","克莱斯","杰克斯"]
a = 0
while a < len(list):
    chengji = int(input("请输入"+list[a]+"的成绩:"))
    if chengji >= 60:
        hish[list[a]] = chengji
    else:
        low[list[a]] = chengji
    a = a + 1

print(hish,low) 

a={"ss":"wode",12:"sss","nihao":"wohao"}

for i in a:
    print(i)

tall_grade = {}
short_grade={}
list_student=["黄","叶","敖","吴","陈","付","李","张","成"]

a = 0 
while a < len(list_student):
    grade = int(input("请输入"+list_student[a]+"的成绩:"))
    if grade > 60:
        tall_grade[list_student[a]]=grade
    
    else:
        short_grade[list_student[a]]=grade

    a = a + 1

print("成绩大于60：",tall_grade)
print("成绩小于60:",short_grade)


hish = {}
low = {}

list = ["张三","王武","莱尔","布莱顿","哈顿","科莱丽","来恩施","吉特迈","克莱斯","杰克斯"]

for i in range(0,len(list)):
    chengji = int(input("请输入"+list[i]+"的成绩:"))
    if chengji >= 60:
        hish[list[i]] = chengji
    else:
        low[list[i]] = chengji
print(hish,low)  

#1.九九乘法表

for a in range(1,10):       # 输出1---10

    for b in range(1,10):       #输出1---10
        if a >= b :
            print(str(b)+"*"+str(a)+"="+str(a*b),end=" ")  
    print()
    
# 2.九九乘法表

for i in range(1,10):
    for j in range(1,10):
        if i>=j:           
            print(i,"*",j,"=",i*j,end=" ")
    print()  #打印了一个空，就是实现一个换行

# 3 九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="  ")
    print()
    
    #练习一：
import time
while True:
    for i in range(31,1,-1):
        time.sleep(1)
        print("现在是红灯不能走",i)
    for j in range(36,1,-1):
        time.sleep(1)
        print("好了，已经绿灯了,请通行",j)
    for k in range(4,1,-1):
        time.sleep(1)
        print("等会等会，黄灯",k)

light={"red_light":30,"green_light":35,"yellow_light":5}

for i in light:
    #for j in range(light[i],0,-1):  
        #print(i,j)
    for j in range(light[i]):
        print(i,light[i]-j)


#练习二，实现注册功能

admin={}
a=input("请输入你的注册账号:")
b=input("请输入你的注册密码：")

if  len(a) > 5 and len(a) < 8  :
    if a[0].islower:
#    if a[0] in "qwertyuiopasdfghjklzxcvbnm":
        if len(b) > 6 and len(b) <12:
            admin[a]=b
            print("恭喜你注册成功")
            print(admin)
        else:
            print("输入密码的格式不正确，请重新输入：")
    else:
        print("输入的 账号不是小写字母开头")
else:
    print("输入账号的格式不正确，请重新输入:")

a=input("请输入你的注册账号:")
b=input("请输入你的注册密码：")

if  len(a) >= 5 and len(a) <= 8  :
    if a[0] in "qwertyuiopasdfghjklzxcvbnm ":
        if len(b) >= 6 and len(b) <= 12:
            print("恭喜你注册成功",{a:b})
        else:
            print("输入密码的格式不正确，请重新输入：")
    else:
        print("输入的账号不是小写字母开头")
else:
    print("输入账号的格式不正确，请重新输入:")

# break

for i in range(10):
    if i == 4:
        break
    print(i)


for i in range(1,10):
    for j in range(1,i+1):
        if i==3:
            break
        print(i,"*",j,"=",i*j,end=" ")
    print()

"""