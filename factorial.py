import math

print("\n Factorial calculation")
number=int(input("enter the number"))
print(str(number)+"! =", end="")
print(number)
for i in range(1, number):
     print(str(i), end="*")
print(str(number))

fact = math.factorial(number)
print("\nHere is the result from the math library: ")
print("The factorial of " + str(number) + " is " + str(fact) + "!")

fact = 1
for i in range(1, number+1):
     fact = fact*i
print("\nHere is the result from my own algorithm: ")
print("The factorial of " + str(number) + " is " + str(fact) + "!")
print("\nIt is shown twice that " + str(number) + "! = " + str(fact) + " (with excitement!)")
