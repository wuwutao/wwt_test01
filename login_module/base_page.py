
#封装定位元素的类

class Class_page():

    def __init__(self,driver):
        self.driver = driver
    #父类没有设置url，就可以直接到子类中拿url
    def open(self,url=None):
        if url is None:
            self.driver.get(self.url)

        else:
            self.driver.get(url)

    def by_id(self,id):   
        return self.driver.find_element_by_id(id)

    def by_class_name(self,class_name):   
        return self.driver.find_element_by_class_name(class_name)
    
    def by_name(self,name):
        return self.driver.find_element_by_name(name)

    def by_path(self,path_name):
        return self.driver.find_element_by_xpath(path_name)
    
    