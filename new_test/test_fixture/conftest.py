import pytest

@pytest.fixture(scope="function",params=['吴武涛','张世龙','卜步伟'])   #依次执行三次

def fixture_my(request):        #使用request 接收params的值，传进request   

    print("\n前置条件")
    yield request.param        #通过request.param 接收     ：固定写法
    print("\n后置条件")
    