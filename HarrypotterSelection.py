gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Answer the following question")

# --- QUESTION 1 ---
print("Q1.Do you like Dawn or Dusk")
print("1)Dawn")
print("2)Dusk")
answer = int(input("Enter (1 or 2)"))

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input")


# --- QUESTION 2 ---
print("Q2) When I’m dead, I want people to remember me as")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
answer = int(input("Enter your choice(1-4)"))

if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print("Wrong Input")


# --- QUESTION 3 ---
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")


answer = int(input("Enter your choice(1-4)"))

if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print("Wrong input")


# --- FINAL SCORES & WINNER ---
# 1. Store scores in a dictionary for easy comparison
house_scores = {
    "Gryffindor": gryffindor,
    "Ravenclaw": ravenclaw,
    "Hufflepuff": hufflepuff,
    "Slytherin": slytherin
}



winning_house = max(house_scores, key=house_scores.get)
max_score = house_scores[winning_house]


print("\n--- FINAL SCORES ---")
print("Gryffindor score:", gryffindor)
print("Ravenclaw score:", ravenclaw)
print("Hufflepuff score:", hufflepuff)
print("Slytherin score:", slytherin)

print("\n--- WINNER ---")
if max_score > 0:
    print(f"The winning house is {winning_house} with a score of {max_score}!")
else:
    print("It's a four-way tie! No points were scored.")