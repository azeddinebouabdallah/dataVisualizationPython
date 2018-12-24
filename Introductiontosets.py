def average(l):
	l = set(l)
	return sum(l) / len(l)


n = int(input())
l = list(map(int, input().split()))
res = average(l)
print(res)