# Visualization in PYTHON 

# matplotlib: basic library for data visualization
# some others: vispy, seaborn, pygal, folium, pandas

import matplotlib.pyplot as plt

fig = plt.figure('Histogram')
ax = fig.add_subplot(1,1,1)

ax.hist([30, 35, 30, 27, 60, 50, 53, 45, 40, 37], bins = 7, facecolor = 'g', normed=True) # normed = values are in [0 - 1]
# facecolor = r : red
plt.title('Distibution')
plt.xlabel('Range')
plt.ylabel('Amount')
plt.show()

fig2 = plt.figure('Box-plot')
ax2 = fig2.add_subplot(1,1,1)
ax2.boxplot([21, 18, 20, 35, 16, 23, 30])
plt.show()

fig3 = plt.figure('Bar')
ax3 = fig3.add_subplot(1,1,1)
ax3.set_xlabel('X') 
ax3.set_ylabel('Y')
ax3.set_title('Bar Graph')
ax3.bar([0, 1, 2, 3], [5, 10, 15, 5], [0.5, 0.5, 0.5, 0.5], color = ['r', 'b', 'g', 'y'])# X , Y , Width, List of colors
plt.show()

fig4 = plt.figure('Line')
ax4 = fig4.add_subplot(1,1,1)
ax4.set_xlim([-2, 10])
ax4.set_ylim([-2, 10])
ax4.set_title('Line graph')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.plot([-2, -1, 0, 1, 2, 3, 4, 5, 6],[1, 4, 9, 5, 3, 6, 2, 9, 8])
plt.show()