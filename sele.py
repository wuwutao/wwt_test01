"""
# from selenium import webdriver

# #调用web下的Chrome()的类，赋值给dricer
# driver=webdriver.Chrome()
# #调用Chrome 中的get方法去访问百度地址
# driver.get("https://www.baidu.com")

# driver.set_window_size(200,400)
# driver.maximize_window()
# driver.quit()
# driver.find_elements_by_css_selector(".s_ipt").send_keys("什么东西")
# driver.find_elements_by_css_selector(".s_btn").click()

#定位页面元素，进行输入
# dricer.find_element_by_id("kw").send_keys("python菜鸟驿站")
#和单击操作
                        #实现定位class ，进行操作
# driver.find_element_by_class_name("s_ipt").send_keys("斗罗大陆")
# driver.find_element_by_class_name("bg s_btn").click()

# driver.find_element_by_id("kw").send_keys("我爱你")
#使用绝对路径，定位元素，属性，在没有id/name 的情况下
#driver.find_element_by_xpath("/html/body/div/div/div[5]/div/div/form/span[2]/input").click()

# driver.find_element_by_xpath("//input[@id='su']").click()

#<em class="">我爱你</em>
#<a href="http://map.baidu.com" target="_blank" class="mnav c-font-normal c-color-t">地图</a>
# driver.find_element_by_xpath("//*[@class='mnav c-font-normal c-color-t']").click()


#driver.find_element_by_class_name("s-tab-item s-tab-video").click()
# driver.find_element_by_link_text("资讯").click()
# driver.find_element_by_class_name("c-img-border c-img-radius-large").click()

# driver.find_element_by_class_name("fluid-item-link").click()
# driver.find_element_by_id("search_input").send_keys("王牌对王牌")
# driver.find_element_by_class_name("search-btn-text").click()


from selenium import webdriver

driver=webdriver.Chrome()

url_baidu="https://www.baidu.com"
driver.get(url_baidu)

second_web="http://news.baidu.com"
driver.get(second_web)

print("back to %s"%(url_baidu)) 
driver.back()

print("back to %s"%(second_web))
driver.forward()
#界面刷新 refresh
driver.refresh()
driver.refresh()
driver.refresh()
# driver.get("https://www.baidu.com")
driver.quit()


import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
x =driver.find_element_by_id('kw')
x.send_keys("selenium")
x.submit()
# driver.find_element_by_id('su').click()

time.sleep(10)
driver.quit()

import time

from selenium import webdriver

drivers = webdriver.Chrome()

drivers.get("https://www.baidu.com")

size=drivers.find_element_by_id("kw").size
print(size)

text=drivers.find_element_by_class_name("s-bottom-layer-content").text
print(text)

time.sleep(10)
drivers.quit()


#鼠标操作：
from selenium import webdriver
from selenium.webdriver import ActionChains

drivers=webdriver.Chrome()
drivers.get("https://www.baidu.com")

drivers.maximize_window()
abs =drivers.find_element_by_link_text("更多")
ActionChains(drivers).move_to_element(abs).perform()

#键盘操作
import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys


drs = webdriver.Chrome()
drs.get("https://www.baidu.com")

drs.find_element_by_id("kw").send_keys("我真的好想能够回到过去")
drs.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)      #回退一个字母   
drs.find_element_by_id("kw").send_keys(Keys.BACK_SPACE) 

# drs.find_element_by_id("kw").send_keys("你身边")
# drs.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")    #全选
# drs.find_element_by_id("kw").send_keys(Keys.CLEAR)          #清除
# drs.find_element_by_id("kw").send_keys("加油加油")      
drs.find_element_by_id("su").send_keys(Keys.ENTER)

time.sleep(10)

drs.quit()


#获取验证信息
#title,text,current_url

from selenium import webdriver
import time

ds=webdriver.Chrome()
ds.get("https://www.baidu.com")
print("=====================")

title = ds.title
print("title"+title)

n_url=ds.current_url
print("url:"+n_url)

ds.find_element_by_id("kw").send_keys("selenium")
ds.find_element_by_id("su").click()

time.sleep(3)

print("-----------------")
title=ds.title
print("title:"+title)

sn_url=ds.current_url
print("sn_url:"+sn_url)

num=ds.find_element_by_class_name("nums").text
print("num:"+num)

ds.quit()


#显示等待：

import time
from selenium import webdriver
from selenium.webdriver.common.by import By             #使用By的方式来定位id
from selenium.webdriver.support.ui import WebDriverWait     #webdriverwait 是driverwait 提供的方法
from selenium.webdriver.support import expected_conditions as EX    #导入设置预期结果

dirr=webdriver.Chrome()
dirr.get("https://www.baidu.com")

ele=WebDriverWait(dirr,5,0.5).until(

    #判断是否可见
    EX.visibility_of_element_located((By.ID,"kw"))
)

ele.send_keys("哈哈哈哈")

time.sleep(6)
dirr.quit()



import time 
from selenium import webdriver

dss=webdriver.Chrome()
dss.get("https://www.baidu.com")

print(time.ctime())

for i in range(10):
    try:    
        #如果发现了定位的id,说明可见，所以直接执行break
        cs=dss.find_element_by_id("kw")
        if cs.is_displayed():
            break
        else:
            pass
    except:
        pass
    time.sleep(1)
else:
    print("time out")

print(time.ctime())
dss.quit()



#隐式等待
from selenium import webdriver 
from time import ctime
from selenium.common.exceptions import NoSuchElementException

dicts=webdriver.Firefox()
dicts.implicitly_wait(10)
dicts.get("https://www.baidu.com")

try:
    print(ctime())
    dicts.find_element_by_id("kw22").send_keys("selenium")
except NoSuchElementException as e:
    print(e)

finally:
    print(ctime())
    dicts.quit()    
    


#定位一组元组：
from time import sleep
from selenium import webdriver

dx=webdriver.Chrome()
dx.get("https://www.baidu.com")

dx.find_element_by_id("kw").send_keys("selenium")
dx.find_element_by_id("su").click()

sleep(3)

txt = dx.find_elements_by_xpath("//div[@tpl='se_com_default']/h3/a")

# print(len(txt))

for i in txt:
    print(i.text)

dx.quit()


#多表单切换
# 导包
from selenium import webdriver
import time
# 创建一个浏览器对象
driver = webdriver.Chrome()
# 默认浏览器全屏
driver.maximize_window()
# 访问163邮箱
driver.get('https://www.126.com/')
time.sleep(2)

login=driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to_frame(login)

driver.find_element_by_name("email").send_keys("15960262793")
driver.find_element_by_name("password").send_keys("12345678")
time.sleep(2)

driver.find_element_by_id("dologin").click()

time.sleep(5)
driver.quit()



#实现多窗口之间的切换
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://i.mooc.ndnu.edu.cn/space/index?t=1617454770371")
a1=driver.current_window_handle     #保存句柄

driver.find_element_by_xpath("//div[@class='ulDiv']/ul/li[6]/div/a").click()
for handle in driver.window_handles:
    #切换到对应的脚本
    driver.switch_to_window(handle)
    if "学习进度" in driver.title:
        break

driver.find_element_by_class_name("knowledgeJobCount").click()

for handle in driver.window_handles:
    #切换到对应的脚本
    driver.switch_to_window(handle)
    if "学生学习页面" in driver.title:
        break

driver.find_element_by_id("video_html5_api").click()

time.sleep(720)

driver.find_element_by_class_name("orientationright").click

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

#设置句柄
search_window=driver.current_window_handle

driver.find_element_by_link_text("登录").click()
time.sleep(2)
driver.find_element_by_link_text("立即注册").click()

for handle in driver.window_handles:
    driver.switch_to_window(handle)

    if "注册百度账号" in driver.title:
        break

driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("wwt")
driver.find_element_by_id("TANGRAM__PSP_4__userName").click()
driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("15960262793")
driver.find_element_by_id("TANGRAM__PSP_4__phone").click()
driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("123456789")
driver.find_element_by_id("TANGRAM__PSP_4__phone").click()
driver.find_element_by_id("TANGRAM__PSP_4__verifyCode").send_keys("1234")
driver.find_element_by_id("TANGRAM__PSP_4__verifyCode").click()

driver.find_element_by_name("isAgree").click() 

#driver.find_element_by_id("login_btn").click()
# driver.find_element_by_id("TANGRAM__PSP_4__submit").click()

# driver.find_element_by_class_name("tang-pass-footerBarULogin pass-link").click()

time.sleep(2)

driver.find_element_by_class_name("pass-button pass-button-blue continue").click()

for handle in driver.window_handles:
    driver.switch_to_window(handle)

    if "登录百度账号" in driver.title:
        break

driver.find_element_by_class_name("tang-pass-footerBarULogin pass-link").click()

# driver.find_element_by_id("TANGRAM__PSP_3__userName").clear()
# driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys("15960262793")

driver.find_element_by_id("TANGRAM__PSP_3__password").click()
driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys("wwt2328..")

driver.find_element_by_id("TANGRAM__PSP_3__submit").click()



import time 
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

 #找到页面元素
ele = driver.find_element_by_xpath('//div[@id="u1"]//a[text()="设置"]')
#实例化鼠标对象
action = ActionChains(driver)
#鼠标移动到该元素上，鼠标悬停,等待下拉框元素可见
action.move_to_element(ele).perform()

WebDriverWait(driver,1).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="bdpfmenu"]//a[1]')))
driver.find_element_by_xpath('//a[text()="搜索设置"]').click()
time.sleep(2)

driver.find_elements_by_class_name("prefpanelgo setting-btn c-btn c-btn-primary").click()

alert=driver.switch_to_alert

alert_text=alert.text
print(alert)
alert.accept()



#下拉框处理

import time 
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.maximize_window()
link=driver.find_element_by_link_text("设置").click()
driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)

sel=driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value('20')  



#上传文件的测试接口
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = driver.find_element_by_id('file')
upload.send_keys('d:\\baidu.py')  # send_keys
print(upload.get_attribute('value'))  # check value

driver.quit()


#设置下载文件

#firefox
from selenium import webdriver
import os

fb=webdriver.FirefoxProfile()
#:0:下载到桌面，1：表示默认路径,2:自定义路径
fb.set_preference("browser.download.folderList",2)
#os.getcwd： 返回当前目录,下载到一起
fb.set_preference("browser.download.dir",os.getcwd())
#对所有类型进行不在弹框显示，因为一般下载都会对你进行弹窗，再点击下载
fb.set_preference("browser.helperApps.neverAsk.saveToDisk","binary/octet-stream")

driver=webdriver.Firefox(firefox_profile=fb)
driver.get("https://pypi.org/project/selenium/#files")

driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()


#chrome:下载
from selenium import webdriver
import os

options=webdriver.ChromeOptions()
prefs={'profile.default_content_settings.popups':0,
        'download.default_directory':os.getcwd()}
options.add_experimental_option('prefs', prefs)

driver=webdriver.ChromeOptions(chrome_options=options)
driver.get("https://pypi.org/project/selenium/#files")

driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()



#操作cookie

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")


driver.add_cookie({'name':'wwt','value':'123456'})

for cookie in driver.get_cookies():
    print("%s-->%s" % (cookie['name'],cookie['value']))



 #调用javascript
 
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#设置大小框
driver.set_window_size(800,600)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

js="window.scrollTo(300,500);"
driver.execute_script(js)



 #处理html 视频播放

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://videojs.com/")

video=driver.find_element_by_xpath('//*[@id="preview-player_html5_api"]')
url=driver.execute_script("return arguments[0].currentSrc;",video)
print(url+"----------")

print("statrt"+"----------s")

driver.execute_script("arguments[0].play()",video)

time.sleep(20)

print("pause")
driver.execute_script("arguments[0].pause()",video)

time.sleep(3)
driver.quit() 

#设置滑动解锁
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
#导入错误的类型，进行判断
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.get("https://www.helloweba.net/demo/2017/unlock/")

slide=driver.find_elements_by_class_name("slide-to-unlock-handle")[0]

#监听事件：获取鼠标
action = ActionChains(driver)
#单击方块的slide，获取
action.click_and_hold(slide).perform()

for i in range(100):
    try:
        #移动的x,y值
        action.move_by_offset(10,0).perform()

    except UnexpectedAlertPresentException:
        break

    #重置action 
    action.reset_actions()
    time.sleep(0.1)

#打印滑动成功信息
success_text=driver.switch_to_alert.text
print(success_text)


#操作滚动时间
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.jq22.com/yanshi4976")

driver.switch_to_frame("iframe")
driver.find_element_by_id("appDateTime").click()

# #定位要滑动到的时间年月日

dwwos =driver.find_elements_by_class_name('dwwo')
year=dwwos[0]
mon=dwwos[1]
day=dwwos[2]

action =webdriver.TouchActions(driver)
action.scroll_from_element(year,0,5).perform()
action.scroll_from_element(mon,0,10).perform()
action.scroll_from_element(day,0,30).perform()

driver.find_element_by_link_text("确定").click()

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#获取浏览器页面截图，保存到指定位置
driver.save_screenshot("./files/1.png")

"""


