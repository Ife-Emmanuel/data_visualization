import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename  = r'C:\Users\User\PycharmProjects\data_visualization\edition2_mapping_global_data_sets\eq_data_1_day_m1.json'
with open(filename) as file_object:
    all_eq_data = json.load(file_object)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes
data = [
    {'type' : 'scattergeo',
     'lon' : lons,
     'lat' : lats,
     'text' : hover_texts,
     'marker' : {'size' : [ 5 * mag for mag in mags],
                 'color' : mags,
                 'colorscale' : 'Viridis',
                 'reversescale' : True,
                 'colorbar' : {'title' : 'Magnitude'}
                 }
     }
        ]
my_layouts = Layout(title= 'Global Earthquakes')

fig = {'data' : data, 'layout' : my_layouts}
offline.plot(fig, filename = 'global_earthquakes.html')

readable_file = r'data/readable_eq_data.json'
with open(readable_file, 'w') as file_object:
    json.dump(all_eq_data, file_object, indent= 4)

