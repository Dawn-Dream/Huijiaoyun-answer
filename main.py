#coding:utf8
 
import urllib2
#json解析库,对应到lxml
import json
#json的解析语法，对应到xpath
import jsonpath
 
with open("test.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    html=data
unicodestr=json.loads(html)
 
#python形式的列表
answer_list=jsonpath.jsonpath(unicodestr,"$..answer")
t=1
for i in answer_list:
    print t,".",i
    t=t+1
array=json.dumps(answer_list,ensure_ascii=False)

#把结果写入到lagouCity.json文件中
with open("answer.json","w") as f:
    f.write(array.encode("utf-8"))