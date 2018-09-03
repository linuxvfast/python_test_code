import matplotlib.pyplot as plt

squares = [11,16,21,23,25]
plt.plot(squares,linewidth=5)  #linewidth设置线条的宽度
plt.title('Square Numbers',fontsize=24)   #设置标题，指定字体大小
plt.xlabel('Value',fontsize=14)     #设置x轴的标题，设置字体大小
plt.ylabel('Square of Value',fontsize=14) #设置y轴的标题，设置字体大小

plt.tick_params(axis='both',labelsize=14) #设置刻度样式
plt.show()
