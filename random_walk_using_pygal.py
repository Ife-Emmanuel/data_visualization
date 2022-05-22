import matplotlib.pyplot as plt
from random_walk import RandomWalk
import pygal

# Make a random walk, and plot the points.
while True:
    rw = RandomWalk(1000)
    rw.fill_walk()

    # Set the size of the plotting window.
    # plt.figure(figsize= (10, 6), dpi= 128, facecolor= (0, 0.6, 0.6))
    point_numbers = list(range(rw.num_points))
    # To use pygal to make random walk visualization challenge
    hist = pygal.Bar()
    hist.title = 'Random Walk Visualization Using Pygal'
    hist.x_title = 'Walk in horizontal direction'
    hist.y_title = 'Walk in vertical direction'
    hist.x_labels = ['{0}'.format(i) for i in rw.x_values]
    hist.add('Random walk', rw.y_values)
    hist.render_to_file('random walk.svg')

    response = input('Do you want to prodeuce another visualization?(y/n)')
    if response == 'n':
        break
    elif response == 'y':
        continue