print("Hello World")
print("Hi, I am Hanzala. \nHow's it going")

'''there are 3 datatypes
1. string
2. integer / numbers / floating numbers
3. boolean'''

a = "IIT Bombay"
print(a)

#if we want to check the data type of "a"
print(type(a))

'''what is a class?
in python, whatever we create is a object
so, "a" is a object of class string'''

a = 2
print(type(a))
#now, "a' is an integer

a = 2.1
print(type(a))
#now, "a" is a floating integer

#STRING
city = "Mumbai"
'''
index:
Mumbai
012345

M - 0, U - 1, M - 2,B - 3, A - 4, I - 5

reverse index:
Mumbai
i = -1, a = -2, b = -3, m = -4, u = -5, M = -6
'''

#if we want to print the first index
print(city[0])

#reverse indexing
print(city[-1])

#slicing - cutting till desired length
print(city[0:3])

#what if we don't mention the starting or the closing index
print(city[:3])
print(city[0:])
print(city[-4:-1])
print(city[-4:])
print(city[-1:])

#if we want to find the length of any string
print(len(city))

#strings are immutable meaning strings cannot be changed once created
#string has different methods
print(city.upper())
print(city)
#change is temporary, to make it permanent, we have to re-assign it
city = city.upper()
print(city)

print(city.lower())
print(city)
city = city.lower()
print(city)

#boolean datatype returns either true or false
city = city.startswith("mu")
print(city)

str1 = "My name is Hanzala"
str2 = "I live in Mumbai"
str3 = str1 + " and " +str2
print(str3)

print("My name is Hanzala")
print("Hanzala live in Mumbai")
print("His age is 25")

first_name = "Hanzala"
last_name = "Ansari"
age = 25
print("My name is " + first_name)
print(first_name + " live in Mumbai")
print("His age is " + str(age))
#we are trying to concatenate (add) a string and a int that's why it shows error
#we use str() to avoid error

#formatted string: pass the variable
print(f"My name is {first_name} {last_name}")
print(f"{first_name} {last_name} lives in Mumbai")
print(f"My age is {age}")

#INPUT(): ask user to input
college = input("Enter your college name: ")
age = input("Enter your age: ")
print("My college is " + college + " and my age is " + (age))
print(f"My college is {college} and my age is {age}")
#here age is working since it is giving age as a string

#print(1+2)
#print(company*3)

num = 12.23
print(type(num))
print(int(num))

num1 = "12.23"
print(num1[-1])
print(type(num1))
print(float(num1))
print(int(float(num1)))
