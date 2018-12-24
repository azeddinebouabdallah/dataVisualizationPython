from collections import Counter, OrderedDict

class OrderedCount (Counter, OrderedDict):
	pass

s = input()
for c in OrderedCount(sorted(s)).most_common(3):
	print (*c)