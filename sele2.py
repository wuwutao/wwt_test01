
# #1.1
# from selenium import webdriver
# import time 
# from module import Mail

# driver = webdriver.Chrome()
# driver.get("http://www.126.com")

# time.sleep(2)

#x-URS-iframe1617589200641.3623
# name=driver.find_element_by_xpath("//*[@id='x-URS-iframe']")
# iframe = driver.find_elements_by_tag_name("iframe")[0]
# driver.switch_to.frame(iframe)
# driver.find_element_by_class_name("j-inputtext.dlemail.j-nameforslide").click()
# driver.find_element_by_class_name("j-inputtext.dlemail.j-nameforslide").send_keys("2382328231")

# driver.find_element_by_class_name("j-inputtext.dlpwd").click()
# driver.find_element_by_class_name("j-inputtext.dlpwd").send_keys("12345678")

# driver.find_element_by_class_name("u-checkbox.tabfocus").click()

# driver.find_element_by_id("dologin").click()
# time.sleep(5)

# driver.quit()
# y = driver.find_element_by_class_name("httploginframe")
# driver.switch_to.frame(y)
# driver.find_element_by_class_name("u-loginbtn.btncolor.tabfocus.btndisabled").click()




#1.2
# from selenium import webdriver
# import time 
# from module import Mail
# import read_test
# driver = webdriver.Chrome()
# driver.get("http://www.126.com")
# time.sleep(2)

# #读取数据，从文本中txt  
# with open('./files/user_info.txt','r') as f:
#     data=f.readlines()
# #定义个数组
# users=[]
# for i in data:
#     #用一个变量装切片后的内容
#     user=i[:-1].split(":")
#     #将变量中的内容传到users 数组中
#     users.append(user)
# print(users)
# # #设置句柄
# a1=driver.current_window_handle    
# #在内置函数中定义driver,初始就要有
# mains = Mail(driver)
# mains.login_1(users[0][0],users[0][1])


# #读取csv文件
# from selenium import webdriver
# from module import Mail
# import time
# import csv      #1.3 从cvs 中读取文件内容
# import codecs    #中文的编码格式

# from itertools import islice        #跳过第一行内容

# users=[]
# data=csv.reader(codecs.open('./files/user_info.csv','r','gbk'))
# for lines in islice(data,1,None):
#     users.append(lines)


# driver=webdriver.Chrome()
# driver.get("http://www.126.com")

# mainss = Mail(driver)
# mainss.login_1(users[0][0],users[0][1])

# time.sleep(2)

#在lojin在传两个参数是name,password
# mains.login_1("15960262793","wwt123456")
# mains.login_1("123456789","wwt123456")
#mains.login_1(users[0][0],users[0][1])
#调用从数组中得到的数组的元素： username,passward


# driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[3]/div[4]/div[1]/div[2]/a[1]").click()
# #判断注册网易免费邮箱
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     if "注册网易免费邮箱" in driver.title:
#         break

# time.sleep(2)
# driver.switch_to_window(a1)
# #driver.quit()

# mains.qiut_1()


#读取xml文件
# from selenium import webdriver
# from module import Mail
# import time

#coding=utf-8
from xml.dom.minidom import parse

#打开xml文件
dom =parse("./files/test.xml")

#得到文档对象
root = dom.documentElement

login =root.getElementsByTagName("login")

#获得login中的两个属性值：
username=login[0].getAttribute("username")
print(username) #admin

password=login[0].getAttribute("password")
print(password) #123456

username=login[1].getAttribute("username")
print(username) #wode

password=login[1].getAttribute("password")
print(password) #321654

#获得一组标签
tag_name=root.getElementsByTagName("os")
print(tag_name[0].firstChild.data)



# driver=webdriver.Chrome()
# driver.get("http://www.126.com")

# mainss = Mail(driver)
# mainss.login_1(users[0][0],users[0][1])

# time.sleep(2)