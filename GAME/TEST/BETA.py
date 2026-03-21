import time
import random
import sys
import platform
from random import randint
#These are the req modules


cylinder_size = 8
odds = 4 / cylinder_size #Change this when developing the game.
days = 0
count = 0
#these all make the game functional. Too many to go in-depth with.



print("\n\nDragon-Breath Roulette")
time.sleep(1); print("Remaster of DEAD'S ROULETTE")
time.sleep(0.5); print(" Date of Production: 3/17/26")
time.sleep(0.5); print("  GitHub: NathanSlone2010")
time.sleep(0.5); print("   ALPHA BUILD")
time.sleep(0.5); print("    Rating: M for Mature")
#This is the introduction

con = input("[S/E] ").upper()
if con == "S":
    print("LOADING", end="")
    num_dots = random.randint(3, 7)
    for _ in range(num_dots):
        time.sleep(random.uniform(0.3, 1.0))
        print(".", end="", flush=True)
    print()
if con == "E":
    print("EXITTING", end="")
    num_dots = random.randint(3, 7)
    for _ in range(num_dots):
        time.sleep(random.uniform(0.3, 1.0))
        print(".", end="", flush=True)
        sys.exit()
        print()
if con not in ["S", "E"]:
    print("NOT VALID OPTION. STARTING PROGRAM ANYWAYS.")
#This allows starting the game.



while True:
	print("THE ROUND RACKS...\n")
	time.sleep(1); print("1. Shoot yourself..")
	time.sleep(1.5); print("2. Shoot the man across the table...")
	time.sleep(2); print("3. REVENGE....")
	choice = input(">>>")

	bullet = random.randint(1, cylinder_size)
	position = random.randint(1, cylinder_size)
	#Randomize the bullet each turn.

	if choice == "1":
		print("You point the shotgun at yourself")
		if random.random() < odds:
			time.sleep(1.5); print("The shotgun goes off.. You slump over the table...")
			time.sleep(0.5); print("'Rid of the body in the fire. Now!'")
			break
		else:
		    count == 1
		    time.sleep(0.3); print("A shell ejects... 'You survive for now..'")

	if choice == "2":
		time.sleep(0.5); print("You point it at the man. 'Good luck out there, bro..'")
		if random.random() < odds:
			time.sleep(0.5); ("HE SURVIVES.")
		else:
		    time.sleep(0.5); print("Fuck me... Goodbye.. BANG. The rounds go off.")
		    break

	if choice == "3":
		time.sleep(1); print("You point it at the guard...")
		if random.random() < odds:
			print("CLICK. The shell does not fire... 'DUMB BASTARD!")
			break
		else:
		   print("BANG. The gun goes off... 'Congratulations... You and Opponent both wins.")
		   break

	if choice not in ["1", "2", "3"]:
		print("MAKE A CHOICE!")