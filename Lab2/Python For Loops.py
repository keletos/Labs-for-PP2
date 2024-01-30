#Python For Loops
  
#Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
  
#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#The break Statement
  
#Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#The continue Statement
  
#Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function
  
#Using the range() function:
for x in range(6):
  print(x)

#Using the start parameter:
for x in range(2, 6):
  print(x)

#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

#Else in For Loop
  
#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested Loops

#Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#The pass Statement
    
for x in [0, 1, 2]:
  pass

#Creating a Function

def my_function():
  print("Hello from a function")

#Calling a Function
  
def my_function():
  print("Hello from a function")

my_function()

#Arguments

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Number of Arguments

#This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")

#Arbitrary Arguments, *args

#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitrary Keyword Arguments, **kwargs

#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Return Values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#The pass Statement

def myfunction():
  pass

#Positional-Only Arguments

def my_function(x, /):
  print(x)

my_function(3)

def my_function(x):
  print(x)

my_function(x = 3)

def my_function(x, /):
  print(x)

my_function(x = 3)

#Keyword-Only Arguments

def my_function(*, x):
  print(x)

my_function(x = 3)

def my_function(x):
  print(x)

my_function(3)

def my_function(*, x):
  print(x)

my_function(3)

#Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#Recursion

#Recursion Example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
