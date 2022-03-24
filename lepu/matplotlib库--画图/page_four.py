import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import json

current_path = os.path.abspath(os.path.dirname(__file__))


def draw_st_line(name,y_list,num_points=1440,scale_number=24,fig_size=(10,5)) -> None:
    """
    60*24=1440分钟个点
    标注24个刻度
    """
    my_dpi=96
    
    x_axis = [_ for _ in range(1,num_points+1)]
    if len(y_list) < num_points:
        for _ in range(0,num_points-len(y_list)):
            y_list.append(np.NAN)
    x = np.array(x_axis)
    A = np.array(y_list)
    # 长*宽,单位为英寸
    # plt.figure(figsize=(525/my_dpi, 125/my_dpi), dpi=my_dpi)
    plt.figure(figsize=fig_size)
    plt.grid(linestyle = "--")      #设置背景网格线为虚线
    ax = plt.gca() # 获取当前的axes
    # ax.spines['left'].set_visible(False)
    # ax.spines['top'].set_color('#ffffff')
    # ax.spines['bottom'].set_color('#ffffff')
    # ax.spines['left'].set_color('#ffffff')
    # ax.spines['right'].set_color('#ffffff')
    # ax.tick_params(which='both', width=0)
    # ax.tick_params(which='major', length=0)
    # ax.tick_params(which='minor', length=0, color='r')


    plt.plot(x,A,color="black",linewidth=1)
    # group_labels = ['' for _ in range(0,scale_number)]
    # plt.xticks(range(1,num_points+1,int(num_points/scale_number)),labels=group_labels) 
    plt.xticks(range(1,num_points+1,int(num_points/scale_number))) 
    # plt.xticks(range(1,1441,60)) #默认字体大小为10
    y_group_labels = ['' for _ in range(0,4)]
    # plt.yticks(range(2,9,2),labels=y_group_labels) 
    # plt.yticks(range(2,9,2)) 

    # plt.axis('off')
    # plt.axis('off')
    plt.margins(0, 0)
    # plt.savefig(f'{current_path}/{name}_line_chart.svg',format='svg',pad_inches = 0, bbox_inches='tight',dpi=my_dpi)  #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中
    plt.show()



def draw_hour_hr_line(name,y_list,num_points=24,scale_number=24,fig_size=(10,5)) -> None:
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
    plt.figure(figsize=fig_size)

    plt.grid(which='major', color='#eb8b8b', linewidth=0.8)
    plt.grid(which='minor', color='#ee9595', linestyle=':', linewidth=0.5)

    plt.minorticks_on()
    ax = plt.gca() # 获取当前的axes
    ax.xaxis.set_minor_locator(AutoMinorLocator(n = 5))
    ax.spines['top'].set_color('#eb8b8b')
    ax.spines['bottom'].set_color('#eb8b8b')
    ax.spines['left'].set_color('#eb8b8b')
    ax.spines['right'].set_color('#eb8b8b')
    ax.tick_params(which='both', width=0)
    ax.tick_params(which='major', length=0)
    ax.tick_params(which='minor', length=0, color='r')
    plt.plot(x,A,color="black",linewidth=1.5)
    group_labels = ['' for _ in range(0,scale_number)]
    plt.xticks(range(1,num_points+1,int(num_points/scale_number)),labels=group_labels) 
    plt.xlim(1,num_points+1)
    plt.savefig(f'{current_path}/{name}_chart.svg',format='svg')  #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中


# 读取json文件内容,返回字典格式
with open(os.path.join(current_path, './签字报告.json'),'r',encoding='utf8')as fp:
    json_data = json.load(fp)

# 画分钟st图
for obj in json_data["stList"]:
    leadName = obj["leadName"]
    leadData = obj["leadData"]
    # draw_st_line(leadName,leadData)

# 画小时心率图，心率变异性图，室性个数，室上性个数图
bpm = []
sdnn = []
room_num = []
room_up_num = []
for obj in json_data["hrvList"]:
   bpm.append(obj["hr"])
   sdnn.append(obj["sdnn"])
draw_st_line("hr",bpm,num_points=24)
# draw_st_line("sdnn",sdnn,num_points=24)

# for obj in json_data["ecgHourEventList"]:
#    room_num.append(obj["VentricularBeatCount"])
#    room_up_num.append(obj["AtrialBeatCount"])
# draw_st_line("VentricularBeatCount",room_num,num_points=24)
# draw_st_line("AtrialBeatCount",room_up_num,num_points=24)


# 画小时心电图
min_hr = []
max_hr = []
avg_hr = []
for obj in json_data["ecgHourEventList"]:
   min_hr.append(obj["MinHeartRate"])
   max_hr.append(obj["MaxHeartRate"])
   avg_hr.append(obj["AverageHeartRate"])
# draw_hour_hr_line("MinHeartRate",min_hr)
# draw_hour_hr_line("MaxHeartRate",max_hr)
# draw_hour_hr_line("AverageHeartRate",avg_hr)

