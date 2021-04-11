import pytest

@pytest.fixture(scope="function")   #依次执行三次

def fixture_my():        #使用request 接收params的值，传进request   

    print("\n全局前置条件")
    yield 
    print("\n全局后置条件")
    