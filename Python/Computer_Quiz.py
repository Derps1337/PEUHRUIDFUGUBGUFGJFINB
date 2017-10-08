import random, math, csv

#-------------------------------------------
def cls():
    print ('\n' * 50)
    return
#-------------------------------------------


#-------------------------------------------
def printtitle():
    print('''
=============================
 Multi choice quiz main menu
=============================


''')
    return
#-------------------------------------------


#-------------------------------------------
def paktc():
    input("Press any key to continue")
    return
#-------------------------------------------


#-------------------------------------------
def printdificulty():
    print ('''
Enter dificulty level :-

    1-Easy
    2-Medium
    3-Hard
''')
    return
#-------------------------------------------


#-------------------------------------------    
def printsubjectchoice():
        print ('''
Enter subject :-

    1-Computer Science
    2-Music
    3-History
''')
        return
#-------------------------------------------


#-------------------------------------------
def printdificultychoice(Dificulty):
    print ("")
    print ("you selected",Dificulty,"Dificulty") 
    print ("")
    return
#-------------------------------------------


#-------------------------------------------
def  printselectedsubject(Sub):
    print ("")
    print ("you selected",Sub,"as your subject")
    print ("")
    return
#-------------------------------------------


#-------------------------------------------    
def read_database(filename):
    dictionary = {}
    infile = open(filename, 'r')
    for line in infile:
        line = line.strip()
        q,a1,a2,a3,a4 = line.split(',')
        question = (q)
        answers = [a1,a2,a3,a4]
        dictionary[question] = answers
    infile.close()
    return dictionary
#-------------------------------------------


#-------------------------------------------
def calculatepercentage(score,questions,Dif):
    ratio = score / questions
    if Dif == 1:
        percentage = ratio * 50
    if Dif == 2:
        percentage = ratio * 75
    if Dif == 3:
        percentage = ratio * 100
    return percentage
#-------------------------------------------


#-------------------------------------------
def calculategrade(perc):
    if perc <= 25:
        grade = "D"
    if perc >25 and perc <=50:
        grade = "C"
    if perc >50 and perc <=75:
        grade = "B"
    if perc >75 and perc <=100:
        grade = "A"
    return grade
#-------------------------------------------


#-------------------------------------------
def selectnumber1to(num):
    while True:
        print ("")
        print ("Please Select your answer 1 to",num)
        Dif_choice = input ()
        if not Dif_choice.isdigit():
            print("You must enter a numerical value")
            continue
        Dif_choice = int(Dif_choice)
        if Dif_choice >=1 and Dif_choice <=num:
            break            
        print ("You must enter a number in the range 1 to",num)
    return(Dif_choice)
#-------------------------------------------


#-------------------------------------------
def ask_question(question, answers, Dif):
    score = 0
    multi = ["","","",""]
    randomlocation = random.randint(1,Dif+1)-1
    multi[randomlocation] = answers[0]
    Correctanswer = randomlocation+1
    randomlocation = random.randint(1,4)-1
    location = 1
    while location <= 3:
        randomlocation = random.randint(1,4)-1
        if multi[randomlocation] == "":
            multi[randomlocation] = answers[location]
            location += 1      
    print("")    
    print("1: ",multi[0])
    print("2: ",multi[1])
    if Dif >= 2:
        print("3: ",multi[2])
    if Dif == 3:
        print("4: ",multi[3])

    Dif_choice = selectnumber1to(Dif+1)

    if Dif_choice == Correctanswer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print()
    return score
#-------------------------------------------


#-------------------------------------------
def get_dif_choice():
    printdificulty()
    Dif_choice = selectnumber1to(3)
    return Dif_choice
#-------------------------------------------


#-------------------------------------------
def get_Subject_choice():
    printsubjectchoice()   
    Subject_choice = selectnumber1to(3)
    return Subject_choice
#-------------------------------------------


#-------------------------------------------
def main():
    SubjectDict = {1:'Computer Science',2:'Music', 3:'History'}    
    DifDict = {1:'Easy',2:'Medium', 3:'Hard'}
    Currentpercentage = 0
    score = 0
    score = int(score)
    cls()
    printtitle()
    Subject = get_Subject_choice()
    printselectedsubject(SubjectDict[Subject])
    paktc()
    cls()
    if Subject == 1:
        questions = read_database("Computer.csv")
        print ("Computer science questions loaded")
    if Subject == 2:
        questions = read_database("Music.csv")
        print ("Music questions loaded")
    if Subject == 3:
        questions = read_database("History.csv")
        print ("History questions loaded")
    print ("")
    print("What is your name?")
    name = input()
    print ("")
    numberofquestions = 5
    print ("Hi," + name + " there are", len(questions) ,"different")
    print (SubjectDict[Subject],"questions in the quiz")
    print ("you will be given" , numberofquestions , "random questions: ")
    print ("")
    Question_list = random.sample(questions.keys(), numberofquestions)

    

    Dificulty = get_dif_choice()
    printdificultychoice(DifDict[Dificulty])                    
    paktc()
    cls()
    Currentscore = 0
    questionnumber = 1
    for key in Question_list:
        print ("Question ",questionnumber)
        print(key)
        result = ask_question( key, questions.get(key),Dificulty)
        paktc()
        cls()
        if result == 1:
            Currentscore +=1
        questionnumber += 1
    print("Your final score was",Currentscore,"out of ",numberofquestions)
    Currentpercentage =  calculatepercentage(Currentscore,numberofquestions,Dificulty)
    print("Current grade percentage",Currentpercentage,"%")
    Currentgrade = calculategrade(Currentpercentage)
    print("Your current grade is",Currentgrade)
#-------------------------------------------

    
if __name__ == "__main__":
    main()
