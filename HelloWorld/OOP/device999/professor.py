import random

class Professor:
    exam = True

    def __init__(self,age,name,amount):
        self.age = age
        self.name = name
        self.amountOfQuestions = amount
        self.grade = 0
        self.amountOfQuestions = 0
        self.correctAnswer = 0
        self.wrongAnswer = 0
        print("Hello, my name is "+name)
        print("I am "+str(age)+" old")
        print("We can proceed to the exam")

    def substract(number1, number2):
        return number1-number2
    
    def addition(number1, number2):
        return number1+number2

    def multiply(number1, number2):
        return number1*number2

    def divide(number1,number2):
        return number1/number2
    
    def statistics(self, student, answer):
        if student==answer:
            self.correctAnswer = self.correctAnswer + 1
        else:
            self.wrongAnswer = self.wrongAnswer + 1
        self.amountOfQuestions = self.amountOfQuestions + 1
    
    def goodAnswer(self):
        correct = float(self.correctAnswer)
        amount = float(self.amountOfQuestions)
        return float(round(correct*100/amount,3))

    def badAnswer(self):
        wrong = float(self.wrongAnswer)
        amount = float(self.amountOfQuestions)
        return float(round(wrong*100/amount,3))


if __name__ == '__main__':
    professorName = input("You are going to prof. = ")
    age = int(input("His age = "))
    amountQuestions = int(input("Number of questions = "))
    professor = Professor(age,professorName,amountQuestions)
    while Professor.exam:
        number1 = random.randint(1,11)
        number2 = random.randint(1,11)
        actionType = random.randint(1,4)
        if actionType==1:
            studentAnswer = int(input(str(number1)+" - "+str(number2)+" = "))
            correctAnswer = Professor.substract(number1,number2)
            professor.statistics(studentAnswer,correctAnswer)
        elif actionType==2:
            studentAnswer = int(input(str(number1)+" + "+str(number2)+" = "))
            correctAnswer = Professor.addition(number1,number2)
            professor.statistics(studentAnswer,correctAnswer)
        elif actionType==3:
            studentAnswer = int(input(str(number1)+" * "+str(number2)+" = "))
            correctAnswer = Professor.multiply(number1,number2)
            professor.statistics(studentAnswer,correctAnswer)
        elif actionType==4:
            studentAnswer = float(input(str(number1)+" / "+str(number2)+" = "))
            correctAnswer = Professor.divide(number1,number2)
            professor.statistics(studentAnswer,correctAnswer)
        if amountQuestions == professor.amountOfQuestions or amountQuestions < professor.amountOfQuestions:
            takeExtra = int(input("Do you want to take one more 1/yes, 0/no = "))
            if takeExtra==0:
                Professor.exam = False
    print("Student answered to "+str(professor.amountOfQuestions)+" questions")     
    print(str(professor.goodAnswer())+" is correct")   
    print(str(professor.badAnswer())+" is wrong")


