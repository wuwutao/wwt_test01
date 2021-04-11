from selenium import webdriver
from selenium.webdriver import ActionChains
import time 
import pytest
import os
import allure

#实现将封装的数据,传递给测试用例，一个一个执行，判断，搜索内容是否相匹配
#parametrize/allure 生成测试报告,
search_list=['小米', '小米11 Ultra', '小米11 Pro', '小米11 青春版', '小米10S', '小米11']
class Test_times():
    
    #fixture 前置后置对象，scope,autouse,ids,name,params
    @pytest.fixture(scope='module',autouse=True)
    def before_class(cls):
        global driver
        #获取浏览器驱动
        driver = webdriver.Chrome()
        #获取地址
        driver.get("https://www.mi.com/")
        yield
        cls.after_class()
    def after_class(cls):
        global driver
        driver.quit()

    @allure.feature("搜索框")
    @allure.story("热门产品搜索")
    @pytest.mark.parametrize("args",search_list)
    def test_items(self,args):
        global search_list    
        global driver

        driver.find_element_by_id("search").click()
        driver.find_element_by_id("search").clear()
        driver.find_element_by_id("search").send_keys(args)
        #search-btn iconfont
        driver.find_element_by_class_name("search-btn.iconfont").click()

        #获取到所有需要产品的title
        a = driver.find_elements_by_css_selector(".goods-list .title")
            
        items =[it.text for it in a]
        assert 2==2
        # assert (args,items)


    @allure.feature("搜索框")
    @allure.story("常规产品搜索")
    def test_search_goods(self):
        print("常规搜索")
if __name__=='__main__':
    pytest.main(['vs','--alluredir ./temp'])
    os.system('allure generate ./temp -o ./report --clean')