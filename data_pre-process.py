import pandas as pd

file = '豆瓣电影Top250.csv'
temp = pd.read_csv(file)

#数据探索
print(temp.shape)
print(temp.info())

#统计缺失值
print(temp.isnull().sum())
temp['影评'] = temp['影评'].fillna('无影评')
#检测重复值
print(temp.duplicated().sum())

data = temp[['电影名称', '评分', '评价数', '影评']]

#根据评价数排序
data.sort_values(by='评价数', ascending=False)

#根据评分分组
group = data.groupby('评分')
group_count = group.count()
group_count.sort_index(inplace=True)



