# n = int(input())
# for i in range(n):
# 	s = input()
# 	if len(s) > 10:
# 		print(s[0] + str(len(s[1:-1])) + s[-1])
# 	else:
# 		print(s)

n = 1

# n = int(input())
natural = True
for m in range(2, n + 1):
	print(n, m, n % m)
	if n != m and n % m == 0:
		natural = False
		break
if n != 1 and natural:
	print('Yes')
else:
	print('No')
