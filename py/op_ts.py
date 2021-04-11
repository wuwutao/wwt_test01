#使用opium 重写了调用执行查找元素的方法

import poium
# from base import Base_page
from poium import Page,PageElement
class Baidu_pages(Page):

	search_input = PageElement(id="kw")
	search_button = PageElement(id="su")

