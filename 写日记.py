import time 

now = time.strftime("%y-%m-%d %H:%M:%S")
test =input("请输入今天的心情：")

with open("D:\test.txt","a",encoding="utf8") as f :

    f.write(now+"\n")
    f.write(test+"\n")
    f.write("----------------------\n")