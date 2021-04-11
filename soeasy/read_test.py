

with open('./files/user_info.txt','r') as f:
    data=f.readlines()

#定义个数组
users=[]
for i in data:

    #用一个变量装切片后的内容
    user=i[:-1].split(":")
    #将变量中的内容传到users 数组中
    users.append(user)

print(users)