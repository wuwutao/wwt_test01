
# #1.1
# from selenium import webdriver
# import unittest
# import time

# #定义test类：必须添加TestCase 方法
# class Test_baidu(unittest.TestCase):

#     #使用setup 连接数据库，使用teardown 关闭数据库
#     #调用前置，每执行一次都会执行一次里面内容
#     def setUp(self):
#         #驱动浏览器
#         self.driver=webdriver.Chrome()
#         #设置浏览器的url
#         self.bd_url="http://www.baidu.com"

#         #定义类：需要执行的测试用例
#     def test_search_key_selenium(self):
#         #get到一个url
#         self.driver.get(self.bd_url)
#         #获取元素，定位id
#         self.driver.find_element_by_id("kw").send_keys("selenium")
#         #点击click
#         self.driver.find_element_by_id("su").click()
        
#         time.sleep(5)
#         #获取到界面标题
#         title=self.driver.title
#         #设置断言，判断预期结果的title 是否等于实际结果的title
#         self.assertEqual(title,"selenium_百度搜索")

    
#     def test_search_key_unittest(self):

#         #获取地址
#         self.driver.get(self.bd_url)
#         #使用定位
#         self.driver.find_element_by_id("kw").send_keys("unittest")
#         self.driver.find_element_by_id("su").click()
#         time.sleep(5)
#         #使用断言
#         title = self.driver.title
#         self.assertEqual(title,"unittest_百度搜索")

#     #每执行完一次测试用例的调用都会执行
#     def tearDown(self):
#         self.driver.quit()


#     #只在本地执行，其他函数调用不了
# if __name__ =='__main__':
#     # 使用函数的套件，testsuite
#     suit=unittest.TestSuite()
#     #一次执行一条：需要添加执行的方法名
#     suit.addTest(Test_baidu("test_search_key_selenium"))
#     suit.addTest(Test_baidu("test_search_key_unittest"))

#     #使用texttestrunner 执行
#     runner = unittest.TextTestRunner()
#     runner.run(suit)

#     #或者直接调用主函数中的内容
#     # unittest.main()


#2.0
#定义的函数类中的方法很多重复，可以直接把重复的代码进行封装成一个函数，可以直接调用
#1.1
# from selenium import webdriver
# import unittest
# import time

# #定义test类：必须添加TestCase 方法
# class Test_baidu(unittest.TestCase):

#     #使用setup 连接数据库，使用teardown 关闭数据库
#     #调用前置，每执行一次都会执行一次里面内容
#     #每次都执行浏览器的开启和关闭会很耗时： 使用setUpClass可以解决，只执行一次，开启到测试用例结束
#     # def setUp(self):
#         # #驱动浏览器      
#         # self.driver=webdriver.Chrome()
#         # #设置浏览器的url
#         # self.bd_url="http://www.baidu.com"

#     @classmethod
#     def setUpClass(cls):
#         cls.driver=webdriver.Chrome()
#         cls.bd_url="http://www.baidu.com"


#         #定义一个方法存储要查找的key值，封装一些重复的操作
#         #自定义的方法不会跟测试用例一起执行，因为它只执行以test开头的方法民中的方法
#     def search_key(self,baidu_key):
#         self.baidu_key = baidu_key
#         #获取url地址
#         self.driver.get(self.bd_url)
#         #获取元素，定位id
#         self.driver.find_element_by_id("kw").send_keys(baidu_key)
#         #点击click
#         self.driver.find_element_by_id("su").click()

#         time.sleep(1)
#         #定义类：需要执行的测试用例
#     def test_search_key_selenium(self):
#         #设置需要搜索的地址
#         baidu_key="selenium"
#         #调用函数search_key,将参数传入
#         self.search_key(baidu_key)
#         #设置断言
#         self.assertEqual(self.driver.title,baidu_key+"_百度搜索")      
        
#     def test_search_key_unittest(self):

#         baidu_key="unittest"
#         self.search_key(baidu_key)
#         #设置断言
#         self.assertEqual(self.driver.title,baidu_key+"_百度搜索")

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#     # #每执行完一次测试用例的调用都会执行
#     # def tearDown(self):
#     #     self.driver.quit()


