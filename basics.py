import json

data = json.load(open("files/question.json", encoding='utf8'))
# print(data)

for questionIndex, question in enumerate(data):
    print(questionIndex, question)
    for key in question:
        print(questionIndex, key)
        for answerIndex, answer in enumerate(question[key]):
            # print(' ', answerIndex, answer)
            print('xxx')
