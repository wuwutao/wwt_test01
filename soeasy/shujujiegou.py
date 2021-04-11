
'''
#python合并两个有序的数组

#a=[2,4,5,8,9,17]
#b=[6,10,15,21]
#将b的元素全部有序的插入到a数组中，全部打印输出

a=input("请输入第一个数组：")
b=input("请输入第二个数组：")

def lest1():
    a1 =a.split(",")
    return a1
    b1 =b.split(",")
    return b1

lest1()
for i in a:
    print(i,end=" ")

for i in b:
    print(i,end=" ")

'''
import random
import time
import string


print(time.time())                                  #获取当前已经经过的秒数
print(time.localtime(time.time()))                  #获取当前时间
print(time.asctime(time.localtime(time.time())))    

a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
random.shuffle(a)
print(a)

print(random.sample('zyxwvutsrqponmlkjihgfedcba',10))

ran_str = (''.join(random.sample(string.ascii_letters + string.digits, 8)))
print(ran_str)