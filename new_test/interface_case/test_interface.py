import time
import pytest

class Test_interface():

    def setup_class(cls):
        print("===========>setup_class")

    def teardown_class(cls):
        print("===========>teardown_class")

    def setup_method(cls):
        print("===========>setup_method")

    def teardown_method(cls):
        print("===========>teardown_method")
    
    def setup(cls):
        print("===========>setup")
    
    def teardown(cls):
        print("===========>teardown")

    @pytest.mark.skip(reason="不想执行用户管理测试4")    
    @pytest.mark.usermanage
    def test_jiekou4(self):
        print("执行用户管理测试4")

    @pytest.mark.smoke
    def test_jiekou3(self):
        print("执行smoke测试5")
    
if __name__=='__main__':
    pytest.main()