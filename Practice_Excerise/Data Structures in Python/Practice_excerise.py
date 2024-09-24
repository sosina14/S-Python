Exercise 1: Create a list to store names of your favorite fruits. Write code to access the second element and print it.
fruit_name = [ "Banana" , "Orange" , "Mango" , "pinapple" , "apple" ]
print (fruit_name[1])
Exercise 2: Define a dictionary to store information about your favorite book, including title, author, and genre. Use the method to retrieve the genre.
favorite_book = {
    "Title " : "Hashemal" , 
    "Author " : "Maebel_Fetene",
    "Genre " : 2016  }  
print (favorite_book)

Exercise 3: Write a program to generate a random set of numbers between 1 and ten. Use set operations to remove duplicates and display the unique numbers.

import random

# Generate a list of 10 random numbers between 1 and 10
random_numbers = [random.randint(1, 10) for _ in range(10)]

#print("Generated numbers with possible duplicates:", random_numbers)

# Convert the list to a set to remove duplicates
unique_numbers = set(random_numbers)

print("Unique numbers after removing duplicates:", unique_numbers)


