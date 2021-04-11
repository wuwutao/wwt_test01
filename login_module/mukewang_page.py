import time
from base_page import Class_page
#执行查找定位元素方法

class  Mukewang_search(Class_page):
    
    url="https://www.imooc.com/"
    # url ="https://www.baidu.com"

    #点击输入
    def search_input(self,search_keys):
        self.by_class_name("search-input").send_keys(search_keys)
        time.sleep(2)
    
    #点击搜索
    def search_button(self):
        self.by_class_name("imv2-search2").click()
        time.sleep(2)

    #点击登录
    def login_button(self):
        self.driver.find_element_by_id("js-signin-btn").click()

        # xa-emailOrPhone ipt ipt-email js-own-name
        self.driver.find_element_by_xpath("/html/body/div[9]")
        self.driver.find_element_by_class_name("xa-emailOrPhone.ipt.ipt-email.js-own-name").click()
        self.driver.find_element_by_class_name("xa-emailOrPhone.ipt.ipt-email.js-own-name").send_keys("123456")

        time.sleep(30)

    #点击输入手机号
