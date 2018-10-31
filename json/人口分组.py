import json
from pygal_maps_world.maps import World
from country_codes import get_country_code
from pygal.style import RotateStyle as RS ,LightColorizedStyle as LCS

file_name = 'population_data.json'
with open(file_name) as f:
    pop_data = json.load(f)

populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            populations[code] = population

populations_group1,populations_group2,populations_group3 = {},{},{}
for code,population in populations.items():
    if population < 10000000:
        populations_group1[code] = population
    elif population < 1000000000:
        populations_group2[code] = population
    else:
        populations_group3[code] = population
print(len(populations_group1),len(populations_group2),len(populations_group3))

world_map_style = RS('#336699',base_style=LCS)
world_map = World(style=world_map_style)
world_map.title = 'World Population in 2010, by Country'
world_map.add('2010,1-1千万',populations_group1)
world_map.add('2010,1千万-10亿',populations_group2)
world_map.add('2010,>10亿',populations_group3)
world_map.render_to_file('fill_world_map3.svg')