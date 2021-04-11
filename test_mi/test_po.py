from selenium import webdriver
from selenium.webdriver import ActionChains
import time 

#实现将封装的数据,传递给测试用例，一个一个执行，判断，搜索内容是否相匹配
#parametrize/allure 生成测试报告,


class Test_times():

    @classmethod
    def setup_class(cls):
        global driver
        #获取浏览器驱动
        driver = webdriver.Chrome()
        #设置隐式等到时间
        driver.implicitly_wait(10)
        #获取地址
        driver.get("https://www.mi.com/")

    @classmethod
    def teardown_class(cls):
        global driver
        #driver.quit()
    def test_01(self):
        global driver
        #.J_siteUserInfo
        driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div[1]/div[3]/a[1]").click()
        #btn btn-primary
        time.sleep(2)
        driver.find_element_by_class_name("btn.btn-primary").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").send_keys("15960262793")

        driver.find_element_by_id("pwd").click()
        driver.find_element_by_id("pwd").send_keys("wwt2328..")

        #点击登录按钮
        driver.find_element_by_id("login-button").click()

        # new_web01 = current_windows_handle()
        #定位到搜索框
        time.sleep(2)
        driver.find_element_by_id("search").send_keys("耳机\n")

        time.sleep(2)
        #选中第一个商品，添加购物车:耳机
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/a/img").click()

        #出现页面跳转
        for handle in driver.window_handles:
            driver.switch_to_window(handle)

            #判断标题，判断当前窗口是否相等
            if "小米真无线" in driver.title :
                break
            
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div[2]/div[7]/div[1]/a").click()

        for handle in driver.window_handles:
            driver.switch_to_window(handle)

            if "成功加入购物车" in driver.title :
                break

if __name__=='__main__':
    pytest.main(['vs'])
    # os.system('allure generate ./temp -o ./report --clean')