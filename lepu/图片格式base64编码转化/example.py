
import  base64

# 读码
f=open(r'./II_line_chart.jpg','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
print(ls_f)

# 解码
imagedata = base64.b64decode(ls_f)#解码
 
# 根据解码生成图片 
file = open('timg.jpg',"wb")
file.write(imagedata)
f.close()