# Store the Quiz Data in a Dictionary
import random
# quiz data
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}
# gennerate 35 quiz files
# to do: create the quiz and answer key
# to do: work out the header for the quiz
# to do: shuffle the order of the states
# to do: loop through all 50 states, making  a question for each
for quiznum in range(35):
    quizfile = open('capitalsquiz%s.txt' % (quiznum + 1), 'w')
    answerkeyfile = open('capitalsquiz_answers %s.txt' % (quiznum + 1), 'w')
# write out the header for the quiz
    quizfile.write('name:\n\n Date:\n\nPeriod:\n\n')
    quizfile.write((' ' *20) + 'state capitals quiz (Form %s)' % (quiznum + 1))
    quizfile.write('\n\n')
# shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
#loop through all 50 states, making the questions for each
    for questionnum in range(50):
# get right and wrong answers:
        correctanswer = capitals[states[questionnum]]
        wronganswer = list(capitals.values())
        del wronganswer[wronganswer.index(correctanswer)]
        wornganswer = random.sample(wronganswer, 3)
        answeroptions = wronganswer + [correctanswer]
        random.shuffle(answeroptions)
# write the questions and the answer options to the quiz file
        quizfile.write('%s. what is the capital of %s?\n' % (questionnum + 1, states[questionnum]))
        for i in range(4):
            quizfile.write('%s. %s\n' % ('ABCD'[i], answeroptions[i]))
        quizfile.write('\n')
        answerkeyfile.write('%s. %s\n' % (questionnum + 1, 'ABCD' [answeroptions.index(correctanswer)]))
    quizfile.close()
    answerkeyfile.close()
