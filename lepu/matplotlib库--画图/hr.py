import numpy as np
import matplotlib.pyplot as plt
import json
from matplotlib.ticker import AutoMinorLocator



def draw_line(name,y_list,num_points=1440,scale_number=24,fig_size=(10,5)) -> None:
    """
    60*24=1440分钟个点
    标注24个刻度
    """

    x_axis = [_ for _ in range(1,num_points+1)]
    if len(y_list) < num_points:
        for _ in range(0,num_points-len(y_list)):
            y_list.append(np.NAN)
    x = np.array(x_axis)
    A = np.array(y_list)
    # 长*宽,单位为英寸
    # plt.rcParams['xtick.direction'] = 'in'
    # plt.rcParams['ytick.direction'] = 'in'
    # plt.tick_params(axis='both',which='both',direction='in')
    plt.figure(figsize=fig_size)
    # plt.grid(linestyle = "--")      #设置背景网格线为虚线

    plt.grid(which='major', color='#eb8b8b', linewidth=0.8)

    plt.grid(which='minor', color='#ee9595', linestyle=':', linewidth=0.5)

    plt.minorticks_on()
    ax = plt.subplot(111) #注意:一般都在ax中设置,不再plot中设置

    ax.xaxis.set_minor_locator(AutoMinorLocator(n = 5))
    # plt.grid(b=True, which='major', color='b', linestyle='-')      #设置背景网格线为虚线
    # plt.grid(b=True, which='minor', color='r', linestyle='--')      #设置背景网格线为虚线
    # plt.grid(linestyle = "-", which="major")      #设置背景网格线为虚线
    # plt.grid(linestyle = "--", which="minor")      #设置背景网格线为虚线
    ax = plt.gca() # 获取当前的axes
    # ax.spines['top'].set_visible(False)
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
    # plt.yticks(np.arange(-0.5,0.6,0.1)) 
    # y_group_labels = ['' for _ in range(0,2)]
    # plt.yticks((-1,1),labels=y_group_labels) 
    # plt.xticks(range(1,1441,60)) #默认字体大小为10
    # plt.xticks(range(0,1440,60)) #默认字体大小为10
    plt.xlim(1,1441)
    plt.ylim(-0.5,0.5)

    # plt.savefig(f'./{name}_line_chart.svg',format='svg')  #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中
    plt.show()


# 读取json文件内容,返回字典格式
with open('./签字报告.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)

min_hr = []
for obj in json_data["ecgHourEventList"]:
   min_hr.append(obj["MinHeartRate"])
draw_line("MinHeartRate",min_hr)

# 获取心率数据 -- page4_1
# bpm_data_list=json_data['stList'][0]["leadData"]
# bpm_leadName=json_data['stList'][0]["leadName"]
# draw_line(bpm_leadName,bpm_data_list)