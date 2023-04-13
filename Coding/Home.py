#Daily Python
import shutil

print(" ")
#print("Write a code to summate two numbers")

# x = 7
# y = 6

#sum = x + y

#print("Answer: ", sum)
#print(" ")

# " Creating Variable "

#character_name = "John"
#character_age = "25"
#is_male = False

#print ("There once was a man named " + character_name +", ")
#print ("he was " + character_age + " years old. ")
#print ("He really liked the name" + character_name +", ")
#print ("but didn't like being " + character_age)

#" String = plain text / backslash character"
#
#print("Giraffe\nAcademy")
#print("Giraffe\"Academy")
#print("Giraffe\Academy")

"Length of String"
"Replace Function, order of numbers"

#phrase = "Giraffe Academy"

#print(len(phrase))
#print(phrase[0])
#print(phrase.replace("Giraffe", "Gun"))

# print("Python Project")

# import random

#MAX_LINES = 3
#MAX_BET = 100
#MIN_BET = 1

#ROWS = 3
#COLS = 3

#symbol_count = {
 #   "A": 2,
  #  "B": 4,
   # "C": 6,
    #"D": 8
#}


#def get_slot_machine_spin(rows, cols, symbols):
    #all_symbols = []
    #for symbol, symbol_count in symbols.items():
     #   for _ in range(symbol_count):
     #       all_symbols.append(symbol)

    #columns = []
    #for _ in range(cols):
        #column = []
        #current_symbols = all_symbols = []
        #for _ in range(rows):
         #   value = random.choice(current_symbols)
        #    current_symbols.remove(value)
       #     column.append(value)

      #  columns.append(column)

     #return column


# def print_slot_machine(columns):
  #  for row in range(len(columns[0])):
   #     for i, column in enumerate(columns):
    #        if i != len(columns) - 1:
     #           print(column[row], "|")
      #      else:
       #         print(column[row])


#def deposit():
 #   while True:
  #      amount = input("How much would you like to deposit? $")
   #     if amount.isdigit():
    #        amount = int(amount)
     #       if amount > 0:
       #         break
      #      else:
        #        print("Insufficient amount, Must be greater than 0")
        #else:
         #   print("Enter a valid number")

    #return amount


#def get_number_of_lines():
 #   while True:
  #      lines = input("Enter Number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
   #     if lines.isdigit():
    #        lines = int(lines)
     #       if 1 <= lines <= MAX_LINES:
      #          break
       #     else:
       #         print("Enter Valid number of Lines")
        #else:
         #   print("Enter a value")

    #return lines


#def get_bet():
 #   while True:
  #      amount = input("What would you like to bet on each line? $")
   #     if amount.isdigit():
    #        amount = int(amount)
     #       if MIN_BET <= amount <= MAX_BET:
      #          break
       #     else:
        #        print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        #else:
         #   print("Please enter a number")

    #return amount


#def main():
 #   balance = deposit()
  #  lines = get_number_of_lines()
   # while True:
    #    bet = get_bet()
     #   total_bet = bet * lines

      #  if total_bet > balance:
       #     print(f"You do not have sufficient funds, your current balance is: ${balance}")
        #else:
         #   break

    # print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}. ")

     #slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    #print_slot_machine(slots)

    #main()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (2/101)

print("Working With Variables: ")

# Variable = Container for a value. Behaviour -> Exact to value it is
# x = Bro
# y = 21
# z = True

first_name = "Bro"
last_name = "Code"
full_name = first_name + " " + last_name
age = 21
age += 1 # This increases age by one
height = 184.5

# print(type(age))
# print(age)
# print(type(name))
# print("Hello " + name)

# Typecasting allows to convert variable into string to allow displaying "your age is: " with int: age (e.g) - "str" = typecast

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (3/101)

print (" ")
print("Your age is: " + str(age))

# Float allows numerical value with a decimal portion => essentially integer "int" with decimal
print("your height is: "+str(height)+"cm")

