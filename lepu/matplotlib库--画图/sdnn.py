import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import json

current_path = os.path.abspath(os.path.dirname(__file__))

def draw_room_line(name,y_list,num_points=24,scale_number=24,fig_size=(10,5)) -> None:
    """
    每个小时一次数值,最多24小时
    标注24个刻度
    """
    x_axis = [_ for _ in range(1,num_points+1)]
    if len(y_list) < num_points:
        for _ in range(0,num_points-len(y_list)):
            y_list.append(np.NAN)
    x = np.array(x_axis)
    A = np.array(y_list)
    # 长*宽,单位为英寸
    plt.figure(figsize=fig_size)
    plt.grid(linestyle = "--")      #设置背景网格线为虚线
    plt.plot(x,A,color="black",linewidth=1.5)
    group_labels = ['' for _ in range(0,scale_number)]
    plt.xticks(range(1,num_points+1,int(num_points/scale_number)),labels=group_labels) 
    # plt.xticks(range(1,1441,60)) #默认字体大小为10

    plt.savefig(f'{current_path}/{name}_line_chart.png',format='png')  #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中
    plt.show()


# 读取json文件内容,返回字典格式
with open('./签字报告.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)


bpm = []
sdnn = []
room_num = []
room_up_num = []
for obj in json_data["hrvList"]:
   bpm.append(obj["hr"])
   sdnn.append(obj["sdnn"])
draw_room_line("hr",bpm)
draw_room_line("sdnn",sdnn)

for obj in json_data["ecgHourEventList"]:
   room_num.append(obj["VentricularBeatCount"])
   room_up_num.append(obj["AtrialBeatCount"])
draw_room_line("VentricularBeatCount",room_num)
draw_room_line("AtrialBeatCount",room_up_num)
