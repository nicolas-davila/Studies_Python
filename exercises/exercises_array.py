# Import the array module

from array import array

# Create an array of 5 integers

int_array = array('i', [1, 2, 3, 4, 5])

# Accessing elements in an array

print(int_array[0])  # Access the fisrt value

# Adding elements to an array

int_array.append(6)  # Add a new element to the end of the array

# Removing elements from an array

int_array.pop(3)  # Remove the fourth element from the array

# Modifying elements in an array

int_array[4] = 10  # Change the fifth element

print(int_array)

# Iterating over an array

for i in int_array:
    print(i)

# Verifying the existence of an element in an array

if 10 in int_array:
    print("10 is in the array")

# Matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ]

#Accessing the elements

fisrt_element = matrix[0][0]
second_element = matrix[1][1]

print(second_element)

#Modifying an element

matrix[0][1] = 10

print(matrix[0][1])

#Iterating over a matrix

for line in matrix:
    for column in line:
        print(column, end=" ")
    print() #Jumps to the next line

#Verifying the existence of an element in a matrix

if 10 in matrix[0]:
    print("10 is in the matrix")
else:
    print("10 is not in the matrix")