import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import json

current_path = os.path.abspath(os.path.dirname(__file__))


# adjust_ratio 为最大值离最大截止值的占比
def gen_interval_list(real_max_num,rows,adjust_ratio=1) -> list:
    real_max_num = int(real_max_num)
    int_avg = real_max_num // rows  # 平均数取整
    len_max_num = len(str(real_max_num))  # 最大值长度
    digits_min_value = int(f'{1:<0{len_max_num + 1}}')  # n位数的最小值

    if len_max_num <= 1:
        scale = int_avg + 1  # 刻度值
    elif round(real_max_num / digits_min_value, 1) >= adjust_ratio:
# 低1位进一
        rate = pow(10, len_max_num - 1)  # 计算进位
        scale = (int_avg // rate + 1) * rate
    else:
        # 低2位进一
        rate = pow(10, len_max_num - 1 - 1)  # 计算进位
        scale = (int_avg // rate + 1) * rate

    max_val = scale * rows
    print(real_max_num, int_avg, len_max_num, digits_min_value, scale, max_val)
    result = np.linspace(0,max_val,rows+1,dtype=int)
    return result.tolist()





def draw_st_line(name,y_list,num_points=1440,scale_number=24,fig_size=(10,5), rows= 6,symmetry=False) -> None:
    """
    60*24=1440分钟个点
    标注24个刻度
    """
    my_dpi=96
    
    y_list_max = max(y_list)
    x_axis = [_ for _ in range(1,num_points+1)]
    if len(y_list) < num_points:
        for _ in range(0,num_points-len(y_list)):
            y_list.append(np.NAN)
    x = np.array(x_axis)
    A = np.array(y_list)
    # 长*宽,单位为英寸
    # plt.figure(figsize=(525/my_dpi, 125/my_dpi), dpi=my_dpi)
    plt.figure()
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


    plt.plot(x,A,color="black",linewidth=0.8)
    group_labels = ['' for _ in range(0,scale_number)]
    plt.xticks(range(1,num_points+1,int(num_points/scale_number)),labels=group_labels) 
    # plt.xticks(range(1,1441,60)) #默认字体大小为10
    y_group_labels = ['' for _ in range(0,rows)]
    yticks_list = gen_interval_list(y_list_max,rows)
    # print(len(yticks_list))
    # plt.yticks(yticks_list[1:],labels=y_group_labels) 
    # plt.yticks(range(2,9,2),labels=y_group_labels) 
    if not symmetry:
        ax.set_ylim(yticks_list[0], yticks_list[-1])
    else:
        ax.set_ylim(-yticks_list[-1],yticks_list[-1])
        left_yticks_list = [-x for x in yticks_list]
        yticks_list = left_yticks_list[1:][::-1] + yticks_list
    # plt.axis('off')
    plt.margins(0, 0)
    # plt.savefig(f'{pic_output_path}/{name}_line_chart.svg',format='svg',pad_inches = 0, bbox_inches='tight',dpi=my_dpi)  #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中
    plt.show()
    return yticks_list


# 读取json文件内容,返回字典格式
with open('./签字报告.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)


# 画小时心率图，心率变异性图，室性个数，室上性个数图
bpm = []
sdnn = []
room_num = []
room_up_num = []
interval_dict ={}
for obj in json_data["hrvList"]:
    bpm.append(obj["hr"])
    sdnn.append(obj["sdnn"])
interval_dict.setdefault('hr', draw_st_line("sdnn",sdnn,num_points=24,rows=6))
print(interval_dict)

# 画分钟st图
leadName = json_data["stList"][0]["leadName"]
leadData = json_data["stList"][0]["leadData"]
draw_st_line(leadName,leadData,rows=3,symmetry=True)