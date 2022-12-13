# Functions

# The following covers the basics of functions, but you can do even more with parameters.

# Functions are blocks of code that are only executed when called upon.
# That process is called "invoking a function."

def welcome(name):
    print("Hello! How's it going, " + name + "?")
    print("Welcome to the function file.")

# When you send information to a function, this is called passing an argument.
# Arguments are the information that you send to a function.
# The function needs a matching number of parameters, which is why
# we wrote welcome(name) instead of welcome().
# In order to add parameters to your function,
# list the parameters (which will be a temporary nickname) in the parentheses.

welcome("Aliyah")

# However, because we have written the function with parameters,
# you cannot just invoke a function with welcome().
# You will have to input an argument.

print("")
welcome("friend")
print("")

cat_name = "Navraj"
welcome(cat_name)

# In order to display an integer or number with a string, you need to cast the number as a string.

def hello(first_name, last_name, age):
    print("Hey, " + first_name + " " + last_name + "!")
    print("You're " + str(age) + ".")

print("")
hello("Tom", "Brady", 45)

print("")

# Keyword Arguments

# Keyword arguments are arguments preceded by an identifier when passed into a function.
# The order of the arguments doesn't matter, unlike positional arguments.
# When we use keyword args, Python knows the names of the arguments that our function receives.

hello(last_name="Gomez", age=30, first_name="Selena")

print("")

# Nested Function Calls

# Nested function calls are function calls inside of other function calls.
# The innermost function calls are resolved first and returned values are used as
# arguments for the next outer function. They're used to consolidate function calls
# into less lines of code. The following is an extreme example of a nested function call.

print(round(abs(float(input("Enter a whole, positive number: ")))))

print("")

# *Args

# *Args is a parameter that packs all arguments into a tuple.
# They're useful so that a function can accept a varying amount of arguments.

def add(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

print(add(3,5,3,7))

# Since tuples are immutable, if you want to change the value in a tuple, you should
# convert it to a different collection. The following is an example:

def combine(*args):
    total = 0
    args = list(args)
    args[0]=10
    for i in args:
        total += i
    return total

print(combine(3,5,3,7))


# **Kwargs

# **Kwargs is a parameter that packs all arguments into a dictionary.
# It's useful because a function can accept varying amounts of keyword arguments.
# **Kwargs is identical to *args except *args accepts varying amounts of positional
# arguments and packs them into a tuple while **kwargs accepts keyword arguments
# and packs them into a dictionary. The following is an example.

def welcome(**kwargs):
    print("Welcome, " + kwargs['first'] + " " + kwargs['last'] + "!")
    print("You're " + str(kwargs['height']) + " cm tall.")

welcome(last="Squarepants",first="Spongebob",middle="X",height=50)

# Here's another example if you want to include as many names as given.

def greeting(**names):
    print("Hi, ", end=" ")
    for key, value in names.items():
        print(value, end=" ")
    print("!")

greeting(title="Mr.", first="Samuel", middle="L", last="Jackson")