#     #只在本地执行，其他函数调用不了
# if __name__ =='__main__':
#     # 使用函数的套件，testsuite
#     suit=unittest.TestSuite()
#     #一次执行一条：需要添加执行的方法名
#     suit.addTest(Test_baidu("test_search_key_selenium"))
#     suit.addTest(Test_baidu("test_search_key_unittest"))

#     #使用texttestrunner 执行
#     runner = unittest.TextTestRunner()
#     runner.run(suit)

#     #或者直接调用主函数中的内容
#     # unittest.main()



#3.0生成测试报告：testhtmlreport
#需要下载第三方库

# from selenium import webdriver
# import unittest
# import time
# #导入更好看的测试报告，更改TestRunner 模块的包
# from unittestreport import TestRunner
# # from TestRunner import HTMLTestRunner

#定义test类：必须添加TestCase 方法

#import unittest from unittestreport import TestRunner 
# # 第一步：加载测试套件 suite1 = unittest.defaultTestLoader.discover(r"xxx\xxx\cases") # 
# 第二步：创建运行对象，传入测试套件 runner = TestRunner(suite1) #通过TestRunner运行
# # 第三步：执行测试 runner.run()

#class TestRunner(): 
# """unittest运行程序""" 
# def __init__(self, suite: unittest.TestSuite, filename="report.html", report_dir=".", title='测试报告', tester='木森', desc="木森执行测试的报告", templates=1 ): 
    # """  
    # 初始化用例运行程序  :param suites: 测试套件  :
    # param filename: 报告文件名  :
    # param report_dir:报告文件的路径  :
    # param title:测试套件标题  :
    # param tester:测试者  :
    # param desc:相关的描述信息  :
    # param templates: 可以通过参数值1或者2，指定报告的样式模板，目前只有两个模板  
    # """ 

# class Test_baidu(unittest.TestCase):
#     """百度测试"""
#     @classmethod
#     def setUpClass(cls):
#         cls.driver=webdriver.Chrome()
#         cls.bd_url="http://www.baidu.com"

#     def search_key(self,baidu_key):
#         self.baidu_key = baidu_key
#         #获取url地址
#         self.driver.get(self.bd_url)
#         #获取元素，定位id
#         self.driver.find_element_by_id("kw").send_keys(baidu_key)
#         #点击click
#         self.driver.find_element_by_id("su").click()

#         time.sleep(1)
#         #定义类：需要执行的测试用例
#     def test_search_key_selenium(self):
#         """ 测试搜索关键字：selenium """
#         #设置需要搜索的地址
#         baidu_key="selenium"
#         #调用函数search_key,将参数传入
#         self.search_key(baidu_key)
#         #设置断言
#         self.assertEqual(self.driver.title,baidu_key+"_百度搜索")      
        
#     def test_search_key_unittest(self):
#         """ 测试搜索关键字：unittest """    
#         baidu_key="unittest"
#         self.search_key(baidu_key)
#         #设置断言
#         self.assertEqual(self.driver.title,baidu_key+"_百度搜索")
    
#     def test_search_key_zahaha(self):
#         """ 测试搜索关键字：哈哈哈哈哈 """
#         baidu_key="哈哈哈哈"
#         self.search_key(baidu_key)
#         #设置断言
#         self.assertEqual(self.driver.title,"hahahaa")    


#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

#     #只在本地执行，其他函数调用不了
# if __name__ =='__main__':

#     # unittest.main()
#     #加上运行路径
#     suits=unittest.defaultTestLoader.discover(".",pattern='sele_u*.py')
#     #加上时间   
#     now_time = time.strftime("%Y-%m-%d %H_%M_%S")

#     #配上模板
#     runner = TestRunner(suits)
#     runner.run()
#     # with open("./files/"+now_time+"report.html",'wb') as f:
#     #     #打开了将数据填进report.html中
#     #     runner = HTMLTestRunner(stream=f,verbosity=1,title="百度搜索",description="win10,百度,谷歌")
#     #     #填入刚刚执行的数据
#     #     runner=TestRunner(suits)
#     #     runner.run()


