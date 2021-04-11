
#缺点，元素写死在方法中，如果出现定位的元素发生变化，不好做更改
#所有引入pageobject 很好的解决这个问题：test_op_pro02.py
#页面对象化

#1.页面对象化：看有几个页面，定义几个类
#2.操作函数化：每个类中封装方法，函数   如果需要跳转到另一个页面，使用return 返回对象



#首页
class IndexPage():
    def __init__(self,driver):
            self.driver = driver
            driver.get("https://www.mi.com/")
    #定义方法，点击首页进入登录页
    def to_login(self):
        
        #点击登录页
        driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div[1]/div[3]/a[1]").click()
        driver.find_element_by_class_name("btn.btn-primary").click()
        time.sleep(2)

        #返回登录页的一个对象给登录页LoginPage
        #涉及到页面跳转，就返回一个对象，看你需要返回到哪个
        return LoginPage(self.driver)
    
    #搜索页面也是在首页中一起进行的，可以直接放在登录上一起执行操作
    def search_items(self,items="耳机"):
        
        self.driver.find_element_by_id("search").send_keys(items+'\n')
        #点击完，到商品详情页面  返回对象
        return GooditemsPage(self.driver)
        #因为一点击就跳转到商品详情页了,不是登录页中的功能
        #driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/a/img").click()

#登录页
class LoginPage():
    def __init__(self,driver):
            self.driver = driver

    def login(self,username,password):
        #输入账号密码
        self.driver.find_element_by_id("username").click()
        self.driver.find_element_by_id("username").send_keys(username)

        self.driver.find_element_by_id("pwd").click()
        self.driver.find_element_by_id("pwd").send_keys(password)

        #点击登录按钮
        self.driver.find_element_by_id("login-button").click()

        #返回首页对象
        #涉及到页面跳转，就返回一个对象，看你需要返回到哪个
        #不加的话，需要拿着这个对象进行操作更麻烦
        return IndexPage(self.driver)   
#商品页
class GooditemsPage():
    def __init__(self,driver):
            self.driver = driver
    #查找耳机
    def goods_items(self):
        #点击商品查找
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/a/img").click()
        
        #判断页面是否跳转
        for handle in driver.window_handles:
            self.driver.switch_to_window(handle)

            #判断标题，判断当前窗口是否相等
            if "小米真无线" in driver.title :
                #已经切换页面
                return ItemPage(self.driver)          

#点击后，商品详情页
class ItemPage():
    def __init__(self,driver):
            self.driver = driver
    
    def pick_shop_car(self):

        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div[2]/div[7]/div[1]/a").click()

        #判断是否发生页面跳转
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)

            if "成功加入购物车" in driver.title :
                return ShopCarPage(self.driver)

#购物车页面
class ShopCarPage():
    def __init__(self,driver):
        self.driver = driver

    #设置断言，检查信息
    def check_message(self):
        res = self.driver.find_element_by_class_name("goods-info").text
        #断言
        assert "小米真无线" in res

if __name__=='__main__':
    #页面的初始化
    from selenium import webdriver
    import time
    #获取浏览器驱动
    driver = webdriver.Chrome()
    #设置隐式等到时间
    driver.implicitly_wait(10)
    #获取地址
    driver.get("https://www.mi.com/")

    #定位到登录页---登录---首页---搜索商品--搜索页面---选择商品---商品详情页---添加购物车---购物车---检查

    indexPage=IndexPage(driver)

    loginPage =indexPage.to_login()

    #登录
    indexPage = loginPage.login("15960262793","wwt2328..")

    #搜索商品
    gooditemsPage =indexPage.search_items()

    itemPage=gooditemsPage.goods_items()

    shopCarPage=itemPage.pick_shop_car()

    shopCarPage.check_message()
