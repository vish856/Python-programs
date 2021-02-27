print("\t\t\tWelcome to Binary/hexa decimal conveter app")
#user input
value = int(input("\ncompute the binay & hexa decimal vaulues uo following decial numbers :"))
decimal = list(range(1, value+1))
binary = []
hexadecimal = []
for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("Generating lists...complete !")

#The bin() method converts and returns the binary equivalent string of a given integer.
#The hex() function converts an integer number to the corresponding hexadecimal string
#slicing The slice() function returns a slice object.
#A slice object is used to specify how to slice a sequence.
#You can specify where to start the slicing, and where to end

print("\nUsing slices, we will now show a portion of each list.")
lower_range = int(input("what decimal number would you like to start at :"))
upper_range = int(input("what decimal number would you like to start at : "))

print("\n Decimal values from" + str(lower_range) + "to" +str(upper_range)+ ":")
for num in decimal[lower_range-1:upper_range]:
    print(num)
print("\n Binary values from" + str(lower_range) + "to" +str(upper_range)+ ":")
for num in binary[lower_range-1:upper_range]:
    print(num)

print("\n Hexa Decimal values from" + str(lower_range) + "to" +str(upper_range)+ ":")
for num in hexadecimal[lower_range-1:upper_range]:
    print(num)

#Slicing in python means taking elements from one given index to another given index.
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].

#output of whole list
input("\n\n PRESS ENTR TO SEE THE ALL VALUE FROM 1 T0 "+str(value)+ ".")
print("decimal----binay---hexadecimall")
print("--------------------------------------------")
for d,b,h in zip(decimal,binary,hexadecimal):
    print(str(d)+"......"+str(b)+"...."+ str(h))
