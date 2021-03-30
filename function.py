
# # 方法：
# #def :方法的声明
# #jiafa:方法的名称
# #a,b:参数
# def jiafa(a,b):
#     ''' 
#     方法的声明
#     这是一个加法的方法
#     '''
#     if type(a) is int and type(b) is int:
#         return a+b
#     else:
#         return "输入的类型不正确,请重新输入"

# a = jiafa(1,1)
# print(a)

# """
# 返回值返回后，我们可以对返回来的值进行操作，
# 而print 不能
# """
'''
def jiafa(a,b):

    if type(a) is int and type(b) is int:
        print(a+b)
    else:
        print("输入的类型有误")

#不能拿到jiafa 方法算出的值，取出来的值是None
a = jiafa(12,23)
print(a)


def check_name(username):
    if  len(username) >= 5 and len(username) <= 8  :
        if username[0] in "qwertyuiopasdfghjklzxcvbnm ":
            return True
        else:
            return "输入的账号不是小写字母开头"
    else:
        return "输入账号的格式不正确，请重新输入:"
        

username=input("请输入你的注册账号:")
password=input("请输入你的注册密码：")

if check_name(username)==True:
    if len(password)>=6 and len(password)<=12:
        print("注册成功",{username,password})
    else:
        print("输入的密码长度错误")

else:
    print(check_name(username))     # 打印check_name 中返回的错误信息，输入的账号不是小写字母开头，输入账号的格式不正确，请重新输入


try:
    print("aa"+1)
except Exception as e:
    print("代码出错了",e)
    
'''

def check_n(user,pas):

    if len(user) >= 6 and len(user) <=8:

        if user[0] in "qwertyuioapsdfghjklzxcbvnm":

            if len(pas) >= 7 and len(pas) <= 12:
                #print("注册成功",{user,pas}) 
                return True
            else:
                return "密码的长度不对"
        else:
            return "第一个字母的小写字母"
    else:
        return "输出的账号长度不对"
        
user=input("请输入你的注册账号:")
pas=input("请输入你的注册密码：")

check_n(user,pas)
print(check_n(user,pas))        #会把return 中的值传递进去，打印出来
# if check_n(user,pas) == True:
#     print("注册成功",{user,pas})
# else:
#     print(check_n(user,pas))
    
# check_n(user,pas)
