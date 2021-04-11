import unittest
from selenium import webdriver
import time

# driver = webdriver.Chrome()
# driver.get("dizhi")
#定义测试类
class Test_baidu(unittest.TestCase):
    #前置条件
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.bd_url="https://www.imooc.com/"

    
    def test_001(self):
        self.driver.get(self.bd_url)
        
        time.sleep(5)
        # self.driver.find_element_by_xpath("/html/body/div[9]")

        self.driver.find_element_by_id("js-signin-btn").click()

        self.driver.find_element_by_xpath("/html/body/div[9]")
        
        self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div/form/div[5]/input").click()
        # # xa-emailOrPhone ipt ipt-email js-own-name
        # x1 =self.driver.find_element_by_xpath("/html/body/div[9]")
        # x2 = x1.find_element_by_xpath("/html/body/div[9]/div[2]/div/form/div[1]/input").click()
        # self.driver.find_element_by_class_name("xa-emailOrPhone.ipt.ipt-email.js-own-name").send_keys("123456")

    @classmethod
    def tearDownClass(cls):

        pass
#方法执行

if __name__=='__main__':
    unittest.main(verbosity=2)

    #将执行完的report 使用文件装起来，存储为：htmltestreporter
    