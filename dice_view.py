

from dice import Dice
import pygal

dice = Dice()

results = [] #统计出现的结果
for num in range(1000):
    result = dice.roll()
    results.append(result)

responses = [] #统计每个点数出现的频率
for value in range(1,dice.num_sides+1):
    response = results.count(value)
    responses.append(response)


#显示直方图
hist = pygal.Bar()

hist.title = "Dice Count View"
hist.x_labels = map(str,range(1,dice.num_sides+1))
hist.x_title = "Result"
hist.y_title = "Responses of Result"

hist.add('D6',responses)
hist.render_to_file('dice_view.svg')

