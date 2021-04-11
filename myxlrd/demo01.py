"""

a="ha"
b=input("输入的内容：")
print(b)

a=input()
print ("获取到你输入的内容：",a)

#加法运算
a=int(input("请输入第一个数："))
b=int(input("请输入第二个数："))

print(a+b)

print(type(()))
print(type([]))
print(type({}))

a=int(2.33)
b=float(5)

print(type(a))
print(type(b))

c="asdfafadgad ga gg  gag " 
print(len(c))

a=input("请输入第一段的内容：")
b=input("请输入第二段的内容：")

print(len(a)+len(b))
"""

class T():
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)

    def add(self):
        return self.a+self.b

print(T(3,4).add())

class B(T):
    #没对其进行调用
    def sub(self,a,b):
        return a-b

print(B(2,3).add())



