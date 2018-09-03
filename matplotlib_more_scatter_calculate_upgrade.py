import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,edgecolors='none',s=40) #edgecolors删除黑色轮廓
# plt.scatter(x_value,y_value,c='red',edgecolors='none',s=40) #edgecolors删除黑色轮廓,并设置线条颜色为红色
#plt.scatter(x_value,y_value,c=(0,0,0.8),edgecolors='none',s=40)#edgecolors删除黑色轮廓,并设置线条颜色为蓝色(红色，绿色，蓝色),值都是0~1之间的小数，越接近0，颜色越深，越接近1，颜色越浅

plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)
plt.axis([0,1100,0,1100000])   #设置x轴和y轴的取值范围
plt.show()
