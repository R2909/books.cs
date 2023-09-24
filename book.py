# BOOKS.CSV
from typing import List

def gcd_two_numbers(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two positive integers using Euclidean Algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def gcd_numbers(numbers: List[int]) -> int:
    """
    Calculate the greatest common divisor (GCD) of a list of positive integers using `gcd_two_numbers`.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty.")

    gcd_result = numbers[0]
    for num in numbers[1:]:
        gcd_result = gcd_two_numbers(gcd_result, num)
    return gcd_result

def get_numbers() -> List[int]:
    """
    Read a list of positive integers from the user, validate the inputs, and return the list.
    """
    numbers = []
    while True:
        try:
            user_input = input("Enter a positive integer (or 'q' to quit): ")
            if user_input.lower() == 'q':
                if not numbers:
                    raise ValueError("Input list cannot be empty.")
                return numbers

            num = int(user_input)
            if num <= 0:
                raise ValueError("Input must be a positive integer.")

            numbers.append(num)

        except ValueError:
            print("Invalid input. Please enter a valid positive integer or 'q' to quit.")

if __name__ == "__main__":
    try:
        numbers = get_numbers()
        gcd = gcd_numbers(numbers)
        print("The GCD of the given numbers is:", gcd)
    except ValueError as ve:
        print("Error:", ve)
