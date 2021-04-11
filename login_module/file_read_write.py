import unittest
from selenium import webdriver
from ddt import ddt,data,file_data,unpack
import yaml
#实现功能文件的读取

#浏览器驱动
@ddt
class Test_file(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     pass
        # self.driver = driver
        # self.driver = webdriver.Chrome()

    # def Readfile():
    #     file_data = []
    #     file = open("./file_text.txt","r",encoding="gbk")
    #     for line in file.readlines:
    #         date =file.append(line.strip("\n").split(","))   

    #     return date    

    @file_data("file.yml")
    @unpack
    def test_01(self,**kwargs):
        print(kwargs.get('name')) 
        print("--------")
    # @classmethod
    # def tearDownClass(cls):
    #     pass
if __name__=='__main__':
    unittest.main()
#获取get
#定义一个方法，封装读取的文件
#使用ddt,对文件的调用
