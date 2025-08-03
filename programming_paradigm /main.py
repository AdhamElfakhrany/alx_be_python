import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        return
    result = safe_divide(sys.argv[1], sys.argv[2])
    print(result)

if __name__ == "__main__":
    main()
