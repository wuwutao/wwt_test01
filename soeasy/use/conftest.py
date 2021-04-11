import pytest

@pytest.fixture(scope="function")   #依次执行三次

def fixture_use():        #使用request 接收params的值，传进request   

    print("\n管理前置条件")
    yield
    print("\n管理后置条件")
    