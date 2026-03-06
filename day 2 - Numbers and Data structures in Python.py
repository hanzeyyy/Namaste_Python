# to run some specific lines instead of running the whole code, press option+shift+E (for macbook)
# python is a strongly and dynamically typed language
# strongly typed means that the variables do have a type and type matters when performing any operation
# dynamically typed means that type of any variable is determined only during run time

#addition (+)
# any operation done between int and float ends as float
a = 1.0
b = 2
print(a+b)

# division (/)
# division of two integers gives float as outcome
# / -> floating division
a = 1
b = 2
print(a/b)

# if we want the division to occur as int in result, we use double division symbol
# // -> integer division
a = 1
b = 2
print(a//b)

#round operator
print(round(2.67))
print(round(2.67,1))

# modulus operator (%)
# tells us the remainder of the operation
print(5%3)

#absolute operator (abs)
print(abs(-3))

#power function -> pow()
print(pow(2,10))
print(2**10)
print(pow(2,-2))

x = 2.0
x = x.is_integer()
print(x)

x = 2.1
x = x.is_integer()
print(x)

### data structures ###
# using data structures, we can store multiple values in a variable
'''
Types of data structures
1. list
2. tuple
3. dictionary
'''

### 1. list ###
# it is group of values
ipl = ["MI", "CSK", "DC", "PSK", "RCB"]
print(type(ipl))

# we can use indexing in list as well
print(ipl[0])

#we can use slicing in list as well
print(ipl[0:2])

# Note: list are mutable i.e. we can change/modify them
ipl[1] = "KKR"
print(ipl[1])

# there are classes in list as well
# append() -> add element at the end of the list
ipl.append("CSK")
print(ipl)

# insert() -> insert element at particular index
ipl.insert(4, "LSG")
print(ipl)

# extend() -> extend list with another list
ipl.extend([1, 2, 3])
print(ipl)

# list can have any datatype in it, not necessarily only strings
print(type(ipl[2]))
print(type(ipl[8]))

# we can do indexing and slicing altogether as well
print(ipl[1][0:2])
print(ipl[1][0:2].lower())

# method 2 to create a list
# split() -> breaks string into a list
ipl_string = "KKR,CSK,MI,DC,LSG"
ipl_list = ipl_string.split(",")
print(ipl_list)

ipl_string = "KKR CSK MI DC LSG"
ipl_list = ipl_string.split(" ")
print(ipl_list)

# method 3 to create a list
# list() -> each element inside this will be an individual element in the list
python_list = list("python")
print(python_list)

# pop() -> to remove any element in the list, if no index is passed, last element is removed (by default)
print(ipl)
print(ipl.pop())
print(ipl)
print(ipl.pop(2))
print(ipl)

num = [2,4,5,1,3]
print(sum(num))
print(max(num))
print(min(num))

# sort() -> sort a list (work for both numbers and alphabets, but int should be in string format)
num.sort()
print(num)

# reverse() -> reverse a list
num.reverse()
print(num)

num_str = ["1", "2", "MI", "CSK"]
num_str.sort()
print(num_str)
# to get index of a particular element in the list
print(num_str.index("CSK"))

#list of list -> multiple list within a list
list_of_list = [[1,2], [2,4], ["Hanzala", "Rohit"]]
print(list_of_list)
print(list_of_list[0])
print(list_of_list[0][0:1])
print(list_of_list[2][0])
print(list_of_list[2][0][1])
print(len(list_of_list))

print(ipl)
ipl_new = ipl
print(ipl_new)

ipl_new.pop()
print(ipl_new)
print(ipl)
# ipl and ipl_new both have the same structure, so both gets affected

#copy() -> shallow copy
ipl_copy = ipl.copy()
print(ipl_copy)
ipl_copy.pop()
print(ipl_copy)
print(ipl)
# ipl list is intact

ipl = [[1,2], [3,4]]
ipl_copy = ipl.copy()
print(ipl_copy)
ipl_copy.pop()
print(ipl_copy)
print(ipl)

print(ipl_copy[0])
ipl_copy[0][0] = 2
print(ipl_copy)
print(ipl)
