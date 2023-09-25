

# birth_year=input("Enter your birth year: ")
# int(birth_year)
# age=2023-int(birth_year)
# print(age)

#first=float(input("First: "))
#second=float(input("Second: "))
#total=first+second
#print("Sum:"+str(total))

#course="Python for beginners"
#print("Python" in course)

# weight=float(input("Weight: "))
# weight_type=input("(K)g or (L)bs: ")
# if weight_type.upper()=="K":
#     print("Weight in Kg: " + str(weight))
# elif weight_type.upper()=='L':
#     print("Weight in Kg: " + str(weight*0.45))

# i=1
# while i<=5:
#     print(i)
#     i=i+1

# names=["Minh","Senura"]
# print(names[-1])

# numbers=[1,2,3,4,5]
# numbers.insert(0, -1)
# print(numbers)

#numbers=[1,2,3,4,5]
#for num in numbers:
#   print(num)

#import datetime as dt

#my_birthday=input("My birthday (YYYY-MM-DD):")

#formated_my_birthday=dt.datetime.stpftime(my_birthday, '%d/%m/%Y')
#print(formated_my_birthday)

"""import pandas as pd
df=pd.read_csv(r'/Users/minnguyen/Desktop/Tableau_Projects/Sample/NetFlix.csv')
print(df)

pd.shape

data=pd.DataFrame(df, columns=['show_id','type','title'])
print(data)"""

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


