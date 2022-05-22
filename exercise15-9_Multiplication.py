from die import Die
import pygal

# Create a D6
die_1 = Die(6)
die_2 = Die(6)
# Make some rolls and store result in a list
results = []

for i in range(1000):
    result_1 = die_1.roll_die()
    result_2 = die_2.roll_die()
    result = result_1 * result_2
    results.append(result)


# Analyze the results.
# first you first need to get the amount of distinct combination you can obtain.
frequencies = []
labels = list(range(1, die_1.num_sides * die_2.num_sides + 1))
labels_copy = labels.copy()
for i, value in enumerate(labels_copy):
    frequency = results.count(value)
    if frequency == 0:
        labels.remove(value)
        continue
    frequencies.append(frequency)


print(str(results) + '\nlength of results : ', len(results))
print(str(frequencies) + '\nlength of frequencies : ', len(frequencies))

# Visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.'
# hist.x_labels = ['{0}'.format(i) for i in label_list]
hist.x_labels = []
for i in labels:
    label = '{0}'.format(i)
    hist.x_labels.append(label)



hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')