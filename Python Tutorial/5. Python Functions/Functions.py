'''
    A function in Python is a collection of connected statements that performs a single task. 
    Functions help in the division of our program into smaller, modular portions. 
    Functions help our program become more ordered and controllable as it grows in size. 
    It also eliminates repetition and makes the code reusable.
'''

# Types of Functins 1. User-defined 
def fun():
   print("Just a function having fun")
fun()
#                   2. Built-in
x = abs(-7.25) # abs is a built in function
print(x)

# Rules for Naming Functions in Python 
    # _print_hello
    # hello123
    # fahr_to_celsius

def square(x):
   """The function returns the square of the input number"""
   print("The square of "+str(x)+" is to be found.")
   return x * x
   
print("The square is: "+str(square(10)))   

'''
    The components of a python function definition are:
1. Keyword def:
In python, the keyword def is used to define a function. It marks the beginning of the function definition.

2. Name of the Function:
function_name is a unique identifier that is considered the name of the Function.

3. Parameters:
These are the values passed to the Function. 0 or more parameters can be included in the parentheses.

4. Colon(:): The:
represent the start of the indented function block.

5. docstring:
The optional docstring or document string is used to define what the Function does.

6. Statements:
These include the sequence of tasks that the Function is to perform. It can also use the pass keyword in case of no statements. These statements are usually indented at the same level (usually 2 or 4 spaces).

7. Return Statement:
The optional return statement symbolizes the return of values from the Function to the calling code.
'''
# Are Functions in Python Passed by Reference or Passed by Value?
# Python code to demonstrate call by value
print()
string = "Good Evening."
 
def greet(string):
   string = "Good Morning"
   print("Inside Function:", string)
   
greet(string)
print("Outside Function:", string)
# Python code to demonstrate call by reference
print()
def append_to_list(list1):
   list1.append(351)
   print("Inside Function: ", list1)
 
multiples_of_5 = [5,10,15,20,25,30]
append_to_list(multiples_of_5)
print("Outside Function: ", multiples_of_5)
