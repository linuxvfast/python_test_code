import matplotlib.pyplot as plt

plt.scatter(2,4,s=20) #s设置点的大小
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

# plt.tick_params(axis='both',which='major',labelsize=14) #设置刻度样式
plt.tick_params(axis='both',labelsize=14) #设置刻度样式
plt.show()
