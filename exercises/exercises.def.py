#Def exercises for python

def function_name(parameters): #parameters are the inputs of the function
    #body of the function
    #code to be executed
    return #"result" --> #optional, if the function returns something

#Example

def welcome(name):
    message = f"Hello, {name}! How are you?"
    return message

username = "Nicolas"
welcome_user = welcome(username)

print(welcome_user)

#No return function

def show_value_squared (number):
    square = number * number
    print(f"The square of the number {number} is {square}!")

show_value_squared(5) 