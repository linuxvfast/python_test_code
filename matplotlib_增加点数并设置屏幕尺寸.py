import matplotlib.pyplot as plt
from matplotlib_scatter_diagram  import RandomWalk

rw = RandomWalk(50000)  #增加点数
rw.fill_walk()

#设置屏幕尺寸,dpi表示屏幕分辨率，figsize表示屏幕的宽度和高度，单位英寸
plt.figure(dpi=128,figsize=(10,6))
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
plt.scatter(0,0,edgecolors='none',s=100,c='red')
plt.scatter(rw.x_values[-1],rw.y_values[-1],edgecolors='none',s=100,c='Yellow')
#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
