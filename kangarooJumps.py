x1, v1, x2, v2 = map(int, input().split())

# x1+yv1 = x2+yv2
# yv1 = x2 - x1 + yv2
# yv1 - yv2 = x2 - x1
# y (v1 - v2) = x2 - x1
# y = (x2 - x1) / (v1 - v2)
# y = (4 - 0) / (3 - 2)
# y = 4 /1  = 4
# YES

"""
y = (5- 0) / (2 - 3)
y = 5 / -1
y = -5      
"""
if v1 == v2 and x1 != x2:
	print('NO')
elif (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) > 0:
	print ('YES')
else: 
	print('NO')