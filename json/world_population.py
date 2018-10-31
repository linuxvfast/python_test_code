from pygal_maps_world.maps import World

world_map = World()
world_map.title = 'North,Central,and South America'

world_map.add('North America',['ca','mx','us'])
world_map.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
world_map.add('South America',['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])
world_map.render_to_file('world_map.svg')


#python2
#使用pygal.Worldmap()对象生成地图

#python3
#使用下面的对象生成地图
# from pygal_maps_world.maps import World
# world_map = World()