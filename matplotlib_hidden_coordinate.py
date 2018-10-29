import matplotlib.pyplot as plt
from matplotlib_scatter_diagram  import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.scatter(0,0,edgecolors='none',s=100,c='red')
plt.scatter(rw.x_values[-1],rw.y_values[-1],edgecolors='none',s=100,c='Yellow')
#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
