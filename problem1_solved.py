# Program to find the addition, subtraction, multiplication and division of 2 numbers using functions
def add(a,b):
	return (a + b)

def sub(a,b):
	return (a - b)

def mult(a,b):
	return (a * b)

def div(a,b):
	return ( a/b )

def main():
	x = int(input("Enter first number"))
	y = int(input("Enter second number"))
	add_result = add(x,y)
	sub_result = sub(x,y)
	mult_result = mult(x,y)
	div_result = div(x,y)
	print("Addition test:", add_result)
	print("Subtraction test:", sub_result)	
	print("Multiplication test:", mult_result)
	print("Division test:", div_result)
if __name__ == "__main__":
	main()
