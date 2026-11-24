a = int(input ("Enter first number : "))
b = int(input("Enter second number : "))
print("both the numbers are greater than 10: ", a>10 and b>10)
print("aleast one of the numbers is less than 5: ", a<5 or b<5 )
print("first number is not grearter than second: ", not a>b)

# comparison

Age = int(input(" Enter your age :  "))

if Age >= 18:
  print("you are an adult") 

else:
   print("you are a minor ") 


# membership

s = input(" Enter string : ")
print( "a" in s  )
print("python" not in s)
