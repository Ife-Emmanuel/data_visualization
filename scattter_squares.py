# import matplotlib.pyplot as plt
#
# x_values = list(range(1001))
# y_values = [x**2 for x in x_values]
# # print(x_values)
# # print(y_values)
# # x_values = [1, 2, 3, 4, 5]
# # y_values = [1, 4, 9, 16, 25]
# print(len(x_values))
# print(len(y_values))
# # wow data visualization is actually very simple mehn. fucking interesting.
# # plt.scatter(x_values[0 : 3], y_values[0 : 3], s= 200)
# # plt.scatter(x_values[3 : 5], y_values[3 : 5], s= 200)
# plt.scatter(x_values, y_values, s= 40, c= y_values, cmap= plt.cm.Blues, edgecolors= 'none')
# plt.show()
# #plt.scatter(x_values, y_values, c= y_values, cmap= plt.cm.Blues, edgecolors= 'none', s= 200, marker= 's')
#
# # Set chart title and label axes.
# plt.title('Square Numbers', fontsize= 24)
# plt.xlabel('Value', fontsize= 14)
# plt.ylabel('Square Value', fontsize= 14)
#
# # Set size of tick label
# plt.tick_params(axis= 'both', which= 'major', labelsize= 14)
# plt.axis([0, 1100, 0, 1100000])
# plt.savefig('squares_plot.png', bbox_inches= 'tight')

import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 8, 27, 64, 125]
x_values = list(range(5000))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, s= 200, edgecolors= 'none', c= y_values, cmap= plt.cm.Greens, marker= 's')
plt.show()