human = True
print("Are you Human?: " + str(human))
# print(type(human))

# Four basic data types: Boolean, String, Floats and Int

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (4/101)

print(" ")
print("Working with Multiple Assignments: ")

name = "Bro"
age = 21
attractive = True
# This ^ is symmetrical to that below ¬
name, age, attractive = "Bro", 21, True
print(name, age, attractive)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (5/101)

print(" ")
print("String Methods: ")
name = "bro"

print(len(name)) # Provides the length of the number in "name"
print(name.find("r")) # Finds the position of character in the name, i.e. B = first letter = 0, R = 1, O = 2.
print(name.capitalize()) # Capitalizes name
print(name.upper()) # Prints name in ALL Upper case.
print(name.lower()) # Prints name in ALL lower case
print(name.isdigit()) # Checks if string ONLY digit
print(name.isalpha()) # Checks if string contains only alphabetic letters

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (6/101)

print(" ")
print("Working with Typecasting: ")
# Type cast = converts one data type into another

x = 1
y = 2.0
z = "3"

x = float(x)
y = int(y)
z = int(z)
# can change all these to floats to achieve decimal place

print("X equates to: " + str(x))
print(y)
print(z)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (7/101)

print(" ")
print("Working with User Inputs: ")

#name = input("What is your name?: ")
#age = int(input("How old are you?: "))
#height = float(input("How Tall are you?: "))

age = age + 1
print("Hello "+ name)
print("You are "+str(age)+" Years old!")
print("You are "+str(height)+"cm tall.")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (8/101)

print(" ")
print("Working with Functions related to numbers: ")

import math

pi = -3.14
x = 4
y = 12
z = 10

print(round(pi))
print(math.ceil(pi)) # ceil rounds number up to the nearest integer
print(math.floor(pi)) # floor rounds a number down to the nearest integer
print(abs(pi)) # returns absolute value of number
print(pow(pi,2)) # raises a number to the power
print(int(math.sqrt(25))) # returns square root of value
print(max(x, y, z, pi)) # returns max value of given numbers
print(min(x, y, z, pi)) # returns min value

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (8/101)

print(" ")
print("Working with Slicing: ")
# There are 3 arguments in slicing: Staring index, stopping index and step index.
# [start:stop:step]

name = "Bro Code"
# create substring

first_name = name[0:3] # can leave index to name[:3]
last_name = name[4:8] # indexing is exclusive therefore would exclude character for "7" hence we include 8.
funky_name = name[0:8:2]
reverse_name = name[::-1] # returns name in reverse

# print(funky_name)
# print(reverse_name)

website1 = "http://google.com"
website2 = "http://aol.com"
slice = slice(7,-4) # 7 = start index (use of positive index), -4 = stop index

print(website1[slice])
print(website2[slice])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (9/101)

print(" ")
print("Working with If statements: ")
# If statemnt = executes code under condition being true

# age = int(input("How old are you?: "))

if age == 100:# double = checking if age is at that leve rather than changing age to 100
    print("You are a century old")
elif age >= 18:
    print("You will be registered as an adult.")
elif age < 0:
    print("Invalid Age.")
else:
    print("You will be registered as a child.")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (10/101)

print(" ")
print("Working with Logical Operators: ")

# temp = int(input("Temperature?: "))

# if not (temp>=0 and temp<=30):
  #  print("Stay inside. ")

# elif not (temp < 0 or temp >30):
   # print("Temperature is good. Go outside. ")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (11/101)

print(" ")
print("Working with While Loops: ")
# executes code unlimited times as long as conditions are true

name = ""

# while len(name) == 0:
  #  name = input("Enter your name: ")

# print("Hello "+name)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (12/101)

print(" ")
print("Working with For Loops: ")
# For loops are similar to while loops except only execute a limited amount of time.

# for i in range(50,100+1,2): # 2 is the step = amount of intervals counted by
  #  print(i)

