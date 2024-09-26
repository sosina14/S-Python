# main.py (Program)
import arithmetic_operations

def main():
    print("Arithmetic Operationsa")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    arithmetic_operations.perform_operation(num1, num2, operation)
    # result =  print(f"Result: {result}")

if __name__ == "__main__":
    main()
    
