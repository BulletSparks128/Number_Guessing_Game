import random
import math

print ("This is program will take a range of numbers and pick a random number within that range.")
print ("Then it will ask you to guess the number.")

lowest = int(input("Type lowest number in range: "))
highest = int(input("Type highest number in range: "))

x = random.randint(lowest, highest)
print("\n\tYou've only ", round(math.log(highest - lowest + 1, 2)), " chances to guess the number!\n")

count = 0

while count < math.log(highest - lowest + 1, 2):
    count += 1

    guess = int(input("Guess the number: "))

    if x == guess:
        print("Congratulations  you did it in ", count, "try(tries)")
        break
    elif x > guess:
        print("You need to guess higher!")
    elif x < guess:
        print("You need to guess lower!")

if count >= math.log(highest - lowest + 1, 2):
    print("\nThe number id %d" % x)
    print("\tBetter Luck Next Time!")
