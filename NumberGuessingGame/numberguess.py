# import random package
import random

# generate random number
generatedNumber = random.randint(1, 100)

# prints factors of random number
def print_factors():
    factors = []
    for i in range(1, generatedNumber + 1):
        if generatedNumber % i == 0:
            factors.append(i)
    del factors[0], factors[-1]
    return factors

# prints hints
def print_hints():
    if print_factors() != []:
        hint = random.choice(print_factors())
        print("The number is divisible by " + str(hint))
    else:
        if generatedNumber < 10:
            print("This number is a prime number. There are no more valid hints.")
        else:
            stringNumber = str(generatedNumber)
            firstDigit = stringNumber[0]
            secondDigit = stringNumber[-1]
            primeHints = ["This number is a prime number. Enter 0 for another hint.",
                          "This number starts with " + firstDigit + ". Enter 0 for another hint.",
                          "This number ends with " + secondDigit + ". Enter 0 for another hint."]
            print(random.choice(primeHints))

# main function for inputted number
def correctInput():
    while True:
        try:
            inputNumber = int(input("Enter a number between 1 to 99: "))
        except ValueError:
            print("Please enter a valid number.")
            pass
        else:
            if inputNumber in range(1, 100):
                if generatedNumber == inputNumber:
                    print("Congratulations! You won the game. The number is " + str(generatedNumber) + ".")
                    break
                elif generatedNumber <= inputNumber:
                    print("Try a lower number. Enter 0 for a hint.")
                else:
                    print("Try a higher number. Enter 0 for a hint.")
            elif inputNumber == 0:
                print_hints()
            else:
                print("Please enter a valid number between 1 to 99.")

# runs the function
correctInput()