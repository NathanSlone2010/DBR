import time
import random
import sys
import platform
from random import randint
#These are the req modules


print("NO ERRORS")
#This allows users to know if the program started correctly


cylinder_size = 6
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
        time.sleep(1); print(".", end="", flush=True)
        time.sleep(1); print(".", end="", flush=True)
        time.sleep(1); print(".", end="", flush=True)
        time.sleep(1); print(".", end="", flush=True)
        time.sleep(1.5); print("..", end="", flush=True)
        print()
if con == "E":
        print("EXITING", end="")
        time.sleep(1); print(".", end="", flush=True)
        time.sleep(2); print("..", end="", flush=True)
        print()
        sys.exit()
