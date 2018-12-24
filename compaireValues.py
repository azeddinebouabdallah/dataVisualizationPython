import matplotlib.pyplot as plt

data = {
	'Players': 	['Didou', 'Younes', 'Sara'],
	'Age'	:	[20, 13, 11],
	'Level' : 	[16, 8, 6],
	'Weight':	[67, 55, 44] 
}

figure = plt.figure('Stacked bar')
ax = figure.add_subplot(1,1,1)

bar_width = 0.5
bars = [i+1 for i in range(len(data['Players']))]
ticks = [i + (bar_width/2) for i in bars]
ax.bar(bars, data['Age'], width = bar_width, color= '#AAF600', label= 'Age')
ax.bar(bars, data['Level'], width = bar_width, bottom = data['Age'], label = 'Level', color= "#3498db")
ax.bar(bars, data['Weight'], width = bar_width, bottom = [i + j for i, j in zip(data['Age'], data['Level'])], label= 'Weight', color= '#2ecc71')

ax.set_xlabel('Players')
ax.set_ylabel('Total')

plt.xlim([min(ticks) - bar_width, max(ticks) + bar_width])
plt.legend(loc = 'upper right')
plt.xticks(ticks, data['Players'])
plt.show()