# ===========================================================================
# Assignment:   Assignment 1: A Basic Business and Engineering Calculator
# Date:         November 2, 2026
# Course:       Purdue University, MIS 586
# Student(s):   William Orazi, Preston Nicol
# Instructor:   Dr. Shoaib Khan
# Description:  A basic calculator application that handles common
#               arithmetic, simple engineering equations, and business
#               functions.
# ===========================================================================


# ===========================================================================
# Breakdown of Work:
# 
# William Orazi:
#   1. Implemented program scaffolding, including the menu and sub-menus for
#      each calculator type (basic, engineering, and business).
#   2. Implemented unit conversion functions for engineering calculations.
#   3. Implemented the break-even point calculation for business calculations.
#
# Preston Nicol:
#   1. Work Item
#   2. Work Item
#   3. Work Item
# ===========================================================================


# ===========================================================================
# SECTION 0: HELPER FUNCTIONS
# ===========================================================================

# Prompts the user for a number and returns it as a float. If the user
# types 'exit', the function returns None. If the user enters an invalid
# number, the function displays an error message and prompts for a new
# number.
def get_number(prompt):
    full_prompt = prompt + " or type 'exit' to return to the menu: "

    print()
    entry = input(full_prompt)

    while entry != "exit":
        try:
            return float(entry)
        except ValueError:
            print()
            print("Invalid input. Please enter a number.")
            print()
            entry = input(full_prompt)

    return None


# ===========================================================================
# SECTION 1: BASIC CALCULATOR
# ===========================================================================

# Placeholder for the six basic operations.
# Parameter: operation is the symbol the user chose (+, -, *, /, mod, ^)
# Later: prompt for two numbers, perform the operation, display the
# result, and handle division by zero and invalid number input.
def basic_operation(operation):
    print("The " + operation + " operation is not built yet.")


# Menu for the basic calculator.  A user can select one of six menu options,
# or return to the main menu.
def basic_calculator_menu():
    operation = ""
    while operation != "0":
        print()
        print("======= Basic Calculator =======")
        print("  +    Addition")
        print("  -    Subtraction")
        print("  *    Multiplication")
        print("  /    Division")
        print("  mod  Modulus")
        print("  ^    Exponentiation")
        print("  0    Back to Main Menu")
        print("=================================")
        print()
        operation = input("Enter an operation symbol: ")

        # True when the user typed one of the six supported symbols
        is_valid_operation = (operation == "+" or operation == "-" or
                              operation == "*" or operation == "/" or
                              operation == "mod" or operation == "^")

        if is_valid_operation:
            basic_operation(operation)
        elif operation != "0":
            print("Invalid choice. Please enter +, -, *, /, mod, ^, or 0.")


# ===========================================================================
# SECTION 2: ENGINEERING CALCULATIONS
# ===========================================================================

# ---- 2a. Shape Area/Volume ----

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


# ---- 2b. Unit Conversions ----

# Prompts the user for a length in meters, converts it to feet, and displays
# the result rounded to two decimal places.
def meters_to_feet():
    feet_per_meter = 3.28084
    prompt = "Enter a length in meters"

    meters = get_number(prompt)
    feet = meters * feet_per_meter

    print()
    print(str(meters) + " meter(s) is equal to " + str(round(feet, 2)) + " feet.")


# Prompts the user for a length in meters, converts it to feet, and displays
# the result rounded to two decimal places.
def kilograms_to_pounds():
    pounds_per_kilogram = 2.20462
    prompt = "Enter a weight in kilograms"

    kilograms = get_number(prompt)
    pounds = kilograms * pounds_per_kilogram

    print()
    print(str(kilograms) + " kilogram(s) is equal to " + str(round(pounds, 2)) + " pound(s).")


# ---- 2c. Engineering Menus ----

# Menu for choosing a shape. 2D shapes give area, 3D shapes give volume.
def shapes_menu():
    choice = ""
    while choice != "0":
        print()
        print("======= Shapes: Area and Volume =======")
        print("  1. Triangle (Area)")
        print("  2. Rectangle (Area)")
        print("  3. Circle (Area)")
        print("  4. Cube (Volume)")
        print("  5. Cylinder (Volume)")
        print("  6. Cone (Volume)")
        print("  0. Back to Engineering Menu")
        print("=========================================")
        print()
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
        print("======= Unit Conversions =======")
        print("  1. Meters to Feet")
        print("  2. Kilograms to Pounds")
        print("  0. Back to Engineering Menu")
        print("=================================")
        print()
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
        print("==== Engineering Calculations ====")
        print("  1. Area and Volume of Shapes")
        print("  2. Unit Conversions")
        print("  0. Back to Main Menu")
        print("==================================")
        print()
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


# Promps the user for the fixed costs, sales price per unit, and variable cost
# per unit, then prints the break-even point in units, rounded to the next whole
# unit.  If the sales price is less than or equal to the variable cost, the
# function prints a message indicating that there is no break-even point.
def break_even_point():
    fixed_costs = get_number("Enter the total fixed costs")

    if fixed_costs is None:
        return

    price = get_number("Enter the sales price per unit")

    if price is None:
        return

    variable_cost = get_number("Enter the variable cost per unit")

    if variable_cost is None:
        return

    units = calculate_break_even(fixed_costs, price, variable_cost)

    print()
    if units is None:
        print("No break-even point.  The sales price must be greater than the variable cost.")
    else:
        print ("The break-even point is " + str(units) + " units.")


# Calculates the break-even point in units, given the fixed costs, sale price
# per unit, and variable cost per unit.  Returns None if the sale price
# equals the variable cost (division by zero) or if the fixed costs are
# negative (will never break even).  Otherwise, returns the break-even point
# rounded up to the next whole unit.
def calculate_break_even(fixed_costs, sale_price, variable_cost):
    contribution_margin = sale_price - variable_cost

    if contribution_margin < 0:
        return None

    try:
        units = fixed_costs / contribution_margin
    except ZeroDivisionError:
        return None

    whole_units = int(units)

    if units - whole_units > 0:
        whole_units += 1

    return whole_units


# Menu for choosing a business calculation.
def business_menu():
    choice = ""
    while choice != "0":
        print()
        print("===== Business Calculations =====")
        print("  1. Compound Interest")
        print("  2. Break-Even Point")
        print("  0. Back to Main Menu")
        print("=================================")
        print()
        choice = input("Enter your choice: ")
 
        if choice == "1":
            compound_interest()
        elif choice == "2":
            break_even_point()
        elif choice != "0":
            print()
            print("Invalid choice. Please enter 0, 1, or 2.")


# ===========================================================================
# SECTION 4: MAIN MENU
# ===========================================================================

def main_menu():
    choice = ""
    while choice != "0":
        print()
        print("=========== Main Menu ===========")
        print("  1. Basic Calculator")
        print("  2. Engineering Calculations")
        print("  3. Business Calculations")
        print("  0. Exit")
        print("=================================")
        print()

        # Capture the user's choice and determine appropriate calculator
        # menu to display.  If the user enters an invalid choice, display
        # an error message and prompt for a new choice.
        choice = input("Enter a calculator option to begin: ")
 
        if choice == "1":
            basic_calculator_menu()
        elif choice == "2":
            engineering_menu()
        elif choice == "3":
            business_menu()
        elif choice == "0":
            print()
            print("Thanks for using the calculator. Goodbye!")
        else:
            print()
            print("Invalid choice. Please enter 0, 1, 2, or 3.")


# Start the calculator program.
main_menu()