#疫情排查傻瓜式脚本
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("http://2019-ncov.ndnulife.com/#/home?session=oVlZUw_w6z4Ej2WYVW47xrni6x5Q&t=1617377059.38637")

time.sleep(1)
# /html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[18]/div[1]/div[2]/div
# alert = driver.switch_to.alert
# alert.dismiss()

#取消选择框
driver.find_element_by_class_name("van-button.van-button--default.van-button--large.van-dialog__confirm").click()

#点击温度
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[4]/div[1]/span[3]/button").click()

#设置具体温度

# /html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[4]/div[1]/span[3]/div[2]/div/div[2]/div[1]/ul/li[6]
# /html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[4]/div[1]/span[3]/div[2]/div/div[2]/div[1]/ul/li[2]
# /html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[4]/div[1]/span[3]/div[2]/div/div[2]/div[1]
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[4]/div[1]/span[3]/div[2]/div/div[2]/div[1]").click()
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[4]/div[1]/span[3]/div[2]/div/div[2]/div[1]").click()
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[4]/div[1]/span[3]/div[2]/div/div[2]/div[1]").click()
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[4]/div[1]/span[3]/div[2]/div/div[2]/div[1]/ul/li[4]/div").click()

#确认提交
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[4]/div[1]/span[3]/div[2]/div/div[1]/button[2]").click()


driver.find_element_by_xpath("//div[@class='el-card__body']/div/div[18]/div/div[2]/div").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[18]/div[2]/div[2]/div").click()

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[19]/div[2]/div/div[2]/div[1]/span").click()

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/main/div/div/div/div[26]/button[4]").click()



# action.click_and_hold(slide).perform()

# driver.find_element_by_link_text("确认").click()
# driver.find_element_by_class_name("van-button__content").click()

