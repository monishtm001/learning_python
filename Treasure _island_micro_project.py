# Treasure Island Game for Shunti Boys
# _______ _______ _______ _______ _______ _______ _______ _______
#|       |       |       |       |       |       |       |       |
#|  T R  |  E A  |  S U  |  R E  |   I   |  S L  |  A N  |   D   |
#|_______|_______|_______|_______|_______|_______|_______|_______|#####


Name = str(input("Please enter your Pretty Name"))
print("Hello"+ " " + Name + "Welcome to treasure Isnald") 

Direction = input("Enter Your Preffered Direction to Move: - N/S/E/W").lower()

if Direction in ["n" ,"s" ,"w"]:
    LorW = input("Where you would likle to Move: Land / Water").lower()
    print("Welcome to Treasure Island- You have selected right Direction You May Proceed."+ " " + LorW )
    if LorW == "land":
        Door = input("Choose which door to enter: A/B/C") .lower()
        print("Congratulations You just skipped a beat. You May Proceed "+ " " + Door)
        if Door == "c":
            print("Congratulations You Just Found The Treasure")
        else:
            print("GAME OVER - You Choose The Wrong Door")
    elif LorW == "water":
        Choose_Action = input("Enter What u would like to do either Swim or wait for the Boat: - Swim/Boat").lower()
        print("You just choose to move through water:" + " " + Choose_Action)
        if Choose_Action=="swim":
            print("You Just Drowned LOL - Game Over")
            exit()
        elif Choose_Action=="boat":
            Door = input("Choose which door to enter: A/B/C") .lower()
            print("Congratulations You just skipped a beat. You May Proceed "+ " " + Door)
        if Door == "c":
            print("Congratulations You Just Found The Treasure")
        else:
            print("GAME OVER - You Choose The Wrong Door")
else:
    print("You just choose wrong direction - GAME OVER")
