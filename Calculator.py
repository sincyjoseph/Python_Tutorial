from CalculatorFunctions import addition,substraction,multiplication,division

while(True):
    numb1 = input("Enter Number 1: ")
    numb2 = input("Enter Number 2: ")

    print("\n**************Calculator Menu**************")
    print("\t1 . Addition")
    print("\t2 . Substraction")
    print("\t3 . Multiplication")
    print("\t4 . Division")
    print("\t5 . Quit")
    print("*********************************************")

    choice = input("Enter your choice:")

    if(choice == 1):
        result = addition(numb1, numb2)
        print ("\tResult: "+ str(result))
    elif (choice == 2):
        result = substraction(numb1, numb2)
        print ("\tResult: "+ str(result))
    elif (choice == 3):
        result = multiplication(numb1, numb2)
        print ("\tResult: "+ str(result))
    elif (choice == 4):
        result = division(numb1, numb2)
        print ("\tResult: "+ str(result))
    elif (choice == 5):
        result = quit(0)
    else:
        print ("\tGive valid choice")