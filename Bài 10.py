# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:20:27 2020

@author: Trần Thị Diệu Hiền
"""

#Numpy
print("1/Tìm hiểu thư viện Numpy")
import numpy as np
A=[[1,2,3],[2,1,3],[1,1,-1]]
A=np.array(A)
print(A)
B=[[1,2,1],[2,1,4],[1,1,0]]
B=np.array(B)
print("Cộng hai ma trận A và B")
print(A+B)
print("Nhân hai ma trận A và B")
print(A.dot(B))

#Pandas
print("2/Tìm hiểu thư viện Pandas")
import pandas as pd
result = pd.read_csv('writeData.csv')
print(result.head(10))
pds = 'https://data.cese.nsw.gov.au/data/dataset/1a8ee944-e56c-3480-aaf9-683047aa63a0/resource/da0fd2ec-6024-3206-98d4-81a2c663664b/download/headcount.csv'
data = pd.read_csv(pds)
print(data.head(10))
ts = 'https://data.cese.nsw.gov.au/data/dataset/027493b2-33ad-3f5b-8ed9-37cdca2b8650/resource/af20d17c-a7ac-4251-af75-e5ae66573e92/download/collections.json'
data1 = pd.read_json(ts)
print(data1.head(10))

# Matplotlib
print("3/ Tìm hiểu thư viện Matplotlib")
# Bar Chart
import matplotlib.pyplot as plt
color_names = ["Jella", "Natsu", "Lucy", "Gray", "Erza"]
colors = ["#3498db", "#fd79a8", "#f1c40f", "#273c75", "#e74c3c"]
num_favorite = [227, 361, 136, 197, 272]
xs = [i + 0.03 for i, _ in enumerate(color_names)]
plt.bar(xs, num_favorite, color=colors)
plt.title("Những nhân vật trong FT")
plt.xticks([i+0.1 for i, _ in enumerate(color_names)], color_names)
plt.xlabel("Tên nhân vật")
plt.ylabel("Sức mạnh")
plt.show()

# Column Chart
pythontask_means, pythontask_std = (50, 47, 30, 35, 27), (3, 4, 5, 2, 3)
fatigue_means, fatigue_std = (172, 156, 93, 134, 75), (4, 6, 3, 4, 4)
ind = np.arange(len(pythontask_means))  
width = 0.35 
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, pythontask_means, width, yerr=pythontask_std,
                label='Bài tập Python',color='#74b9ff')
rects2 = ax.bar(ind + width/2, fatigue_means, width, yerr=fatigue_std,
                label='Độ mệt mỏi của sv',color='#d63031')
ax.set_xticks(ind)
ax.set_xticklabels(('Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5'))
plt.title('''   Biểu đồ thể hiện độ mệt mỏi mà 
   bài tập lập trình gây ra''')
plt.xlabel("Thời gian trải qua")
plt.ylabel("Số bài tập TLT độ mệt mỏi")
ax.legend()
plt.show()

# Boxplot Chart
x = np.random.randn(70) + np.arange(0, 70)*0.75 + 10
y = np.random.randn(80) + np.arange(0, 80)*1.0 +20
z = np.random.randn(65) + np.arange(0, 65)*0.5 + 5
t = np.random.randn(60) + np.arange(0, 60)*0.4 + 0.0

plt.boxplot([x, y, z, t], 
            labels = ['Mùa Xuân', 'Mùa Hạ', 'Mùa Thu','Mùa Đông'],
            showfliers = True)

plt.title('''Biểu đồ Boxplotb thể hiện 
  chỉ số thay đổi nhiệt độ theo độ F theo mùa ở xứ NONAME''')
plt.xlabel('Mùa')
plt.ylabel('Chỉ số nhiệt độ theo độ F')