def candidate_answer():
    pointer=False
    answer=int(input('Enter your answer: '))
    if const_options[answer-1]==question[1]:
        pointer=True
    return pointer

def display_question(question_set):
    global question
    global const_options
    question=question_set[0]
    options=question_set[1]
    const_options=[]
    options.append(question[1])
    options=set(options)
    print(question[0])
    no=1
    for j in options:
        print(no,j)
        const_options.append(j)
        no=no+1

def test(*question_sets):
    score=0
    for i in question_sets:
        display_question(i)
        result=candidate_answer()
        if result==True:
            print("congrats! You entered the correct answer")
            score=score+1
        else:
            print("You entered wrong answer")
    print(f"Your {score} answers are correct out of {len(question_sets)} questions ")
question_set1=[('What is the capital of Russia ?','Moscow'),['New Delhi','Beijing','Kiyv']]
question_set2=[('Who is the prime minister of India ?','Narendra Modi'),['Rahul Gandhi','Arvind Kejriwal','Mamta banerjee']]
question_set3=[('Which country is known as largest democracy in the world ?','India'),['U.S.A.','China','U.K.']]
question_set4=[('In which state of India lithium reserves is found ?','Kashmir'),['Delhi','West Bengal','Bihar']]
question_set5=[('BARAK-8 is a defence item jointly developed by India and _______?','Israel'),['Russia','U.S.A.','France']]
print('+----------------------------------------------------------------Rules--------------------------------------------------------------+')
print('|                                                                                                                                   |')
print('+ 1.You only need to enter the no. of the options which you think is correct                                                        +')
print('|                                                                                                                                   |')
print('+ 2.Once you started you have to answer all the questions and you will not able attained any question twice                         +')
print('|                                                                                                                                   |')
print('+ 3.Each question contains equal prizes                                                                                             +')
print('|                                                                                                                                   |')
print('+-------------------------------------------------------------Best of luck----------------------------------------------------------+')
will=input(" If you are ready for the test then type(s): ")
if will=='s':
    test(question_set1,question_set2,question_set3,question_set4,question_set5)