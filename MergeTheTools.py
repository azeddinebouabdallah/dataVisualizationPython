# Merge the tools
import textwrap

string = input()
k = int(input())

string = textwrap.wrap(string, k)
newString = []

for s in string: 
	newS = s[0]
	for c in s:
		if not (c in newS):
			newS = '{0}{1}'.format(newS, c)
	print(newS)