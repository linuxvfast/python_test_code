from dice import Dice
import pygal

dice = Dice()
dice2 = Dice()
#存储摇到的骰子点数
results = []

for roll_num in range(100):
    result = dice.roll() + dice2.roll()
    results.append(result)

#存储分析结果
analysis_results = []
max_result = dice.num_sides + dice2.num_sides
for value in range(2,max_result+1):
    analysis = results.count(value)
    analysis_results.append(analysis)

print(analysis_results)

#结果可视化
hist = pygal.Bar()
hist.title = 'Count two dice 1000 times'
hist.x_labels = map(str,range(2,max_result+1))
hist.x_title = 'points'
hist.y_title = 'count results'
hist.add('two D6',analysis_results)
hist.render_to_file('count_results2.svg')  #文件后缀必须是.svg


参考图形：http://www.pygal.org/en/stable/documentation/types/bar.html
