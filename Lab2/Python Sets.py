#Set

#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates Not Allowed

#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Get the Length of a Set

#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Set Items - Data Types

#String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

#type()

#What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor

#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Access Items

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Add Items

#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add Sets

#Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add Any Iterable

#Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove Item

#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#Loop Items

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Two Sets

#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Keep ONLY the Duplicates

#Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#Keep All, But NOT the Duplicates

#Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#Return a set that contains all items from both sets, except items that are present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#True and 1 is considered the same value:
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)

#Python Dictionaries

#Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Dictionary Items

#Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Duplicates Not Allowed

#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Dictionary Length

#Print the number of items in the dictionary:
print(len(thisdict))

#Dictionary Items - Data Types

#String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#type()

#Print the data type of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#The dict() Constructor

#Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Accessing Items

#Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#Get the value of the "model" key:
x = thisdict.get("model")

#Get Keys

#Get a list of the keys:
x = thisdict.keys()

#Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#Get Values

#Get a list of the values:
x = thisdict.values()

#Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#Get Items

#Get a list of the key:value pairs
x = thisdict.items()

#Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Add a new item to the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


#Check if Key Exists

#Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change Values
  
#Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Adding Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Update Dictionary

#Add a color item to the dictionary by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Removing Items

#The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1984
}
thisdict.clear()
print(thisdict)

#Loop Through a Dictionary

#Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

#Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])

#You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

#You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)

#Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

#Copy a Dictionary

#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries

#Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Access Items in Nested Dictionaries

#Print the name of child 2:
print(myfamily["child2"]["name"])

