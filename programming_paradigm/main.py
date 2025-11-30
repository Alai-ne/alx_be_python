import sys
from robust_division_calculator import safe_divide

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
    else:
        numerator_input = sys.argv[1]
        denominator_input = sys.argv[2]
        result = safe_divide(numerator_input, denominator_input)
        print(f"Result: {result}")
