import math
import sys

def add (a,b):
    return (a + b)

def mult(a,b):
	return (a * b)

def sub(a,b):
    return (a - b)


def div(a,b):
    return (a/b)


def sqrt(a):
    sqrt_result = math.sqrt(a)
    return (sqrt_result)


def square(a): 
    return (a * a)

def main ():

    print("1.Addition")
    print("2.Multiplication")
    print("3.Subtraction")
    print("4.Division")
    print("5.square root")
    print("6.square ")
    print("7.Exit program")

    choice = None

    while choice != 7:
        choice = int(input("Select an option:"))

        if choice  in range(5,7):
            x = int(input("Enter a number:"))            
        elif choice in range(1,5):
            x = float(input("Enter the first number:")) 
            y = float(input("Enter second number:"))        
        elif choice == 7:
            sys.exit(0)

        if choice ==1:
            add_result = add(x,y)
            print ("The sum is: ", add_result)
        elif choice ==2:
            mult_result = mult(x,y)
            print ( "The product is: ", mult_result)
        elif choice ==3:
            sub_result = sub(x,y)
            print ("The difference is: ", sub_result)
        elif choice ==4:
        
            div_result = div(x,y)
         
            print ("The division result is: ",div_result)
        elif choice ==5:        
            sqrt_result = sqrt(x)
            print ("The square root is: ",sqrt_result)
        elif choice ==6:
            square_result = square(x)
            print ("The square is:",square_result)

if (__name__=="__main__"):
    main()



