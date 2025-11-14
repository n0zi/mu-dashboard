import math


def perform_calculation(number1: float) -> bool:
    """Return True and print sqrt when input is valid (non-negative float).

    Return False and print an error message when input is invalid for sqrt.
    """
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
        return True
    except ValueError:
        print("Error: Invalid input! Please enter a non-negative number.")
        return False


def main() -> None:
    # Loop until the user provides a valid number that sqrt can accept
    while True:
        try:
            number1 = float(input("Enter the number: "))
        except ValueError:
            print("Input must be a number (e.g. 3 or 3.5). Please try again.")
            continue

        # perform_calculation returns True when successful; break the loop then
        if perform_calculation(number1):
            break


if __name__ == "__main__":
    main()

