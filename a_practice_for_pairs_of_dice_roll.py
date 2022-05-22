from die import Die
import pygal

# Create a D6
die_1 = Die(10)
die_2 = Die(6)
# Make some rolls and store result in a list
pre_results = []

for i in range(1000):
    result_1 = die_1.roll_die()
    result_2 = die_2.roll_die()
    result = result_1, result_2
    result = {result}
    pre_results.append(result)


print(results)
# Analyze the results.
# first you first need to get the amount of distinct combination you can obtain.
frequencies = []
labels = set(results)
for value in labels:
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)

# Visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling one D8 1000 times.'
# hist.x_labels = ['{0}'.format(i) for i in label_list]
hist.x_labels = []
for i in labels:
    i = label
    label = '{0}'.format(i)
    hist.x_labels.append(label)



hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D8', frequencies)
hist.render_to_file('die_visual.svg')

from collections import Counter

def find_tuple_frequency(collection):
    """To find the frequency of a dataset in a defined collection."""


