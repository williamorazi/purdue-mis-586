# ===========================================================================
# Assignment:   Assignment 1: A Basic Business and Engineering Calculator
# Date:         November 2, 2026
# Course:       Purdue University, MIS 586
# Student(s):   William Orazi, Preston Nicol
# Instructor:   Dr. Shoaib Khan
# Description:  A basic calculator application that handles common
#               arithmatic, simple engineering equations, and business
#               functions.
# ===========================================================================

# ===========================================================================
# SECTION 1: BASIC CALCULATOR
# ===========================================================================

# Placeholder for the six basic operations.
# Parameter: operation is the symbol the user chose (+, -, *, /, mod, ^)
# Later: prompt for two numbers, perform the operation, display the
# result, and handle division by zero and invalid number input.
def basic_operation(operation):
    print("The " + operation + " operation is not built yet.")


# Menu for the basic calculator. The user types an operation symbol,
# or 0 to go back to the main menu.
def basic_calculator_menu():
    operation = ""
    while operation != "0":
        print()
        print("--- Basic Calculator ---")
        print("  +    Addition")
        print("  -    Subtraction")
        print("  *    Multiplication")
        print("  /    Division")
        print("  mod  Modulus (remainder)")
        print("  ^    Exponentiation (power)")
        print("  0    Back to main menu")
        operation = input("Enter an operation symbol: ")

        # True when the user typed one of the six supported symbols
        is_valid_operation = (operation == "+" or operation == "-" or
                              operation == "*" or operation == "/" or
                              operation == "mod" or operation == "^")

        if is_valid_operation:
            basic_operation(operation)
        elif operation != "0":
            print("Invalid choice. Please enter +, -, *, /, mod, ^, or 0.")


# ================================================================================
# SECTION 2: ENGINEERING CALCULATIONS
# ================================================================================

# ---- 2a. Shape placeholders (area for 2D shapes, volume for 3D) ----

# Later: prompt for base and height, then display the triangle's area.
def triangle_area():
    print("Triangle area is not built yet.")


# Later: prompt for length and width, then display the rectangle's area.
def rectangle_area():
    print("Rectangle area is not built yet.")


# Later: prompt for the radius, then display the circle's area.
def circle_area():
    print("Circle area is not built yet.")


# Later: prompt for the side length, then display the cube's volume.
def cube_volume():
    print("Cube volume is not built yet.")


# Later: prompt for radius and height, then display the cylinder's volume.
def cylinder_volume():
    print("Cylinder volume is not built yet.")


# Later: prompt for radius and height, then display the cone's volume.
def cone_volume():
    print("Cone volume is not built yet.")


# ---- 2b. Unit conversion placeholders ----

# Later: prompt for a value in meters, then display it in feet.
def meters_to_feet():
    print("Meters to feet is not built yet.")


# Later: prompt for a value in kilograms, then display it in pounds.
def kilograms_to_pounds():
    print("Kilograms to pounds is not built yet.")


# ---- 2c. Engineering menus ----

# Menu for choosing a shape. 2D shapes give area, 3D shapes give volume.
def shapes_menu():
    choice = ""
    while choice != "0":
        print()
        print("--- Shapes: Area and Volume ---")
        print("  1. Triangle (area)")
        print("  2. Rectangle (area)")
        print("  3. Circle (area)")
        print("  4. Cube (volume)")
        print("  5. Cylinder (volume)")
        print("  6. Cone (volume)")
        print("  0. Back to engineering menu")
        choice = input("Enter your choice: ")
 
        if choice == "1":
            triangle_area()
        elif choice == "2":
            rectangle_area()
        elif choice == "3":
            circle_area()
        elif choice == "4":
            cube_volume()
        elif choice == "5":
            cylinder_volume()
        elif choice == "6":
            cone_volume()
        elif choice != "0":
            print("Invalid choice. Please enter a number from 0 to 6.")


# Menu for choosing a unit conversion. Anything other than the listed
# options is reported as an unsupported conversion.
def unit_conversion_menu():
    choice = ""
    while choice != "0":
        print()
        print("--- Unit Conversions ---")
        print("  1. Meters to feet")
        print("  2. Kilograms to pounds")
        print("  0. Back to engineering menu")
        choice = input("Enter your choice: ")
 
        if choice == "1":
            meters_to_feet()
        elif choice == "2":
            kilograms_to_pounds()
        elif choice != "0":
            print("Unsupported conversion. Please enter 0, 1, or 2.")


# Top-level engineering menu. Sends the user to shapes or conversions.
def engineering_menu():
    choice = ""
    while choice != "0":
        print()
        print("--- Engineering Calculations ---")
        print("  1. Area and volume of shapes")
        print("  2. Unit conversions")
        print("  0. Back to main menu")
        choice = input("Enter your choice: ")
 
        if choice == "1":
            shapes_menu()
        elif choice == "2":
            unit_conversion_menu()
        elif choice != "0":
            print("Invalid choice. Please enter 0, 1, or 2.")

# ===========================================================================
# SECTION 3: BUSINESS CALCULATIONS
# ===========================================================================
 
# Later: prompt for principal, annual interest rate, and number of
# periods, then display the compound interest earned.
def compound_interest():
    print("Compound interest is not built yet.")
 
 
# Later: prompt for fixed costs, sales price per unit, and variable
# cost per unit, then display the break-even point in units. Must
# handle a price that equals the variable cost (division by zero).
def break_even_point():
    print("Break-even point is not built yet.")
 
 
# Menu for choosing a business calculation.
def business_menu():
    choice = ""
    while choice != "0":
        print()
        print("--- Business Calculations ---")
        print("  1. Compound interest")
        print("  2. Break-even point")
        print("  0. Back to main menu")
        choice = input("Enter your choice: ")
 
        if choice == "1":
            compound_interest()
        elif choice == "2":
            break_even_point()
        elif choice != "0":
            print("Invalid choice. Please enter 0, 1, or 2.")

# ===========================================================================
# SECTION 4: MAIN MENU
# ===========================================================================

def main_menu():
    print("Welcome to the Engineering and Business Calculator!")
    choice = ""
    while choice != "0":
        print()
        print("===== Main Menu =====")
        print("  1. Basic Calculator")
        print("  2. Engineering Calculations")
        print("  3. Business Calculations")
        print("  0. Exit")
        choice = input("Enter your choice: ")
 
        if choice == "1":
            basic_calculator_menu()
        elif choice == "2":
            engineering_menu()
        elif choice == "3":
            business_menu()
        elif choice == "0":
            print("Thanks for using the calculator. Goodbye!")
        else:
            print("Invalid choice. Please enter 0, 1, 2, or 3.")
 
 
# Start the calculator program
main_menu()