# for i in "Bro Code":
  #  print(i)

#import time # need to import time module in order for loop to work in this case
#for seconds in range(0,1000000,1): # countdown starting from 10 down to 0, with intervals goind down by 1.
    #print(seconds)
    #time.sleep(1)
#print("Wag1 Sexy")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (13/101)

print(" ")
print("Working with Nested Loops: ")
# a loop inside a lopp essentially, where the inner loop will complete its process before the outer loop.

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
  #  for j in range(columns):
   #     print(symbol, end="")
    # print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (14/101)

print(" ")
print("Working with Loop Control statements: ")
# Break, continue and pass

# Break =   used to terminate the loop
# Continue = skips to next iteration of loop
# Pass = does nothing, essentially a placeholder

# while True:
   # name = input("Enter your name: ")
    # if name != "": # != means does not equal
      #  break

# phone_number = "123-456-7890"
# for i in phone_number:
  #  if i == "-":
   #     continue
    # print(i)

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)

# This (^) prints every number in the range of 1 to 21, disregarding 13 as we "pass" the integer.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (15/101)

print(" ")
print("Working with Lists: ")
# List is used to store multiple items within a single variable!

food =["Pizza","Hamburger", "Hotdog", "Spaghetti", "Water"]
food[0] = "Sushi" # changes element 0 from pizza to sushi!
food.append("Ice Cream") # adds an element to the list
food.remove("Hotdog") # removes element
food.pop() # Removes last element
food.insert(0, "Cake") # adds Cake to the position (0) of the list i.e Beginning whilst not removing any other element
food.sort() # sorts list in alphabetical order
# food.clear() # removes all elements in the list

# print(food[0]) # each item is an element and pertains to a given number 0 = pizza, 1 = hamburger
for x in food:
    print(x)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (16/101)

print(" ")
print("Working with 2D lists: ")
# Essentially a list with separate lists

drinks = ["Coffee", "Soda", "Tea"]
dinner = ["Pizza", "Hamburger", "Sushi"]
dessert = ["Cake", "Ice Cream"]

food = [drinks, dinner, dessert]
print(food)
print(food[0]) # Returns first set of element in each list
print(food[0][1]) # Returns the second element of the First list
print(food[1][0]) # Returns the first element of the Second list !

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (17/101)

print(" ")
print("Working with Tuples: ")
# Collections that are ordered and unchangable -> used to group together related data

student = ("Bro", 21,"Male")

print(student.count("Bro")) # count returns the amount of time requested value shows in tuple
print(student.index("Male"))

#for x in student:
  #  print(x)

#if "Bro" in student:
   # print("Bro is here")
#else:
   #'' print("Bro Not present") # to test change name in student variable

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (18/101)

print(" ")
print("Working with Sets: ")
# Set is a collected that is unordered, unindexed and cannot be duplicated in value.

utensils = {"fork", "spoon", "knife",}
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dishes.update(utensils)
#dinner_table = utensils.union(dishes)

print(utensils.difference(dishes)) # returns the value of what is in "utensils" that isn't in "dishes"
print(utensils.intersection(dishes)) # returns what the two sets have in common

#for y in utensils: # here "y" means => for the VARIABLES in Utensils _ this allows it to print whats inside rather than printing "{"fork", "spoon", "knife", "knife", "knife"}"
 #   print(y)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (19/101)

print(" ")
print("Working with Dictionary's: ")
# changeable, unorderder collection of unique key:value pairs.

capitals ={'USA': 'Washington DC',
           'India': 'New Delhi',
           'China': 'Beijing',
           'Russia': 'Moscow'}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Las Giddy"})
capitals.pop("China")

#print(capitals["Russia"])
#print(capitals.get('Germany')) # checks whether there is data for Germany in capitals otherwise returns "none"
#print(capitals.keys())
#print(capitals.values())
print(capitals.items())

for key,values in capitals.items():
    print(key,values)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (20/101)

