print(" Welcome to fibonacci series through for loop")
num=int(input("How many Digits of fibonnaci sequence, you would like to compute: "))
fib=[1,1]
#-2 because we are already using do digit in our fib list[1,1]
for i in range(num-2):
     newfib=fib[i]+fib[i+1]
     fib.append(newfib)
print("\nThe first " + str(num) + " numbers of the Fibonacci Sequence are: ")
for number in fib:
     print(number)

golden =[]
for i in range(len(fib)-1):
     ratio=fib[i+1]/fib[i]
     golden.append(ratio)
print("\nThe corresponding Golden Ratio values are: ")
for ratio in golden:
     print(ratio)
print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")
