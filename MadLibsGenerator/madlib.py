# starts program
# y obtains values for mad libs, n asks for confirmation
def getResponse():
    response = input("In a creative rut? Try MIT's Mad Libs for Beginners. y/n")
    if response == "y":     # obtains values for mad libs
        getValues()

    elif response == "n":   # checks for confirmation
        sureResponse()

    else:
        invalidResponse()   # asks question again
        getResponse()

# prints error message
def invalidResponse():
    print("You have entered an invalid response. Please enter y/n only.")

# checks for confirmation
# y ends the program, n starts the program again
def sureResponse():
    confirm = input("Are you sure? y/n")
    if confirm == "y":      # program stops running
        print("Goodbye! Thank you for using MIT's Mad Libs for Beginners.")

    elif confirm == "n":    # start from beginning
        getResponse()

    else:                   # asks question again
        invalidResponse()
        sureResponse()

# obtains values for mad libs
# restarts program at the end of function
def getValues():
    object = input("Enter an object: ")

    if object == "":
        object == ""
    elif object[0] == "a" or object[0] == "e" or object[0] == "i" or object[0] == "o" or object[0] == "u":
        object = "an " + object
    else:
        object = "a " + object

    inspiration = input("Enter your inspiration: ")
    property = input("Enter a property: ")
    method = input("Enter the method: ")
    source = input("Enter the source: ")

    print("Design " + object + " inspired by " + inspiration + " that is " + property + " through " + method + " using " + source + ".")

    restartResponse()   # restart

# allows user to restart
# y obtains values for mad libs, n asks for confirmation
def restartResponse():
    proceed = input("Would you like to start again? y/n")
    if proceed == "y":      # start from beginning
        getValues()

    elif proceed == "n":    # checks for confirmation
        sureResponse()

    else:                   # asks question again
        invalidResponse()
        restartResponse()

getResponse()   # starts program


