
import yaml
#yaml 的工具包      
#拿到yaml 中的所有数据，进行反序列化，转化为字典
#到时候直接给测试用例数据
class Test_001:
    def __init__(self,read_yaml):
        self.read_yaml = read_yaml
    
    def Rd_yaml(self):
        #读取yaml文件，对读取到的yaml数据进行反序列化，转化为字典的格式
        with open(self.read_yaml,encoding='utf-8') as f:
                        #表示加载的方式  
            data = yaml.load(f,Loader=yaml.FullLoader)
            return data

if __name__=='__main__':
    #封装读取数据的方法
    Test_001('items_yaml.yaml').Rd_yaml()


#将获得的yaml 文件反序列化为字典
#拿给需要调用数据的人

