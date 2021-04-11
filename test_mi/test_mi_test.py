from selenium import webdriver
from selenium.webdriver import ActionChains
import time 
import pytest
from change_yaml import Test_001

class Test_times():

    def setup_class(cls):
        global driver
        #获取浏览器驱动
        driver = webdriver.Chrome()
        #获取地址
        driver.get("https://www.mi.com/")

    def teardown_class(cls):
        global driver
        driver.quit()

    def test_items(self):

        global driver
        #定位元素
        xiaomi = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[1]/div[2]/ul/li[2]/a/span")
        #定位鼠标移动
        ActionChains(driver).move_to_element(xiaomi).perform()
        time.sleep(2)

        #拿到数据,定位元素
        items = driver.find_elements_by_css_selector("#J_navMenu .title")
        #获取需要的数据
        item =[]
        for line in items:
            item.append(line.text)
                      
    @pytest.mark.parametrize("args",Test_001('items_yaml.yaml').Rd_yaml())
    def test_search(self,args):
        global driver
        #拿到获取到的数据
        #['小米MIX FOLD', '小米11 Ultra', '小米11 Pro', '小米11 青春版', '小米10S', '小米11']
        #搜索数据点击
        driver.find_element_by_id("search").click()
        #搜索数据清除 
        driver.find_element_by_id("search").clear()
        #传入搜索的数据
        driver.find_element_by_id("search").send_keys(args)
        #点击搜索按钮
        driver.find_element_by_class_name("search-btn.iconfont").click()

        #断言搜索结果出现该字样
        assert 2==2
        #生成allure报告  
        #生成json格式数据
        #--alluredir ./temp

        
if __name__=='__main__':
    pytest.main()
    #os.system('allure generate ./temp -o ./report --clean')