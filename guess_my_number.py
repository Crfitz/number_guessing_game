import time
from random import randrange
import sys

version = '0.2'
print("\nNumber Guessing Game\n"
	  f"Version {version}\n")
print("Fitzie Enterprises, LLC.\n"
"Copyright 2022; All rights reserved\n")

#player enters the uppermost number for range
end_num = input("Number range between 1 and: ")
#validates that the player enters a number
try:
	end_num = int(end_num)
except ValueError:
	print("\nInvalid entry\n"
	"Please enter a number.\n")
	sys.exit()
ans = randrange(1, end_num, 1)
close = ''
very_close = ''

#printing {ans} just for testing
#print(f"{ans}")
time.sleep(1)

print(f"\nI'm thinking of a number between 1 and {end_num}. \n")
print("I'll give you three guesses\n")

def how_close(num):
	"""Check how close guess is to correct number; based on how large the scope is, determines if guess is "close" or "very close." 
	"Very close" in a "1 to 100" game may be within 5, but that wouldn't make sense in a "1 to 10" game"""
	close = ''
	very_close = ''
	if num <= 10:
		close = int(2)
		very_close = int(1)
	elif num > 10 and num <= 20:
		close = int(3)
		very_close = int(1)
	elif num > 20 and num <= 30:
		close = int(4)
		very_close = int(2)
	elif num > 30 and num <= 50:
		close = int(8)
		very_close = int(3)
	elif num > 50:
		close = int(12)
		very_close = int(5)
	if close and very_close:
		return int(close), int(very_close)
	elif close:
		return int(close)
	

def high_low(guess):
	"""Compares guess to correct number; tells player if guess is too high/low; and how close"""
	close, very_close = how_close(end_num)

	if guess > ans:
		print("Too high!")
		if (guess - ans) <= very_close:
			print("But very very close!")
		elif (guess - ans) <= close:
			print("But close...")
	elif guess < ans:
		print("Too low!")
		if (ans - guess) <= very_close:
			print("But very very close!")
		elif int(ans - guess) <= close:
			print("But close...")
			

def win():
	"""When player guesses the correct number, "YOU WIN" is printed a bunch of times"""
	for iter in range(ans):
		print("* YOU WIN!!! *")
		time.sleep(0.25)
	sys.exit()
	
	
def compare(num, ans):
	try:
		num = int(num)
	except ValueError:
		print("Invalid entry!  Please try again")
		sys.exit()
#	else:
#		print(f"Checks out: {num}")
	
	while True:
		if num == '':
			print("Invalid entry (' ')")
			break
		if isinstance(num, int) == False:
			print("Invalid entry (isinstance)")
			break
		if num == ans:
			print("YOU GUESSED THE RIGHT NUMBER!\n"
			f"The correct answer was {ans}!\n")
			win()
			break
		elif num != ans:
			print("Incorrect. :-(  :-o :-(")
			high_low(num)
			return False
		else:
			print("Invalid entry (else)")
			return False
	

def validate(num):
	while True:
		if num == '':
			print("Invalid entry (null)")
			break
		#checks that 'num' is an integer
		elif isinstance(num, int) == False:
			print("Invalid entry (int)")
			break
		else:
			print("Checks out...")
	
	
# MAIN PROGRAM
while True:
	guess_1 = input("Guess number one: \n")
#	validate(guess_1)
	compare(guess_1, ans)
	guess_1 = int(guess_1)
	#compare(guess_1, ans)
	time.sleep(1)
	print()
	
	guess_2 = input("Guess number two: \n")
	compare(guess_2, ans)
	guess_2 = int(guess_2)
	time.sleep(1)
	print()
	
	guess_3 = input("Guess number three: \n")
	compare(guess_3, ans)
	guess_3 = int(guess_3)
	time.sleep(1)
	break

print()
print(f"\nThe correct answer was {ans}!")
