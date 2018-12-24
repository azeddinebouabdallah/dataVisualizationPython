n = int(input())
mySet = set(list(map(int, input().split())))
m = int(input())
mySet2 = set(list(map(int, input().split())))

resultSet = mySet.difference(mySet2).union(mySet2.difference(mySet))
[print (c) for c in sorted(resultSet)]