import matplotlib.pyplot as plt 

figure = plt.figure('Line')
ax = figure.add_subplot(1,1,1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.plot([0, 1, 2, 3, 4, 5], [10, 12, 3, 7, 1, 4])
plt.show()

fig = plt.figure('Stacked bar')
ax1 = figure.add_subplot(1,1,1)

data = {
	'Players' : ['Didou', 'Younes', 'Sara'],
	'Age': [20, 13, 11],
	'Weight' : [75, 53, 48]
}

bar_width = 0.5
