import random
print("Number guessing game")


number = random.randint(1, 9)
chances = 0

print("Guess a very epik number (between 1 and 9):")
while chances < 5:

 
    guess = int(input("Enter your guess or have badluck: "))


    if guess == number:
        print("Congratulation YOU WONNNNNNNNNNNNNNN!!!")
        break

    elif guess < number:
        print("Your guess was too lowwwwwwwww: Guess a number higher than", guess)
    else:
        print("Your guess was too highhhhhhhhhhhhh: Guess a number lower than", guess)
    chances += 1

if not chances < 5:
    print("YOU LOSE!You are utter garbadge at this game. The number is", number)