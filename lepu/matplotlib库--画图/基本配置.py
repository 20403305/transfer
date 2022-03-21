
# 绘图时如有缺失值
# y = np.array([np.NAN, 45, 23, np.NAN, 5, 14, 22, np.NAN, np.NAN, 18, 23,np.NAN])

# 保存图片
# plt.savefig('D:\\filename.svg',format='svg')  #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中
# 展示图片
# plt.show()


# 设置图片大小
# plt.figure(figsize=(10,5))
# figure语法说明

# figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
# num: 图像编号或名称，数字为编号 ，字符串为名称
# figsize: 指定figure的宽和高，单位为英寸
# dpi: 指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80, 1英寸等于2.5cm, A4 纸是 21*30cm的纸张
# facecolor: 背景颜色
# edgecolor: 边框颜色
# frameon: 是否显示边框

# plt.rcParams['font.sans-serif']=['Arial']  #如果要显示中文字体，则在此处设为：SimHei
# plt.rcParams['axes.unicode_minus']=False  #显示负号


# x轴的内容不为数值，为输入的特定种类
# x = np.array([3,5,7,9,11,13,15,17,19,21])
# A = np.array([0.9708, 0.6429, 1, -0.8333, -0.8841, 0.5867, 0.9352, 0.8000, -0.9359, 0.9405])
# group_labels=['dataset1','dataset2','dataset3','dataset4','dataset5',' dataset6','dataset7','dataset8','dataset9','dataset10'] #x轴刻度的标识
# plt.xticks(x,group_labels,fontsize=12,fontweight='bold') #默认字体大小为10


#设置背景网格线为虚线
# plt.grid(linestyle = "--") 

# 设置显示图片的大小
# plt.figure(figsize=(10,5))


#设置x轴的范围
# plt.xlim(3,21)         
# plt.ylim(-0.5,0.5)


# 隐藏坐标轴
# plt.xticks([])
# plt.axis('off')
# frame = plt.gca()# y 轴不可见frame.axes.get_yaxis().set_visible(False)# x 轴不可见frame.axes.get_xaxis().set_visible(False)
# frame.axes.get_xaxis().set_visible(False)
