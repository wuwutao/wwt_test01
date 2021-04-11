#设置定位元素
#将所有的元素同意：看用例需求是需要使用哪种定位元素的方法
#page object
#传driver 和 url
class Base_page():
   def __init__(self,driver):
      self.driver = driver
      
   #类似，先设置url 为空:小明的父类（base.py）买的汽车没有装电池，
   #而他的儿子(baidu_page)装了电池,设置了：url="http://www.baidu.com"
   #open:相当于汽车，self.url:相当于电池(子类的电池)，子类设置的url给open汽车来使用
   
   def open(self,url=None):   
      #url 的值肯定等于None,一开始设置为空，所有执行else
      if url is None:
         self.driver.get(self.url)

      else:
         #如果不为空，直接调用该url
         self.driver.get(url)

   def by_id(self,id):
      return self.driver.find_element_by_id(id)

   def by_name(self,name):
      return self.driver.find_element_by_name(name)
  
   def by_class(self,class_name):
      return self.driver.find_element_by_class_name(class_name)
   
   def bg_link_text(self,link_text):
      return self.driver.find_element_by_link_text(link_text)

   def get_title(self,get_title):
      return self.driver.title