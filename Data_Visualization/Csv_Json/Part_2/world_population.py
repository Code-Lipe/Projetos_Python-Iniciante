import json
import pygal
from pygal.style import RotateStyle
from country_codes import get_country_code

# Carrega os dados em uma lista
file_name = 'Csv_Json\Part_2\population_data.json'

with open(file_name) as file:
    pop_data = json.load(file)

# Constrói um dicionário com dados das populações
cc_populations = {}

for pop_dict in pop_data:
    
    if pop_dict['Year'] == '2010':

        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        
        code = get_country_code(country_name)

        if code:
            cc_populations[code] = population

# Agrupa os países em três niveis populacionais
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for cc, pop in cc_populations.items():

    if pop < 10000000:
        cc_pops_1[cc] = pop
    
    elif pop < 1000000000:
        cc_pops_2[cc] = pop

    else:
        cc_pops_3[cc] = pop

# Vê quantos paises estão em cada nível
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

worldMap_style = RotateStyle('#336699')
worldMap = pygal.maps.world.World(style=worldMap_style)
worldMap.title = 'World Population in 2010, by Country'

worldMap.add('0-10m', cc_pops_1)
worldMap.add('10m-1bn', cc_pops_2)
worldMap.add('>1bn', cc_pops_3)

worldMap.render_to_file('Csv_Json\Part_2\world_population.svg')
