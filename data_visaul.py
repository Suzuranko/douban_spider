import pandas as pd
import matplotlib.pyplot as plt

file = '豆瓣电影Top250.csv'
temp = pd.read_csv(file)
data = temp[['电影名称', '评分', '评价数', '影评']]

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
x = data['电影名称'].iloc[::10]  # 选择每四行一个电影名称
y = data['评价数'].iloc[::10]  # 选择每四行对应的评价数
plt.figure(figsize=(25,15), dpi=250)  # 设置图表大小和分辨率
plt.bar(x, y, label='评价人数')  # 绘制柱状图，并设置标签
plt.xticks(x, rotation=60, ha='right')  # 设置x轴标签旋转和对齐方式
plt.ylabel("评价人数", fontsize=15)  # 设置y轴标签和字体大小
plt.xlabel("电影名称", fontsize=15)  # 设置x轴标签和字体大小
plt.title("评价人数统计柱状图", fontsize=25)  # 设置图表标题和字体大小
plt.grid(linestyle=':')  # 绘制网格线
plt.legend(loc='upper right')  # 显示图例
plt.show()  # 显示图表
#根据评价数排序
data.sort_values(by='评价数', ascending=False)
#根据评分分组
group = data.groupby('评分')
group_count = group.count()
group_count.sort_index(inplace=True)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

plt.figure(figsize=(10,4),dpi=250)
# 绘制柱状图
plt.bar(range(group_count.shape[0]),group_count['电影名称'],label='电影数量',
tick_label=group_count.index)
#对图像各元素进行设置
plt.xlabel("分数",fontsize=15)
plt.ylabel("电影数量/部",fontsize=15)
plt.title("各分数电影数量统计柱状图",fontsize=20)
plt.grid(linestyle=":")
plt.legend(loc = 'upper right')
plt.show()
