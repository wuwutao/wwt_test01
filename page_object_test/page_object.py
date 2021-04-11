

class Baidu_page():

    def __init__(self,driver):
        self.driver = driver
    
    #设置需要返回的元素各个方法
    #使用page object:便于控制元素的操作，分离
    def by_id(self):
        
        return self.driver