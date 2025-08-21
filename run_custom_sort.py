from sort_package import sort

def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be positive.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    print("Enter package dimensions (in cm) and mass (in kg):")
    width = get_numeric_input("Width: ")
    height = get_numeric_input("Height: ")
    length = get_numeric_input("Length: ")
    mass = get_numeric_input("Mass: ")
    
    result = sort(width, height, length, mass)
    
    # Ternary operator for formatted output
    message = f"Package is {result.lower()}." if result != "REJECTED" else "Package is rejected due to size or weight."
    print(message)

if __name__ == "__main__":
    main()
