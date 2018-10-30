import csv
import matplotlib.pyplot as plt
from datetime import datetime

file_name = 'sitka_weather_2014.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #打印文件头及其位置
    # for index,header in enumerate(header_row):
    #     print(index,header)

    #获取最高气温并转化成整数
    highs,dates,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

    # print(highs)

#绘制高温图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')

plt.title('In 2014, the highest temperature',fontsize=24)
plt.xlabel('',fontsize=10)
fig.autofmt_xdate() #设置倾斜的角度
plt.ylabel('temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
