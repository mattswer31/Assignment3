# 2. Quick Decisions: The Event Planner
attendees = int(input("Enter number of attendees: ")) #needs int wrapper
venue = "large hall" if attendees > 100 else "conference room"
visuals = "projector" if attendees > 100 else "television"
audio = "audio system" if attendees > 100 else "tv speakers"
print(venue + " with " + visuals + " for visuals and " + audio + " for audio")
veg = input("Do you want vegetarian food? yes/no ")
print ("Hire Veggie Delight Caterers" if veg == "yes" else "Hire Gourmet Meals Caterers")