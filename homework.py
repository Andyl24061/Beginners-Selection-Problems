print("You are exploring an island in search of some treasure.")

option1 = input("You arrive at a lake(swim/wait)")
if option1 == "wait":
    print("a boat arrives and you arrive on the island safely")
elif option1 != "swim":
    print("that was not an option. GAME OVER")
else:
    print("While swimming, a shark appears and eats you. GAME OVER")

option2 = input("You come to a cave(go in/walk away)")
if option2 == "go in":
    print("You step on a pressure plate and a boulder crushes you to death. GAME OVER")
elif option2 != "walk away":
    print("that was not an option. GAME OVER")
else:
    print("You walk around the cave and arrive at a crossroad.")

option3 = input("There are three paths(left/right/straight)")
if option3 == "left":
    print("You are trampled by a herd of wildebeest. GAME OVER")
if option3 == "straight":
    print("You get stung by a swarm of poisonous wasps. GAME OVER")
if option3 == "right":
    print("You march on and find the buried treasure! GG YOU WIN")


  
