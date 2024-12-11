import random

target = random.randint(1,100)

print("Hey buddy guess a number between 1 and 100 !!!")

while True:
  userInput = int(input("Take your guess bud!! will be fun:"))

  if(userInput == target):
    print("Booyahhh!! you've done it!")
    break

  elif(userInput > target):
    print("Uh-uh ! Take a smaller guess")

  elif(userInput < target):
    print("Uh-uh ! Take a bigger guess")

print("-----------GAME OVER----------------------")
