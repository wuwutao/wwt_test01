import pytest
import os

if __name__=='__main__':

    pytest.main()     #打印内容：-s
    os.system('allure generate ./temp -o ./report --clean')