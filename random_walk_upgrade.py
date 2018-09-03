from random import choice

class RandomWalk():
    '''生成随机坐标的类'''

    def __init__(self,num_points=5000):
        '''初始化随机漫步的属性'''
        self.num_points = num_points

        #起始位置(0,0),存储随机的点坐标
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        while len(self.x_values) < self.num_points:#检查产生的点总数是否达到指定的值num_points
            #获取移动的方向和距离
            x_direction = choice([1,-1])
            x_distance = choice(range(9))
            x_step = x_direction * x_distance

            y_direction = choice([1, -1]) #移动方向
            y_distance = choice(range(9))#移动距离
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:#禁止原地不动
                continue

            #在最后移动结果上进行移动
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # 保存随机产生的点坐标
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            # print(self.x_values)
            # print(self.y_values)

        return [self.x_values,self.y_values]


    def fill_walk(self):
        '''记录随机产生的点'''

        x_result = self.get_step()[0]
        y_result = self.get_step()[1]
        # print(x_result)
        # print(y_result)



if __name__ == '__main__':
    rw = RandomWalk()
    rw.fill_walk()
