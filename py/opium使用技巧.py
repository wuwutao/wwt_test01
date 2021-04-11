

from poium import Page,PageElement

#支持8种定位方法
class SomePage(Page):

	#方法名 = 需要查找的id	 如果调用的话：测试用例中调用：self.方法名()
	elmemnet_id = PageElement(id = 'id')		# eg: id="kw"
	elmemnet_name = PageElement(name = 'name')
	elmemnet_class = PageElement(class_name = 'name')
	elmemnet_tag = PageElement(tag='input')
	elmemnet_link_text = PageElement(link_text ='百度搜索')
    elmemnet_partial_link_text = PageElement(partial_link_text= '搜索')
    elmemnet_xpath = PageElement(xpath = '//*[class="wwt"]')
    elmemnet_css = PageElement(css='#id')




#设置元素超时时间:
class Baidu_page(Page):
								#默认超时时间为10
	ele = PageElement(id="kw",timeout=5)
	ele = PageElement(id="kw",timeout=30)


#设置元素描述：describe 注释：并无实际意义，增加可读性
#如果测试用例过多的话，需要添加注释来增加可读性

from poium import Page,PageElements

class Baidu_page(Page):
								#默认超时时间为10,自行设置
	username = PageElement(css="#login_name",timeout=5，describe="注释说明，用户名")
	password = PageElement(css="#login_pass",timeout=5，describe="注释说明，密码")

#定位一组数据:PageElements
