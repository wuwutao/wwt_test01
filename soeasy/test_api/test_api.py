import pytest
import requests
import os
from yaml_util import Test_001
#模拟接口测试用例
class Test:                             #拿到封装好的数据   只是获取到值，定位到他的键就行
    @pytest.mark.parametrize('args',Test_001('test.yaml').Rd_yaml())
    def test_01(self,args):

        #拿到封装的数据
        url=args['request']['url']
        params=['request']['params']

        requests.get(url,params=params)
        #断言
        # assert args['validate']['eq'] ==

        # url="https://api.weixin"
        # params=
        # {
        #     "grant_tpye":"clinet_",
        #     "appid": "wx6bcszff5sx82w490",
        #     "sercret":"106sf852dgr4rey1sg"

        # }        
        # x1  = requests.get(url,params = params)
        # print(x1)