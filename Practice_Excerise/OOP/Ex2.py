"""Exercise 2: Creating a Product Catalog

Instruction:

Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock."""

#Defining a Product class with attributes like name, price, and quantity
class product:
    def __init__(self, name , price , quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity

product1 = product ("T-shirt" , 8000, "20 peace")
product2 = product ("Hat" , 200 , "100 peace")
product3 = product ("Phone ", 3000, "10 peace")

# calculating the total value of products in stock.
total_value = product1.price + product2.price + product3.price
print(f"Total value of the all products is ${total_value}. ")










