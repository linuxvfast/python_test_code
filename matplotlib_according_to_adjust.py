import  matplotlib.pyplot as plt
from matplotlib_random_walk import RandomWalk

rw = RandomWalk()#如果需要指定随机点的个数，可以使用rw = RandomWalk(500000)
rw.fill_walk()

# 设置显示图形的窗口大小
plt.figure(dpi=128,figsize=(10,6))  #figsize元组参数指定窗口大小，dpi为系统的像素大小

#从虚到实显示
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=5)

#显示起点和终点
plt.scatter(0,0,c='green',edgecolors='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

