import unittest
from selenium import webdriver
import time
import csv
from itertools import islice
import codecs

# driver = webdriver.Chrome()
# driver.get("dizhi")
#定义测试类
class Test_baidu(unittest.TestCase):
    #前置条件
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.bd_url="https://www.baidu.com"
        #使用数组装所有的数据
        cls.u_date=[]
        #读取csv里面的数据
        with open('mukewang_data.csv','r',encoding='gbk') as f:
            #读数据，csv的内置方法
            data = csv.reader(f)
            #循环遍历，去除第一行
            for i in islice(data,1,None):
                #传出数据,添加到外面定义的数组中
                cls.u_date.append(i)
        
#封装方法
    def search_key(self,search_data):
        #上面只是拿到了url ，并没有实现使用get的方法调用url
        self.driver.get(self.bd_url)
        #定位元素
        self.driver.find_element_by_id("kw").send_keys(search_data)
        self.driver.find_element_by_id("su").click()

#定义test_方法   
    def test_search_key_selenium(self):
        self.search_key(self.u_date[0][1])
            
    def test_search_key_unittest(self):
        self.search_key(self.u_date[1][1])

    def test_search_key_hahahahaha(self):
        self.search_key(self.u_date[2][1])
#后置条件
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
#方法执行

if __name__=='__main__':
    unittest.main(verbosity=2)

    #将执行完的report 使用文件装起来，存储为：htmltestreporter
    