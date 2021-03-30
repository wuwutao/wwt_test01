
"""
print(a[2])
print(a.count(3))
print(a.index(3))

b=(a,"haha","hihi",3)

print(b[0][1])

a=("sss","ss",1,2,3,3,3,3,3,"哈哈","嘻嘻")

#切片
print(a[:])
print(a[:2])
print(a[2:9])
print(a[9:])


a=["sss","ss",1,2,3,3,3,3,3,"哈哈","嘻嘻"]
a.append(5)
print(a)

a.insert(5,"wwt")
print(a)

a.pop(5)
print(a)

#数组进行切片
print(a[0:2])
print(a[2:9])

x=["a","b","c"]
a.extend(x)  
print(a)

y=["as","ss"]
print(a+y)

print(a)
a.remove("哈哈")
print(a)

ww=[True,False,0,1]
a.extend(ww)
print(a)

a.remove(1)
print(a)

a.remove("sss")
print(a)



a={"name":"战士",1:"你好"}
print(a["name"])

a["ddd"] = "wode"
print(a)

b = a.get("name")
print(b)

x = a.pop("ddd")
print(x)

print(a)



print("请输入你的个人信息：")
a =input("name:")
b =input("age:")
c=input("sex:")



list={}
list.update(name=a)
list.update(age=b)
list.update(sex=c)

print(list)

print("haha")
a={"name":input("姓名："),"age":input("年龄："),"sex":input("性别：")}
print(a)
"""

# name =input("name:")
# b =input("age:")
# c=input("sex:")
# list.update(name=name,age=b,sex=c)
# print(list)

print("请输入你的个人信息：")
a =input("name:")
b =input("age:")
c=input("sex:")

list={}
list.update(name=a)
list.update(age=b)
list.update(sex=c)

print(list)

print("a")