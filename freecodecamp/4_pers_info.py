#!/usr/bin/python3

questions = ['What is your name?', 'What is your birthdate?', 'What is your Address?', 'What are your goals?']
answers = []

#for i in len(questions):
for i in range(0,len(questions)):
    try:
        answer = str(input(questions[i]))
        answers.append(answer)
    except:
        e = sys.exc_info()[0]
        write_to_page( "<p>Error: %s</p>" % e )

