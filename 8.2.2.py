n = list(map(int, list(input())))
# n = list(map(int, list('56639')))
even = 0
gt_five = 0
gt_seven = 1
zero_five = 0
for item in n:
	# количество четных цифр;
	if item % 2 == 0:
		even += 1
	# сумму его цифр, больших пяти;
	if item > 5:
		gt_five += item
	# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
	if item > 7:
		gt_seven = gt_seven * item
	# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
	if item == 0 or item == 5:
		zero_five += 1
# количество цифр 3 в нем;
print(n.count(3))
# сколько раз в нем встречается последняя цифра;
print(n.count(n[len(n) - 1]))
print(even)
print(gt_five)
print(gt_seven)
print(zero_five)
