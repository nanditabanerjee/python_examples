def main():
	# While loop example
	name = None
	while (name != "Nandita Banerjee"):		
		name = input("Please enter your full name: ")	# See, I did not use int(input(..)) because I will printant the string and not an integer

	print ("Thank you for entering your correct name.")
	exit(1)	# Use this line if you want to exit the program at any state. The 0 is an exit code

if (__name__=="__main__"):
    main()