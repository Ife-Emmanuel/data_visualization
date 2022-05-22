import json

# Load the data into a list.
filename = r'C:\Users\User\PycharmProjects\data_visualization\Mapping_Global_Data_Sets\population_data.json'
with open(filename) as file_object:
    pop_data = json.load(file_object)

    # Print the 2010 population for each country.
    i = 1
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            print(str(i) + '.  ' + country_name + ' : ' +  str(population))
            i += 1

