import datetime
#Python has a module named time to handle time-related tasks. To use functions defined in the module, we need to import the module firs

time=datetime.datetime.now()
month=str(time.month)
day=str(time.day)
hour=str(time.day)
minute=str(time.minute)

foods=["Meat","chesse"]
print("\t\t WELCOME TO GROCERY SHOPING LIST")
print("\n Current date and time is :"+month+"/"+day+"/"+day+"/"+hour+"/"+minute)
print("your current items are "+foods[0]+" and "+foods[1]+" in your list.")

#input from user
#The append() method appends an element to the end of the list.
#The title() method returns a string where the first character in every word is upper case. Like a header, or a title.

food=input("\n Type of food to add to the grocery shopping list : ")
foods.append(food.title())

food=input("\n Type of food to add to the grocery shopping list : ")
foods.append(food.title())

food=input("\n Type of food to add to the grocery shopping list : ")
foods.append(food.title())

#Print and sort the list
#The sort() method sorts the list ascending by default.
print("\nHere is your grocery list: ")
print(foods)
foods.sort()
print("Here is your grocery list sorted: ")
print(foods)

#simulating shoping
print("\nSimulating grocery shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

# store is out of an item
#The insert() method inserts the specified value at the specified position.
#The pop() method removes the element at the specified position.
print("\n Current grocery list :"+str(len(foods))+" items")
print(foods)
no_item=foods.pop()
print("\n Sorry, The store is out of " + no_item +".")
new_food=input("what food would you like instead: ").title()
foods.insert(0, new_food)

print("\n Here is what remains on your grocery list : ")
print(foods)

