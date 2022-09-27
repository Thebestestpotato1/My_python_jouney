name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
"""Learned an followed 'https://www.youtube.com/watch?v=DLn3jOsNRVE&list=PLYY49OzhMaZpPueW5Oi2C5TFTUdZlwFdQ&index=3&t=1504s' Tech with Tim. """

answer = input("You're on a dirt road and you approach a Y, do you go right or go left? :").lower()

if answer == "left":
    answer = input("You approach a river, do you 'swim' or 'go around' the river?").lower()

    if answer == "swim":
        print("You swam but perished to the tides.")
    elif answer == "go around":
        print("You walked around, ran out of water and drank the river. You got dysentery and died.")
    else:
        print("Not a valid option, you lose.")
elif answer == "right":
    answer = input("You approach a bridge, looks kinda sketch. wanna 'cross' or 'nah'?").lower()

    if answer == "cross":
        answer = input("You made it to work, do you say hi to you boss?").lower()
        if answer == "yes":
            print("He says hi back")
        elif answer == "no":
            print("Wow, not everything needs to be a battle bud. ")
    elif answer == "nah":
        print("You stayed home, lost your job and starved to death.")
    else:
        print("Not a valid option")
else:
    print("Not a vaild option.")
print("Thanks for playing", name)