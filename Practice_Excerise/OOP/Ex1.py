"""Exercise 1: Creating a Student Class

Instructions:

Define a Student class with attributes like name and age. Include a method to display student information."""

#Defining a Student class with attributes like name and age
class student:
    def __init__(self, name , age):
        self.name = name
        self.age = age 
        
student_info1 = student("Sosina Ayele" , 20)
student_info2 = student("Yedidiya Ayele " , 18)

 #Displaying student information      
print(f"1st Student name => {student_info1.name} and her age is => {student_info1.age}")
print(f"2nd student name => {student_info2.name} and his age is => {student_info2.age}")