# #1.0将手动输入的数据，通过数据驱动，将csv内的数据传入：十条用例当做一条执行
# #数据驱动的应用
# import csv
# import codecs
# from itertools import islice
# from selenium import webdriver
# import time
# import unittest
# class Test_baidu(unittest.TestCase):
#     """百度测试"""
#     @classmethod
#     def setUpClass(cls):
#         cls.driver=webdriver.Chrome()
#         cls.bd_url="http://www.baidu.com" 

#     def baidu_key(self,search_key):
#         #接到数据执行
#         self.driver.get(self.bd_url)
#         self.driver.find_element_by_id("kw").send_keys(search_key)
#         self.driver.find_element_by_id("su").click()

#     #需要一个数据,定义一个方法，拿到csv里面的数据
#     #使用这种方式的弊端：虽然csv里面的数据都运行到了，但是他把所有的测试数据当成了一条测试数据，拿到csv里面的数据循环打印
#     #比如十条测试用例中，只有一条是错的，导致了全部执行错误
#     def test_search(self):
#         with codecs.open("baidu_data.csv","r","gbk") as f:
#             data = csv.reader(f)
#             for i in islice(data,1,None):
#                 #拿数据
#                 search_key=i[1]
#                 #通过方法传数据
#                 self.baidu_key(search_key)

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

#     #只在本地执行，其他函数调用不了
# if __name__ =='__main__':

#     unittest.main(verbosity=2)

#2.0改进版
#如何实现将数据一条一条的执行呢
#在开始阶段，循环遍历出所有数据，然后方法中执行用例，一个一个拿数据

# import unittest
# from selenium import webdriver
# import time
# import csv
# from itertools import islice
# import codecs

# # driver = webdriver.Chrome()
# # driver.get("dizhi")
# #定义测试类
# class Test_baidu(unittest.TestCase):
#     #前置条件
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome()
#         cls.bd_url="https://www.baidu.com"
#         #使用数组装所有的数据
#         cls.u_date=[]
#         #读取csv里面的数据
#         with open('baidu_data.csv','r',encoding='gbk') as f:
#             #读数据，csv的内置方法
#             data = csv.reader(f)
#             #循环遍历，去除第一行
#             for i in islice(data,1,None):
#                 #传出数据,添加到外面定义的数组中
#                 cls.u_date.append(i)
        
# #封装方法
#     def search_key(self,search_data):
#         #上面只是拿到了url ，并没有实现使用get的方法调用url
#         self.driver.get(self.bd_url)
#         #定位元素
#         self.driver.find_element_by_id("kw").send_keys(search_data)
#         self.driver.find_element_by_id("su").click()

# #定义test_方法   
#     def test_search_key_selenium(self):
#         self.search_key(self.u_date[0][1])
            
#     def test_search_key_unittest(self):
#         self.search_key(self.u_date[1][1])

#     def test_search_key_hahahahaha(self):
#         self.search_key(self.u_date[2][1])
# #后置条件
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
# #方法执行

# if __name__=='__main__':
#     unittest.main(verbosity=2)


#思考：解决了数据读取的问题；也是叫数据驱动：
#带来了哪些问题呢？？
#读取数据必不可少，执行测试用例，离不开读取数据
#如果需要在csv文件插入数据，可能执行的测试用例对不上，那该咋办
#如果测试数据过多的话，不可能全部放在测试脚本中，同一路径下
#思考，什么是ui 自动化测试
#系统只需要用户输入用户名和密码，和一些关键字，搜索而已
#不需要用户输入大量的 数据

#假设-测试用户发文章的功能，就用到大量数据

#自动化测试的配置------> 数据文件中

#parameterized 参数化库
#实现百度测试
#定义类
# import unittest
# from selenium import webdriver
# import time
# # 实现参数化
# from parameterized import parameterized

