'''
#1.0
from unitests import Calc

def test_add():
    #定义变量创建实体，传入a,b 两个参数
    c = Calc(3,5)
    #再定义变量，调用类中的方法
    result =c.jia()
    #设置断言，result 为预期结果，判断结果
    assert result==8,"加法运算失败"

def test_jian():
    c=Calc(8,5)
    result = c.jian()
    assert result==3,"减法运算失败"

def test_chengfa():
    c=Calc(6,6)
    result =c.chengfa()
    assert result==35,"乘法失败"

def test_fa():
    c=Calc(6,2)
    result = c.chu()
    assert result==3,"出发运算失败"

if __name__ =='__main__':
    test_add()
    test_jian()
    test_chengfa()
    test_fa()

'''

#2.0 使用unittest       低配版
#有缺陷： 需要自己设置错误提示信息，一有错就直接报错，停止运行，无法捕获实现测试用例成功和失败数

#定义一个类，需要基继承unitest.testcase
# import unittest
# from unitests import Calc
#                 #调用模块TestCase
# class Test_Calc(unittest.TestCase):
#         #函数名必须以test 开头
#     def test_jiafa(self):
#         c=Calc(4,5)
#         result= c.jia()
#             #比较预期结果和实际结果
#         self.assertEqual(result,9)

#     def test_jianfa(self):
#         c=Calc(9,6)
#         result=c.jian()
#         self.assertEqual(result,10)

#     def test_chengfa(self):
#         c=Calc(5,6)
#         result=c.chengfa()
#         self.assertEqual(result,30)
    
#     def test_chu(self):
#         c=Calc(6,2)
#         result = c.chu()
#         self.assertEqual(result,3)


# if __name__=='__main__':
#     unittest.main()
#定义四个方法
#设置断言：实际结果和预期结果进行对比，判断执行这条测试用例对错，成功与否

#需要理解四个概念：

#TestCase:测试类需要继承该基类，可以创建新的测试用例

#Test Suite:测试套件：测试用例和测试套件相结合

#TestRunner:用于协调测试执行，向用户提供结果,    

#Test Fixture:用于建立一个或者多个测试环境准备，创建临时或代理数据库
#前置动作 /后置动作   
#setUp()/tearDown(),setUpClass()/tearDownClass()

# #高配版 
# import unittest
# from unitests import Calc
#                 #调用模块TestCase
# class Test_Calc(unittest.TestCase):
#         #函数名必须以test 开头

#     #Test Fixture
#     #测试用例的前置条件     每次执行一条用例都会执行
#     def setUp(self):
#         print(" test start...")
#     #测试用例的后置条件
#     def tearDown(self):
#         print(" test stop")

#     def test_jiafa(self):
#         c=Calc(4,5)
#         result= c.jia()
#             #比较预期结果和实际结果
#         self.assertEqual(result,9)
#     def test_jianfa(self):
#         c=Calc(9,6)
#         result=c.jian()
#         self.assertEqual(result,3)
#     def test_chengfa(self):
#         c=Calc(5,6)
#         result=c.chengfa()
#         self.assertEqual(result,30)  
#     def test_chu(self):
#         c=Calc(6,2)
#         result = c.chu()
#         self.assertEqual(result,3)


# if __name__=='__main__':
#     #TestSuite 创建测试套件suit
#     suit=unittest.TestSuite()
#     #添加需要进行测试的方法,通过TestSuite 里面的addTest添加测试用例
#     suit.addTest(Test_Calc("test_jiafa"))
#     suit.addTest(Test_Calc("test_jianfa"))
#     suit.addTest(Test_Calc("test_chengfa"))
#     suit.addTest(Test_Calc("test_chu"))

#     #创建测试运行器 texttestrunner
#     runner = unittest.TextTestRunner()
#     runner.run(suit)



#断言的用法:
#assertEqual,assertNotEqual

import unittest

class Test_test(unittest.TestCase):

    def test_a(self):
        self.assertEqual(2,2)
        # self.assertIsNot("wode")
        self.assertIs("python","python")

    def test_in(self):
        self.assertIn("hello","hello waa")
    
    def test_true(self):
        self.assertTrue(True)

if __name__=='__main__':

    unittest.main()