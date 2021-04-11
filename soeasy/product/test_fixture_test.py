
class Test_wwt: 

    def  test_01(self,fixture_po):
        print("\n商品管理权限")

            #对装饰器指定函数功能，在执行test02之前，会执行fixture_my这个函数中的内容
    def  test_02(self,fixture_po):      
        print("\nn商品管理权限2")     #打印request.param 中所有的值