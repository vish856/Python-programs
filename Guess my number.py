import random
print("welcome to the Guess my number program")
name=input("Please enter your name : ").title().strip()
print("well "+str(name)+" I am thinking of an number b/w 1 and 20 ")
number = random.randint(1,20)

for guess in range(5):
    guess=int(input("\n\t\t\t Take a guess : "))

    if guess < number:
        print("Guess is low man.")
    elif guess > number:
        print("Guess is too high.")
    else:
        break

if number == guess:
    print("well you got me " +str(name)+ " brother")
else:
    print("Game over : The number I was thinking was" + str(number) +" .")

