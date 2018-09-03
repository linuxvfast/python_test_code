import matplotlib.pyplot as plt
x_value = list(range(1001))
y_value = [x**2 for x in x_value]

#https://matplotlib.org/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
#cmap的颜色参考
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Greys,edgecolors='none',s=40)

plt.title('color map',fontsize=24)
plt.xlabel('x coordinate',fontsize=14)
plt.ylabel('y coordinate',fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])
plt.savefig('squares_plot.png',bbox_inches='tight')  #bbox_inches参数裁剪图标中多余的空白区域
plt.show()
