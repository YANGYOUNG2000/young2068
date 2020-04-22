import random

#字典存储各州对应首府的键-值
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#创建35份试卷和答案的文件
for filenum in range(35):
    file = open("F:\\testing%s.txt"%(filenum + 1),'w')
    answer = open("F:\\answer%s.txt"%(filenum + 1),'w')
    #设置每一份试卷的标题
    file.write(" " * 20 + "America State testing%s\n"%(filenum + 1))
    file.write("Your name:" + "_________" + " " * 3 + "Your class name:" + "________" + " " * 3 + "Your number:" + "________"+"\n\n\n")

    #将各州的键存储在statelist上，并且打乱顺序，以便以出的试卷50道题乱序
    statelist = list(capitals.keys())
    random.shuffle(statelist)

    #for循环创建50道题目
    for i in range(50):
        #将正确答案存储
        #且将所有的键值存储在All_answer中
        #去除正确答案后将剩余答案存储在wronge_answer中
        #随机取出三个后与正确答案存储在一个列表中
        #打乱顺序写入ABCD选项中
        correct_answer = capitals[statelist[i]]
        All_answer = list(capitals.values())
        del All_answer[All_answer.index(correct_answer)]
        wronge_answer = random.sample(All_answer,3)
        Answer = wronge_answer + [correct_answer]
        random.shuffle(Answer)

        #每一道题的模板
        file.write('%s. What is the capital of %s?\n' % (i+1,statelist[i]))
        for j in range(4):
            file.write('%s.%s\n' % ('ABCD'[j],Answer[j]))
        #将正确答案写入每一份相对应的答案文件中
        answer.write('%s.%s\n' % ((i+1),'ABCD'[Answer.index(correct_answer)]))


    file.close()
    answer.close()