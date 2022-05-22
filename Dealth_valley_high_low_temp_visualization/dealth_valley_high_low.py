"""To extract dealth valley weather_data from a csv file and analyse, process, and visualize the data. """
import csv

filename = r'C:\Users\User\PycharmProjects\data_visualization\Dealth_valley_high_low_temp_visualization\death_valley_2018_simple.csv'
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_line = next(reader)
    print(header_line)

# I used zip( I noticed one good application of the numpy where() in template matching of open. the zip stuff I saw in opencv. also has to be reviewed
# data visualization, computer vi=[p;#sion, f_strings, data science, github
