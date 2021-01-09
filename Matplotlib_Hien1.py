# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:58:55 2021

@author: DUC-PC
"""

import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,6), sharey=False, dpi=240)


color_names = ["Jella", "Natsu", "Lucy", "Gray", "Erza"]
colors = ["#3498db", "#fd79a8", "#f1c40f", "#273c75", "#e74c3c"]
num_favorite = [227, 361, 136, 197, 272]
xs = [i + 0.03 for i, _ in enumerate(color_names)] 
ax1.bar(xs, num_favorite, color=colors)
ax1.set(title = '''Biểu đồ thể hiện sức mạnh của
    những nhân vật trong FT''')
ax1.set_xticks([i+0.1 for i, _ in enumerate(color_names)], color_names)
plt.show()



pythontask_means, pythontask_std = (50, 47, 30, 35, 27), (3, 4, 5, 2, 3)
fatigue_means, fatigue_std = (172, 156, 93, 134, 75), (4, 6, 3, 4, 4)
ind = np.arange(len(pythontask_means))  
width = 0.35 
ax2.bar(ind - width/2, pythontask_means, width, yerr=pythontask_std,
                label='BT',color='#74b9ff')
ax2.bar(ind + width/2, fatigue_means, width, yerr=fatigue_std,
                label='Do MM',color='#d63031')
ax2.set_xticks(ind)
ax2.set_xticklabels(('T1', 'T2', 'T3', 'T4', 'T5'))
ax2.set(title =''' Bieu do the hien do met moi
        cua sinh vien ma bai tap Python gay ra''', xlabel = 'Thoi gian', ylabel = 'Do MM', xlim=(0,5), ylim=(0,200))
ax2.legend()
plt.show()

