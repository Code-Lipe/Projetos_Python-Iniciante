import pygal

worldMap = pygal.maps.world.World()
worldMap.title = 'North, Central and South America'

worldMap.add('North America', ['ca', 'mx', 'us'])
worldMap.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
worldMap.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

worldMap.render_to_file('Csv_Json\Part_2/americas.svg')
