#Create 5 list comprehensions to solve the following 5 problems:

#Iterate a list of names to return a list of the names starting with H
names_list = ['Ken', 'Jonas', 'Irene', 'Peter', 'Josef', 'Hans', 'Grethe', 'Holger']
startLetter = 'H'
result = [index for index in names_list if index[0].lower() == startLetter.lower()]
print("The list contains following names with starting with H " + str(result))

#In one line create a list of the numbers 1-100 to the power of 3

numbers = [x**3 for x in range(100)]
print(numbers)

#Iterate a list of names to create a list of tuples where the tuples first value is the length of the name and the second is the name

names = ["John", "Shpat", "Mikkel", "Varr", "Jesper"]
result = [len(name) for name in names]

zipped = zip(result, names)
list(zipped)

#Iterate over each character in a string and get only those that are nummeric
string ='a1f56ds2a31dsf78asd7f'
count = 0
newstring1 =""  
    
for a in string: 
    if (a.isnumeric()) == False: 
        count+= 1
    else: 
        newstring1+= a  
print(newstring1)

#Using only a list comprehension wrapped in set() get all possible combination from throwing 2 dice
roll_combinations = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7)]
list(roll_combinations)

#Create 2 dictionary comprehensions to solve the following:

#Iterate a list of names and create a dictionary where key is the name and value is the length of the name
k = ["Jonas", "Grete", "Sigurt", "Peter", "Arne"]
v = [len(k) for k in names]

dictionary = dict(zip(k, v))
print(dictionary)
#Iterate a list of numbers and create a dictionary with (key, value) being (number, squareroot of number)
import math
k = [2,7,6,9,10,5]
v = [math.sqrt(n) for n in k]
dictionary1 = dict(zip(k,v))
print(dictionary1)
#Progammatically using loops create a small program to produce a dictionary with all the 2 dice throw combinations as keys and their likelyhood in percent as values
roll_combinations = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7)]
list(roll_combinations)
likelihood = 1/len(roll_combinations)
print(likelihood)
print(roll_combinations)