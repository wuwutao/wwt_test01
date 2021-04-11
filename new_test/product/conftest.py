import pytest

@pytest.fixture(scope="function")   #依次执行三次

def fixture_po():        #使用request 接收params的值，传进request   

    print("\n商品前置条件")
    yield 
    print("\n商品后置条件")
    