from pygal_maps_world.maps import World

world_map = World()
world_map.title = 'Populations of countries in North America'
world_map.add('North America',{'ca':34126000,'mx':309349000,'us':113423000})

world_map.render_to_file('world_map.svg')


