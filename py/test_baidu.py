import unittest
from selenium import webdriver
# from baidu_page import Baidu_page
from op_ts import Baidu_pages
import time

class Test_baidu(unittest.TestCase):
   
  @classmethod
  def setUpClass(cls):
    #浏览器驱动程序
    cls.driver=webdriver.Chrome()
  
  @classmethod
  def tearDown(cls):
    #结束退出，最后执行
    cls.driver.quit()
  
  #操作方法一：
  # def test_searth(self):
 	
  #   #设置get,调用标签类，传入一个driver过去
  #   #拿到Baidu_page 用一个变量装着，向baidu_page 传一个driver,需要用到哪个浏览器的类，传到数据驱动
  #   page=Baidu_page(self.driver)      
  #    #调用类中的open方法：判断url
  #   page.open()     #这个page就类似于driver
  #    #查找元素
  #   #设置需要查找的值:
  #   page.search_input("selenium")   #调用需要执行的方法，查找的内容,将selenium 传入search_keys
  #                                   #def search_input(self,search_keys):
  #                                   #self.by_id("kw").send_keys(search_keys)
  #                                   #调用了by_id:他会去他的父类中base找一个叫by_id 的方法
  #                                   #传入了一个id的key值
  #   page.search_button()         
  #   time.sleep(2)                
  #    #设置断言
    
  #   self.assertEqual(self.driver.title,"selenium_百度搜索")


  #操作方法二:  
    #使用opium 重写 baidu_page 的方法
  def test_searth2(self):
    #获取类的driver
    page = Baidu_page(self.driver)
    #该方法是由Page类提供
    page.get("https://www.baidu.com")
    #调用查找元素的方法
    page.search_input("selenium")
    page.search_button.click()
    time.sleep(2)
    #设置断言
    self.assertEqual(self.driver.title,"selenium_百度搜索")

if __name__=='__main__':

  unittest.main(verbosity=2)