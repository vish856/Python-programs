print("\t\t\t WLECOME T10 CRICKETER LSIT OF YOUR'S")
cricket=[]
player=input("who will your main batsman : ").title()
cricket.append(player)
player=input("who will your main bowler : ").title()
cricket.append(player)
player=input("who will your  captain : ").title()
cricket.append(player)
player=input("who will your main kepper : ").title()
cricket.append(player)
player=input("who will your main fielder : ").title()
cricket.append(player)

print("\t\t\t\t Yor are starting 5 for upcomig T10 tournament")
print("\t\t\t\t\t Main Batsmen :\t\t" + cricket[0])
print("\t\t\t\t\t Main Bowler :\t\t" + cricket[1])
print("\t\t\t\t\t Main captain :\t\t" + cricket[2])
print("\t\t\t\t\t Main kepper :\t\t" + cricket[3])
print("\t\t\t\t\t Main fielder :\t\t" + cricket[4])

length = len(cricket)
print("oh no,"+ cricket.pop(0)+" is not available, He is in a Party")
print("your roaster have"+ str(length))

added_player = input("Who will take " + cricket[0] + "'s spot: ").title()
cricket.insert(0, added_player)

print("\t\t\t\t\t Main Batsmen :\t\t" + cricket[0])
print("\t\t\t\t\t Main Bowler :\t\t" + cricket[1])
print("\t\t\t\t\t Main captain :\t\t" + cricket[2])
print("\t\t\t\t\t Main kepper :\t\t" + cricket[3])
print("\t\t\t\t\t Main fielder :\t\t" + cricket[4])

print("\nGood luck " + cricket[2] + " you will do great!")
cricket_length = len(cricket)
print("Your roster now has " + str(cricket_length) + " players.")

