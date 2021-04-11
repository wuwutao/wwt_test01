from   mukewang_page import Mukewang_search
import unittest
from selenium import webdriver
import time
from ddt import ddt,data,file_data,unpack
#测试调用类

#定义测试类
class  Test_muke(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
    
        #需要小写test
    def test_data(self):
        page = Mukewang_search(self.driver)
        #拿到url
        page.open()
        #首页输入查找内容
        page.search_input("selenium")
        #电影查找方法
        page.search_button()
        #回退到首页
        self.driver.back()
        #点击登入页面
        time.sleep(2)
        
        page.login_button()

    @classmethod 
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':

    unittest.main(verbosity=2)