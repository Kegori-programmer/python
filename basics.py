import json

data = json.load(open("files/question.json", encoding='utf8'))
# print(data)

for qIndex, question in enumerate(data):
    print(qIndex, question)
    for key in question:
        print(qIndex, key)
        for answerIndex, answer in enumerate(question[key]):
            print(' ', answerIndex, answer)
