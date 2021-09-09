# n, m = map(int, input().split())
# array1 = list(map(int, input().split()))
# array2 = list(map(int, input().split()))
n = 2
m = 3
array1 = [3, 9]
array2 = [2, 3, 6]

aIdx = 0
bIdx = 0
res = []
while aIdx + bIdx != n + m:
	if aIdx >= n:
		res.append(array2[bIdx])
		bIdx += 1
	elif bIdx >= m:
		res.append(array1[aIdx])
		aIdx += 1
	elif array1[aIdx] < array2[bIdx]:
		res.append(array1[aIdx])
		aIdx += 1
	else:
		res.append(array2[bIdx])
		bIdx += 1

print(' '.join(str(item) for item in res))
