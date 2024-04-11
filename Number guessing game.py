import random
#  Enter the lower limit of the range
Lower = int(input("Enter lower limit: "))
#  Enter the upper limit of the range
Upper = int(input("Enter upper limit: "))
#  Storing the random integer between the specified range
randno = random.randint(Lower, Upper)
#  Making a functiion for operation
def guess_number():
    i = 0
    while i == 0:
        user = int(input("Guess a number: "))
        if user > Lower and user < Upper:
            if user > randno:
                print("Wrong! It's too large, Try again!\n")
            elif user < randno:
                print("Wrong! It's too small, Try again!\n")
            elif user == randno:
                print("Fantastic! you guessed the right number.\n")
                i+=1
        else: 
            print("Number is below or out of range.")
guess_number()