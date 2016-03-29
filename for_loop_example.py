def add(x, y):
	return (x + y)

def main():
	# Say that I want to print something or perform a function ten times.
	for i in range(0, 10):
		print ("I am printing the numbers 0-9. This is number ", i, ".")

	print ("I am adding the numbers from 5 to 9.")
	total = 0
	for i in range(5, 10):		
		print ("+ ", i)
		total = total + i

	print ("------")
	print ("  ", total)

if (__name__ == "__main__"):
	main()