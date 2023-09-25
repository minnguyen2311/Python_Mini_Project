

#Text abbreviations quiz

print ("Welcome to my quiz! The quiz is about text abbreviations")

playing = input("Do you want to play? ")

if playing.lower() == 'yes':
    print("Let's start the quiz")
else:
    print("No worries, lets play next time!")
    quit()

score = 0

question= input("What does LMK stand for? ")
if question.lower() == 'let me know':
    print("Correct")
    score+=1
else:
    print("Incorrect")

question= input("What does AFAIK stand for? ")
if question.lower() == 'as far as i know':
    print("Correct")
    score += 1
else:
    print("Incorrect")

question= input("What does TTYLT stand for? ")
if question.lower() == 'talk to you later':
    print("Correct")
    score += 1
else:
    print("Incorrect")

question= input("What does TGIF stand for? ")
if question.lower() == "thanks goodness it's friday":
    print("Correct")
    score += 1
elif question.lower() == "thanks god it's friday":
    print("Correct")
    score += 1
elif question.lower() == "thanks god its friday":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question= input("What does NVM stand for? ")
if question.lower() == 'nevermind':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct")
print("You got " + str((score/5)*100) + " %" + "questions correct")


