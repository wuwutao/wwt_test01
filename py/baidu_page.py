#设置调用的方法
#调用元素：元素又另外定义方法：by_id,ny_name...
from base import Base_page


class Baidu_page(Base_page):

  url="https://www.baidu.com"

  def search_input(self,search_keys):
  	      #子类调用方便：find_element_by_id	   方法名：by_id
     self.by_id("kw").send_keys(search_keys)

  def search_button(self):
     self.by_id("su").click()


 