# class Tex_baidu(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver=webdriver.Chrome()
#         cls.bg_url="https://www.baidu.com"

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
# #定义方法
#     def search_data(self,baidu_search_data):
#         self.driver.get(self.bg_url)
#         self.driver.find_element_by_id("kw").send_keys(baidu_search_data)
#         self.driver.find_element_by_id("su").click()      
#         time.sleep(2)
    
#     #每个元组都被认为是一条测试用例
#     #case1,case2,case3 为测试用例的名称，
#     #baidu_search_data 对应的是需要测试的数据selenium，unittest，pytest
#     @parameterized.expand([
#         ("case1","selenium"),
#         ("case2","unittest"),
#         ("case3","pytest"),
#     ])
#                 #定位parameterized传入的值：name=case1,baidu_search_data=selenium
#     def test_serach(self,name,baidu_search_data):
#         #将拿到的数据传给自定义的方法：selenium,unittest,pytest    
#         self.search_data(baidu_search_data)
#         #设置断言，比较标题是否相等
#         self.assertEqual(self.driver.title,baidu_search_data+"_百度搜索")

# #执行
# if __name__=='__main__':
#             #使得到测试结果更详细
#     unittest.main(verbosity=2)



#使用DDT(data-driven tests):扩展库  三种方式：(),[],{},装需要用到的数据
#运行使用不同的数据运行一个测试用例
#之前是：一条测试用例对应一条数据/现在一条测试用例对应多条数据

# import unittest
# import time
# from selenium import webdriver
# #扩展库里面的参数：DDT
# from ddt import ddt,data,file_data,unpack
# #定义类
# @ddt
# class Test_baidu(unittest.TestCase):
#     #前置条件
#     @classmethod
#     def setUpClass(cls):
#         #驱动浏览器
#         cls.driver=webdriver.Chrome()
#         #定义调用url
#         cls.bg_url="https://www.baidu.com"       


#     #定义方法
#     def search_data(self,search_key):
#         #获取url
#         self.driver.get(self.bg_url)
#         #执行，获取元素
#         self.driver.find_element_by_id("kw").send_keys(search_key)
#         self.driver.find_element_by_id("su").click()
#         time.sleep(2)
       
#     #参数化使用方式一：元组
#     @data(("case1","selenium"),("case2","unittest"),("case3","pytest"))
#     @unpack
#     def test_search1(self,case,search_key):
#         print('第一种测试用例:',case)
#         self.search_data(search_key)
#         self.assertEqual(self.driver.title,search_key+"_百度搜索")


#     #方法二：列表
#     @data(["case1","selenium"],["case2","unittest"],["case3","pytest"])
#     @unpack
#     def test_search2(self,case,search_key):
#         print('第二中测试用例:',case)
#         self.search_data(search_key)
#         self.assertEqual(self.driver.title,search_key+"_百度搜索")


#     #方法三：字典
#     @data({"search_key":"selenium"},{"search_key":"unittest"},{"search_key":"pytest"})
#     @unpack
#     def test_search3(self,search_key):
#         print('第三种测试用例:',search_key)
#         self.search_data(search_key)
#         self.assertEqual(self.driver.title,search_key+"_百度搜索")


#     #方法四：.json 数据文件参数化
#     #数据文件的参数化：调用sele_unit.json 中的文件
#     #不过.json 文件要和.py 文件放在一起
#     @file_data('sele_unit.json')
#     def test_search4(self,search_key):
#         #.json文件中的所有数据
#         """{
#             "case1":{"search_key":"selenium"},
#             "case2":{"search_key":"unittest"},
#             "case3":{"search_key":"python"}
#             }
#         """
#         print("第四种测试用例：",search_key)
#         #传参
#         self.search_data(search_key)
#         #断言：
#         self.assertEqual(self.driver.title,search_key+"_百度搜索")

#     #方法五：读取yaml 文件数据          ：执行有问题
#     # @file_data('sele_unit.yaml')
#     # def test_search5(self,case):
#     #     search_key = case[0]["search_key"]
#     #     print("第五组测试用例:",search_key)
#     #     #传参
#     #     self.search_data(search_key)
#     #     #断言
#     #     self.assertEqual(self.driver.title,search_key+"_百度搜索")

