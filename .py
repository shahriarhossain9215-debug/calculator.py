"""
Simple Command-Line Calculator

This script provides basic arithmetic operations via user input.
It supports addition, subtraction, multiplication, and division.
"""

from typing import Union

# Define operation functions with type hints and docstrings
def add(x: float, y: float) -> float:
    """Return the sum of x and y."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Return the difference of x and y."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Return the product of x and y."""
    return x * y

def divide(x: float, y: float) -> Union[float, str]:
    """Return the quotient of x and y, or 'Error' if dividing by zero."""
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Dictionary to map user choices to operations for better structure
OPERATIONS = {
    '1': ('Add', add),
    '2': ('Subtract', subtract),
    '3': ('Multiply', multiply),
    '4': ('Divide', divide),
}

def get_valid_choice() -> str:
    """Prompt user for a valid operation choice."""
    while True:
        choice = input("Enter choice (1/2/3/4): ").strip()
        if choice in OPERATIONS:
            return choice
        print("Invalid choice. Please select 1, 2, 3, or 4.")

def get_valid_number(prompt: str) -> float:
    """Prompt user for a valid number, handling invalid inputs."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to run the calculator."""
    print("Select operation:")
    for key, (name, _) in OPERATIONS.items():
        print(f"{key}. {name}")

    choice = get_valid_choice()
    num1 = get_valid_number("Enter first number: ")
    num2 = get_valid_number("Enter second number: ")

    op_name, op_func = OPERATIONS[choice]
    result = op_func(num1, num2)
    print(f"{num1} {op_name.lower()} {num2} = {result}")

if __name__ == "__main__":
    main()