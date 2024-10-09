# 1. Nested Decisions: The Adventure Game
# was using = instead of ==, else is not allowed to have conditions
place = input("Choose a place: forest or cave? ")
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    light = input("Do you: light a torch or proceed in the dark?")
    if light == "light a torch":
        print("You find treasure!")
    elif light == "proceed in the dark":
        print("Without a light source you find nothing of interest.")
    else:
        pass
else:
    pass