#     #后置条件
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
# #执行
# if __name__=='__main__':
#     unittest.main(verbosity=2)

#DDT 支持数据文件的参数化
#创建json 文件


#python 自带的发邮件功能
#SMTP：简单邮件传输协议
#发送邮件正文：
# from selenium import webdriver
# import unittest
# import time
# #导入更好看的测试报告，更改TestRunner 模块的包
# # from unittestreport import TestRunner
# from TestRunner import HTMLTestRunner
# import smtplib
# from parameterized import parameterized
# # 定义test类：必须添加TestCase 方法

# # import unittest from unittestreport import TestRunner 
# # 第一步：加载测试套件 suite1 = unittest.defaultTestLoader.discover(r"xxx\xxx\cases") # 
# # 第二步：创建运行对象，传入测试套件 runner = TestRunner(suite1) #通过TestRunner运行
# # 第三步：执行测试 runner.run()

# class Test_baidu(unittest.TestCase):
#     """百度测试"""
#     @classmethod
#     def setUpClass(cls):
#         cls.driver=webdriver.Chrome()
#         cls.bd_url="http://www.baidu.com"

#     def baidu_keys(self,baidu_key):
#         self.baidu_key = baidu_key
#         #获取url地址
#         self.driver.get(self.bd_url)
#         #获取元素，定位id
#         self.driver.find_element_by_id("kw").send_keys(baidu_key)
#         #点击click
#         self.driver.find_element_by_id("su").click()

#         time.sleep(1)

#     #定义一个类装需要搜索的数据
#     @parameterized.expand([
#         ("case1","selenium"),
#         ("case2","unittest"),
#         ("case3","pytest"),
#     ])
#     def test_search(self,name,search_key):
#         self.baidu_keys(search_key)
#         #断言
#         self.assertEqual(self.driver.title,search_key+"_百度搜索")
    
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

#     #只在本地执行，其他函数调用不了
# if __name__ =='__main__':

#     # unittest.main()
#     #加上运行路径
#     suits=unittest.defaultTestLoader.discover(".",pattern='sele_u*.py')
#     #加上时间   
#     now_time = time.strftime("%Y-%m-%d %H_%M_%S")
#     #runner=unittest.TextTestRunner()
#     with open("./files/"+now_time+"report.html",'wb') as f:
#         #打开了将数据填进report.html中
#         runner = HTMLTestRunner(stream=f,verbosity=1,title="百度搜索",description="win10,百度,谷歌")
#         #填入刚刚执行的数据
        
#         runner.run(suits)
    #将刚刚导出来的HTML 文件通过python 发送邮件给需要看报告的人
    #不过现在出现了点问题：
    #发送smtp:
    #出现问题：
    #ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。

    #以下两行
    # smtp=smtplib.SMTP(user="m15960262793@163.com", password="wwt2328..", host="mail.163.com")
    # smtp.sender(to="2382328231@qq.com", attachments=report)

#1. 发送邮件，html 格式
    # import smtplib
    # #邮件正文：
    # #发送邮件
    # connect("地址")
    # login("登入账号，密码")
    # sendmail("发件人，收件人")

#2. 发送带有附件的邮件
    #邮件主题：
    #发送的附件:
    # with open('txt','r') as f:
    #     xx=f.read()
    # MIMEText:定义邮件的正文，格式，编码
    # [content-type]:附属文件类型
    # [content-disposition]:附件文件名
    # MIMEultipart():定义邮件的主题
    #attach:指定文件信息


#简单发邮件的方式:yagmail
import yagmail

#链接邮箱服务器
yag =yagmail.SMTP(user="m15960262793@163.com",password="UHRQWVWZICGDQOKA",host='mail.163.com',smtp_ssl=True)
#邮件正文
contents=["is a bady,heheehe nis as fffsfdf gs","asdfadga adg g0"]
#发送
yag.send('2382328231@qq.com',"subject",contents)