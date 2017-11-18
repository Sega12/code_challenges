from __future__ import print_function

# creates a list from 0 to 100
numList = list(range(101))

# ask user for input
user_input = input('Press "y" if you wanna see fizzbuzz in action: ').lower()

''' iterates through the list and
checks if num is divisble by number if y is entered '''
if user_input == "y":
	for num in numList:
		if num % 3 == 0 and num % 5 == 0:
			print("fizzbuzz")
		elif num % 3 == 0:
			print("fizz")
		elif num % 5 == 0:
			print("buzz")
		else:
			print(num)
else:
	print("Oh, that's too bad.")

