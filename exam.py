import json
from math import floor

data = json.load(open('../python/files/data.json', encoding='utf8'))
score = 0

for qKey, item in enumerate(data):
	print(item['question'])
	for aKey, option in enumerate(item['option']):
		print(f'    {aKey + 1}: {option}')
	answer = int(input('выберите вариант: '))
	if answer == item['correct']:
		score += 1

print(f'правильных ответов: {floor(score * 100 / len(data))}%')
