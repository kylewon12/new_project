import random as r
import math

print("Kyle Won")

print("Hamza Aslam")

print("Melat Abera")

print("Bereket Zeggai")


# this can be deleted later, just wanted to make something random ;p
print("\n\t---- NUMBER GUESSER ----")
usr_num = input("Enter a numbers between 1-3: ")

n = (r.random() * 3) + 1
n = math.floor(n)


if int(usr_num) == n:
    print(f"LMAO! the computer also guessed {n}, YOU LOST")

else:
    print("NICE! you won")