print("*******welcome to your MPH to MPS conversion program*****")
#Taking Input from user
mph=float(input("what is your speed in miles per hour:"))
#The float() function converts the specified value into a floating point number.
mps=mph*0.4774
mps=round(mps,2)
#The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals, round(number, digits)
print("your speed in mileper secon is : "+str(mps)+ ".")
#The str() function converts the specified value into a string.
