"""
import sys
#当我们调用calc的时候，python，会按照这打印出来的路径，依次向下查找
# print(sys.path)
sys.path.append("D:\\vscode_python\\github\\wwt_test01\\myxlrd\calc")
# print(sys.path)
from calc import adds

print(adds(4,5))

"""

#代码的优化

import sys
from os.path import dirname,abspath

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path+"\\calc")

from calc import adds
print(adds(35))