import random

words = ["Paris", "Gordes", "Marseille", "Nice", "Arles",]
hint1 = ["city", "village", "city", "city", "city"]
hint2 = ["fashion", "small", "oceanside", "tennis camp", "ancient"]

number = random.randint (0,4)

secretword = words[number]

guess = ""
counter = 0

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'length', 'first letter', 'last letter', or 'give up' if you need help.")
    guess = input()
    counter += 1

    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + "guesses")
        break

    elif guess == "hint1":
        print (hint1[number])

    elif guess == "hint2":
        print (hint2[number])

    elif guess == "first letter":
        print( secretword[0] )
        
        
