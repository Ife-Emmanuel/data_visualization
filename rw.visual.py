import matplotlib.pyplot as plt
from random_walk import RandomWalk
import pygal

# Make a random walk, and plot the points.
while True:
    rw = RandomWalk(2000)
    rw.fill_walk()

    # Set the size of the plotting window.
    # plt.figure(figsize= (10, 6), dpi= 128, facecolor= (0, 0.6, 0.6))
    point_numbers = list(range(rw.num_points))
    # To use pygal to make random walk visualization challenge
    plt.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap= plt.cm.Blues, edgecolors= 'none', s= 2)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c= 'green', edgecolors= 'none', s= 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c= 'red', edgecolors= 'none', s= 100)
    # plt.xticks([])
    # plt.yticks([])
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.title('Random Work', fontsize= 23)
    plt.show()
    plt.savefig('random_walk.svg')
    keep_running = input('Make another walk? (y/n)')
    if keep_running == 'n':
        break




















