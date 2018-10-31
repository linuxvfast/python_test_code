import json
from pygal_maps_world.maps import World
from country_codes import get_country_code

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

world_map = World()
world_map.title = 'World Population in 2010, by Country'
world_map.add('2010',populations)
world_map.render_to_file('fill_world_map.svg')