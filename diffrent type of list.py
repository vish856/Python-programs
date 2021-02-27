print(         "\t\t\t\tsumaary table"          )
num1=['15','100','55','24']
num2=[15,100,55,42]
num3=[2.2,5.0,1.245,0.142857]
num4=[[1,2,3],[4,5,6],[7,8,9]]

print("\n\nthe variable in the string is" + str(type(num1))+ "." )
print("it contains the elemrnts"+ str(num1))
print("it element"+num1[0]+" is a"+str(type(num1[0])))

print("\n\nthe variable in the string is" + str(type(num2))+ "." )
print("it contains( the elemrnts"+ str(num2))
print("it element"+str(num2[0])+" is a"+str(type(num2[0])))

print("\n\nthe variable in the string is" + str(type(num3))+ "." )
print("it contains the elemrnts"+ str(num3))
print("it element"+str(num3[0])+" is a"+str(type(num3[0])))

print("\n\nthe variable in the string is" + str(type(num4))+ "." )
print("it contains the elemrnts"+ str(num4))
print("it element"+str(num4[0])+" is a"+str(type(num4[0])))

num1.sort()
num2.sort()
num3.sort()
num4.sort()

print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings: " + str(num1))
print("Sorted num_ints: " + str(num2))
print("\nStrings are sorted alphabetically while integers are sorted numerically!!!")