print(" ")
print("Working with Indexes: ")
# gives access to a sequences element

name = "Bro Code!"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[0:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (21/101)

print(" ")
print("Working with Functions: ")
# Block of code only executed when called!

def hello(first_name,last_name,age):
    print("Greetings "+first_name+ " "+last_name+"!" + " You are "+str(age))
    print("Function Working!")

#my_name = "Bro"

#hello("Bro")
#hello(my_name)
hello("Bro","Code",22)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (22/101)

print("")
print("Working with return statements: ")
# Allows, function sends python values/object back to the caller

def multiply(number1, number2):
    result = number1 * number2
    return result

x = multiply(6,8)

print(x)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (23/101)

print("")
print("Working with keyword arguments: ")
# arguements preceeded by an identifier

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="Adeleye",middle="Adebola",first="Adetayo")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (24/101)

print("")
print("Working with nested function calls: ")
# function calls inside other function calls

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#print(round(abs(float(input("Enter a whole positive number here also: ")))))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (25/101)

print("")
print("Working with variable scope: ")
# region where variable is recognised

def display_name():
    name = "Adeleye"     # Becomes recognised as a global area locally scoped (Available only in this function)
    print(name)

display_name()
print(name)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (26/101)

print("")
print("Working with Args: ")

# Parameter that Packs all arguments into a tuple

def add(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(add(10,2,3))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  (27/101)

print("")
print("Working with Kwargs: ")

# Parameter that packs all arguments into a dictionary
# ** Double asterisk is key

def hello(**kwargs):
    #print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.",first="Adetayo",middle="Ade",last="Adeleye")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (28/101)

print("")
print("Woking with Formats: ")

animal = "cow"
obj = "moon"

#print("The {} jumped over the {}".format("cow","moon"))
#print("The {} jumped over the {}".format(animal,obj))
print("The {1} jumped over the {0}".format(animal,obj)) # Positional arguent
print("The {animal} jumped over the {obj}".format(animal="cow",obj="moon")) # Keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,obj))

name = "Ace"

print("Hello, my name is {}".format(name))
print("Hello, name is {:10}. Nice".format(name))
print("Hello, name is {:>10}. Nice ".format(name))
print("Hello, name is {:<10}. Nice".format(name))
print("Hello, name is {:^10}. Nice".format(name))

num = 3.14159
num1 = 1000

print("Pi is {:.2f}".format(num))
print("Number is {:,}".format(num1))
print("Number is {:b}".format(num1)) # displays value in binary form
print("Number is {:o}".format(num1)) # displays value in octal form
print("Number is {:X}".format(num1)) # displays value in hexadecimal form
print("Number is {:E}".format(num1)) # displays value in scientific notation

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (29/101)

print("")
print("Working with random module: ")

import random

x = random.randint(1,6) # returns random integer within range 1 - 6
print(x)
y = random.random() # returns a random float within the range of 0 and 1
print(y)

myList = ["rock","paper","Scissors"]
z = random.choice(myList) # picks a randon choice from the given list
print(z)

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards) # Shuffles the formation of the assortment of cards.
print(cards)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (30/101)

print("")
print("Working with Exception handling: ")
# event detected within execution disrupting flow of program

#try:
    #numerator = int(input("Enter a number: "))
   #denominator = int(input("Enter a number: "))
    #ans = numerator / denominator
#except ZeroDivisionError:
    #print("Cannot Divide by zero!")
#except ValueError:
   # print("Enter only Numbers!")
#except Exception:
    #print("Error Ocurred: (")
#else:
   # print(ans)
#finally:
    #print("This will always execute!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (31/101)

print("")
print("Working with file detection: ")
# Used to check whether a file exists on device

import os

path = "C:\\Users\Ade\\OneDrive\\Desktop\\pytest.txt"

if os.path.exists(path):
    print("Location exists! ")
    if os.path.isfile(path): # Checks whether path is a file or not.
        print("This is a file! ")
    elif os.path.isdir(path):
        print("This is a directory! ")
