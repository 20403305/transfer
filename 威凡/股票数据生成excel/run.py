import json
import pandas as pd


total1 =[]
total2 =[]

# 读取json文件内容,返回字典格式
with open('./a.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    print('这是读取到文件数据的数据类型：', type(json_data))
    data_list=json_data['data']
    print(len(data_list))

with open('./b.json','r',encoding='utf8')as fp:
    jason_date = json.load(fp)
    data_dict=jason_date['data']['stocks']
    print(len(data_dict))
list1=[]
list2=[]
list3=[]
list4=[]

for i in data_list.values():
    data1=i['symbol'] #用来存放股票代码
    data2=i['stock_chi_name'] #变量用来存放股票名称
    list1.append(data1)
    list2.append(data2)

for data in data_dict:
    data3=data['desc']
    data4=data['symbol']
    list3.append(data3)
    list4.append(data4)

total_data = []

for i in range(len(data_dict)):
    combined_data = []
    combined_data.append(list1[i+1])
    combined_data.append(list2[i+1])
    combined_data.append(list3[i])
    combined_data.append(list4[i])
    total_data.append(combined_data)
    # print(combined_data)

df = pd.DataFrame(total_data)
df.columns =['股票代码', '股票名称',"股票归因","股票代码"]
# print(df)
df.to_csv(r'./res.csv',index=True,encoding='utf_8_sig')