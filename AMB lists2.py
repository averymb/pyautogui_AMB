name = "Avery"

subjects = ["English", "Science", "Math", "History", "French"]

print ("My name is " + name)

for i in subjects:
    print("I take "  +  i  +  " as one of my classes.")


placesilove = ["Paris", "Punta Mita", "Gordes", "NYC", "Palm Beach", "Nantucket", "Cassis", "Fairlee", "Venice", "Croatia", "Nassau", "Greenwich"]

for i in placesilove:
    if i == "Gordes":
        print("Gordes is where I live part of the year")
    elif i == "Greenwich":
        print("Greenwich is where I live during the school year.")
    
foods = []



while True:
    print("What are your favorite foods? Type 'end' to stop program")
    answer = input()
    if answer == "end":
        break
    else:
        foods.append (answer)

for i in foods:
    print (i + " is one of your favborite foods.")
