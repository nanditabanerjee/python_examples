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

def HCF(a,b):
    rem = a % b
    while (rem!=0):
        a = b
        b = rem
        rem = a % b 
        result = HCF(a,b)
    return b

def LCM(a, b):
    if a > b:
       greater = a
    else:
       greater = b

    while(True):
        if((greater % a == 0) and (greater % b == 0)):
           LCM = greater
           break
        greater += 1

    return LCM


def main ():

    print("1.Addition")
    print("2.Multiplication")
    print("3.Subtraction")
    print("4.Division")
    print("5.square root")
    print("6.square ")
    print("7.HCF")
    print("8.LCM")

    choice = None

    while choice != exit:
        choice = input("Select an option:")
        if choice in ('exit','EXIT','Exit'):
            sys.exit(0)
        elif (int(choice ) in range(5,7)):
            x = float(input("Enter a number:"))            
        elif (int(choice) in range(1,5)):
            x = float(input("Enter the first number:")) 
            y = float(input("Enter second number:"))               

        if (int(choice) ==1):
            add_result = add(x,y)
            print ("The sum is: ", add_result)
        elif (int(choice) ==2):
            mult_result = mult(x,y)
            print ( "The product is: ", mult_result)
        elif (int(choice) ==3):
            sub_result = sub(x,y)
            print ("The difference is: ", sub_result)
        elif (int(choice) ==4):
        
            div_result = div(x,y)
         
            print ("The division result is: ",div_result)
        elif (int(choice) ==5):        
            sqrt_result = sqrt(x)
            print ("The square root is: ",sqrt_result)
        elif (int(choice )==6):
            square_result = square(x)
            print ("The square is:",square_result)
        elif (int(choice)==7):
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number:"))
            num3 = int(input("Enter third number:"))
            result = HCF(num1,num2)
            result2 = HCF(result,num3)
            print("The HCF result is:",result2)
        elif (int(choice)== 8):
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number:"))
            num3 = int(input("Enter third number:"))
            result = LCM(num1,num2)
            result2 = LCM(result,num3)
            print("The LCM result is:",result2)
if (__name__=="__main__"):
    main()
