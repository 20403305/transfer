import numpy as np
import matplotlib.pyplot as plt
import json
from matplotlib.ticker import AutoMinorLocator


def draw_line(name,y_list,num_points=24,scale_number=24,fig_size=(10,5)) -> None:
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
    plt.text(-3.7,3,r'$this\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'r'})
    plt.savefig(f'./{name}_chart.png',format='png')  #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中
    plt.show()

# 读取json文件内容,返回字典格式
with open('./签字报告.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)

min_hr = []
max_hr = []
avg_hr = []
for obj in json_data["ecgHourEventList"]:
   min_hr.append(obj["MinHeartRate"])
   max_hr.append(obj["MaxHeartRate"])
   avg_hr.append(obj["AverageHeartRate"])
draw_line("MinHeartRate",min_hr)
# draw_line("MaxHeartRate",max_hr)
# draw_line("AverageHeartRate",avg_hr)
