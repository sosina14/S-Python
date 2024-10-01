"""Exercise 2: Creating a Product Catalog

Instruction:

Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock."""

#Defining a Product class with attributes like name, price, and quantity
class product:
    def __init__(self, name , price , quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity
    

product1 = product ("T-shirt" , 8000, 20 )
product2 = product ("Hat" , 200 , 100 )
product3 = product ("Phone ", 3000, 10 )

# calculating the total value of products in stock.

total_value = (product1.price * product1.quantity) + (product2.price*product2.quantity) + (product3.price * product3.quantity)

print(f"Total value of ({product1.name}, {product2.name} and {product3.name}) is ${total_value}. ")









