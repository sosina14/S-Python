"""QUESTION => Numbers can add up quickly! Write a Python program using a for loop to calculate the sum of all the numbers in a list.
Create a list of numbers (e.g., numbers = [1, 5, 3, 9]).
Initialize a variable total to 0, which will store the running sum.
Use a for loop to iterate over the numbers list.
Inside the loop, add the current number (use the loop variable) to the total variable.
After the loop, print the final total value, which represents the sum of all the numbers in the list."""

#my try
total = 0
for number in [1, 5, 3, 9]:
    total += number 
    print(total)

#chatgpt love

# Define the list of numbers
numbers = [1, 5, 3, 9]

# Initialize total to 0
total = 0

# Use a for loop to iterate over the numbers list and calculate the sum
for number in numbers:
    total += number

# Print the final total value
print(total)
