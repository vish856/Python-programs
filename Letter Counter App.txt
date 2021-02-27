print("Welcome to the letter counter app by visitor bliss")
#Get user input
name = input("\n What is your name : ").title().strip()

#The title() method returns a string where the first character in every word is upper case.
#The strip() Remove spaces at the beginning and at the end of the string:
print("hello, " + name + "!")
print("\n I will count the number of times that a specific letter occurs in a message.")
message = input("\n Enter the message : ")     
letter = input("\n Enter the letter you want to count : ")
#standardrize the message
#lower(),Lower case the string:
message = message.lower()
letter = letter.lower()
#Get the count and display results.
#The string count() method returns the number of occurrences of a substring in the given string. In simple words
letter_count = message.count(letter)
print("\n" + name + ", your message has " + str(letter_count) + " " + letter +
"'s in it.")