else:
    print("Location doesn't exist! ")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (32/101)

print("")
print("Working with File Reading: ")

try:
    with open(path) as file: # Already had file location saved as Path therefore "Path" var used.
        print(file.read())
except FileNotFoundError:
    print("File doesn't exist! ")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (33/101)

print("")
print("Working with File, Opening: ")

#text = "\nadeatadaeadeaadeade"

#with open("pytest2","a") as file: # w opens the file as write, r open the file as read. a appends "adds" to the file
 #   file.write(text)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (34/101)

print("")
print("Working with Files, Copying: ")
#copyfile() copies contents of a file
#copy() has the attributes of copyfile + permissions and destination can be a directory
#copy2() has all the above functions + copies metadata meaning file creation and modification times

#shutil.copyfile(path,'copied.txt') # (source, destination)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (35/101)

print("")
print("Working with Files, Moving: ")

#import os

#source = "copied.txt"
#destination = "C:\\Users\\Ade\\OneDrive\\Desktop" # remember to double the backslash

#try:
 #   if os.path.exists(destination):
   #     print("File already in Location! ")
  #  else:
    #    os.replace(source,destination)
     #   print(source+ "was moved! ")
#except FileNotFoundError:
 #   print(sourec+ " was not found!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (36/101)

print("")
print("Working with Files, Deleteing: ")

#import os
#import shutil

#path = "copied1.txt"

#try:
 #   os.remove(path) # deletes a file
  #  os.rmdir("empty_folder") # Allows User to delete empty directory
   # shutil.rmtree("folder") # Deletes a directory containing files
#except FileNotFoundError:
 #   print("Files doesn't exist, please check again! ")
#except PermissionError:
 #   print("Permission is required to delete file! ")
#except OSError:
 #   print("You cannot delte that folder using that function")
#else:
 #   print(path+" was deleted! ")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (37/101)

print("")
print("Working with Modules: ")
# File containing python code

#import testModule as msg
#from testModule import hello,bye

#msg.hello()
#msg.bye()

#hello()
#bye()

#help("modules")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (38/101)

print("")
print("Working with Games: Rock,Paper,Scissors! ")

#import random

#while True:
 #   list = ["rock","paper","scissors"]

  #  computer = random.choice(list)
   # player = None

    #while player not in list:
     #   player = input("rock, paper, or scissors?: ").lower()
      #  if player not in list:
       #     print("Please input valid selection. ")

    #if player == computer: # here is the sequence if player and computer pick the same
     #   print("Computer: ",computer)
 #       print("Player: ",player)
  #      print("Draw!")
   # elif player == "rock": # here is the sequence where player picks ROCK, conditioning for responses on what computer picks
    #    if computer == "paper":
     #       print("Computer: ", computer)
      #      print("Player: ", player)
       #     print("You Lose!")
       # if computer == "scissors":
        #    print("Computer: ", computer)
         #   print("Player: ", player)
          #  print("You Win!")

    #elif player == "Scissors": # here is the sequence where player picks Scissors, conditioning for responses on what computer picks
     #   if computer == "rock":
      #      print("Computer: ", computer)
       #     print("Player: ", player)
        #    print("You Lose!")
        #if computer == "Paper":
         #   print("Computer: ", computer)
          #  print("Player: ", player)
           # print("You Win!")

    #elif player == "paper": # here is the sequence where player picks PAPER, conditioning for responses on what computer picks
     #   if computer == "rock":
      #      print("Computer: ", computer)
       #     print("Player: ", player)
        #    print("You Win!")
        #if computer == "scissors":
         #   print("Computer: ", computer)
          #  print("Player: ", player)
           # print("You Lose!")

    #replay = input("Replay Game?: (Yes/No)").lower()
    #if replay != "yes":
     #   break
#print("Duece! ")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (39/101)

print("")
print("Working with Games: Quiz! ")







