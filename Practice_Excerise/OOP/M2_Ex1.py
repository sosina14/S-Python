num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

try:
    div = num2 / num1
except Exception:
    print("number cant divide by zero")
