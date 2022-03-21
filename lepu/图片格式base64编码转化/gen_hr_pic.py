
import  base64
import json

# 读取json文件内容,返回字典格式
with open('./签字报告.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)

image_base_data = json_data["imgList"][0]["imgData"]

# 解码
imagedata = base64.b64decode(image_base_data)#解码
 

# 根据解码生成图片 
with open('./hr.jpg','wb')as fp:
    fp.write(imagedata)
