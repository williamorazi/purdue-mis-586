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
#   2. Implemented the basic calculator functionality.
#   3. Implemented unit conversion functions, and the triangle area and cone
#      volume calculations for the engineering calculator.
#   4. Implemented the break-even point calculation for the business calculator.
#
# Preston Nicol:
#   1. Engineering Calculator
#        Area of a rectangle
#        Area of a circle
#        Volume of a cube
#        Volume of a cylinder
#   2. Business Calculator
#        Compound interest calculation
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


# Returns the value of pi to 15 decimal places.
def get_pi():
    return 3.141592653589793


# ===========================================================================
# SECTION 1: BASIC CALCULATOR
# ===========================================================================

# Prompts the user for two numbers, performs the specified operation, and
# displays the result.  If the user enters 'exit' for either number, the
# function returns to the basic calculator menu.  If the user attempts to
# divide by zero, the function displays an error message and returns to the
# basic calculator menu.
def basic_operation(operation):
    first_number = get_number("Enter the first number")
    if first_number is None:
        return

    second_number = get_number("Enter the second number")
    if second_number is None:
        return

    result = calculate_basic_operation(first_number, second_number, operation)

    print()
    if result is not None:
        print(str(first_number) + " " + operation + " " + str(second_number) + " = " + str(result))
    elif operation == "^":
        print("That power can't be calculated or very large results are out of range.")
    else:
        print("Can't divide by zero.  Please enter a second number other than zero.")


# Calculates the result of a basic arithmetic operation on two numbers.
# Returns None if the result can't be calculated: dividing by zero, or a
# power that's too large or doesn't produce a real number.  Otherwise,
# returns the result of the operation rounded to two decimal places.
def calculate_basic_operation(first_number, second_number, operation):
    try:
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            result = first_number / second_number
        elif operation == "mod":
            result = first_number % second_number
        elif operation == "^":
            result = first_number ** second_number

        return round(result, 2)
    except ZeroDivisionError:
        return None
    except OverflowError:
        return None


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

        # Validate the user's choice.
        is_valid_operation = (operation == "+" or operation == "-" or
                              operation == "*" or operation == "/" or
                              operation == "mod" or operation == "^")

        if is_valid_operation:
            basic_operation(operation)
        elif operation != "0":
            print()
            print("Invalid choice. Please enter +, -, *, /, mod, ^, or 0.")


# ===========================================================================
# SECTION 2: ENGINEERING CALCULATIONS
# ===========================================================================

# ---- 2a. Shape Area/Volume ----

# Prompts the user for the base and height of a triangle, calculates the area,
# and displays the result rounded to two decimal places.  If the user enters
# a negative base or height, the function displays an error message.
def triangle_area():
    base = get_number("Enter the triangle's base")
    if base is None:
        return

    height = get_number("Enter the triangle's height")
    if height is None:
        return

    area = calculate_triangle_area(base, height)

    print()
    if area is None:
        print("Invalid dimensions. The base and height can't be negative.")
    else:
        print("The area of the triangle is " + str(area) + " square units.")


# Calculates the area of a triangle given the base and height.  Returns None if
# either the base or height is negative.  Otherwise, returns the area rounded
# to two decimal places.
def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        return None
    else:
        return round(0.5 * base * height, 2)


# Prompts the user for the width and height of a rectangle, calculates the
# area, and displays the result rounded to two decimal places.  If the user
# enters a negative width or height, the function displays an error message.
def rectangle_area():
    width = get_number("Enter the rectangle's width")
    if width is None:
        return

    height = get_number("Enter the rectangle's height")
    if height is None:
        return

    area = calculate_rectangle_area(width, height)

    print()
    if area is None:
        print("Invalid dimensions. The width and height can't be negative.")
    else:
        print("The area of the rectangle is " + str(area) + " square units.")


# Calculates the area of a rectangle given the width and height, using the
# formula width x height.  Returns None if either the width or height is
# negative.  Otherwise, returns the area rounded to two decimal places.
def calculate_rectangle_area(width, height):
    if width < 0 or height < 0:
        return None
    else:
        return round(width * height, 2)


# Prompts the user for the radius of a circle, calculates the area, and
# displays the result rounded to two decimal places.  If the user enters a
# negative radius, the function displays an error message.
def circle_area():
    radius = get_number("Enter the circle's radius")
    if radius is None:
        return

    area = calculate_circle_area(radius)

    print()
    if area is None:
        print("Invalid dimensions. The radius can't be negative.")
    else:
        print("The area of the circle is " + str(area) + " square units.")


# Calculates the area of a circle given the radius, using the formula
# pi x radius^2.  Returns None if the radius is negative.  Otherwise,
# returns the area rounded to two decimal places.
def calculate_circle_area(radius):
    if radius < 0:
        return None
    else:
        return round(get_pi() * radius ** 2, 2)


# Prompts the user for the side length of a cube, calculates the volume, and
# displays the result rounded to two decimal places.  If the user enters a
# negative side length, the function displays an error message.
def cube_volume():
    side_length = get_number("Enter the cube's side length")
    if side_length is None:
        return

    volume = calculate_cube_volume(side_length)

    print()
    if volume is None:
        print("Invalid dimensions. The side length can't be negative.")
    else:
        print("The volume of the cube is " + str(volume) + " cubic units.")


# Calculates the volume of a cube given the side length, using the formula
# side length^3.  Returns None if the side length is negative.  Otherwise,
# returns the volume rounded to two decimal places.
def calculate_cube_volume(side_length):
    if side_length < 0:
        return None
    else:
        return round(side_length ** 3, 2)


# Prompts the user for the radius and height of a cylinder, calculates the
# volume, and displays the result rounded to two decimal places.  If the user
# enters a negative radius or height, the function displays an error message.
def cylinder_volume():
    radius = get_number("Enter the cylinder's radius")
    if radius is None:
        return

    height = get_number("Enter the cylinder's height")
    if height is None:
        return

    volume = calculate_cylinder_volume(radius, height)

    print()
    if volume is None:
        print("Invalid dimensions. The radius and height can't be negative.")
    else:
        print("The volume of the cylinder is " + str(volume) + " cubic units.")


# Calculates the volume of a cylinder given the radius and height, using the
# formula pi x radius^2 x height.  Returns None if either the radius or
# height is negative.  Otherwise, returns the volume rounded to two decimal
# places.
def calculate_cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        return None
    else:
        return round(get_pi() * height * radius ** 2, 2)


# Prompts the user for the radius and height of a cone, calculates the volume,
# and displays the result rounded to two decimal places.  If the user enters
# a negative radius or height, the function displays an error message.
def cone_volume():
    radius = get_number("Enter the cone's radius")

    if radius is None:
        return

    height = get_number("Enter the cone's height")

    if height is None:
        return

    volume = calculate_cone_volume(radius, height)

    print()
    if volume is None:
        print("Invalid dimensions. The radius and height can't be negative.")
    else:
        print("The volume of the cone is " + str(volume) + " cubic units.")


# Calculates the volume of a cone given the radius and height, using the
# formula (1/3) x pi x radius^2 x height.  Returns None if either the radius
# or height is negative.  Otherwise, returns the volume rounded to two
# decimal places.
def calculate_cone_volume(radius, height):
    if radius < 0 or height < 0:
        return None
    else:
        return round((1/3) * get_pi() * radius ** 2 * height, 2)


# ---- 2b. Unit Conversions ----

# Prompts the user for a length in meters, converts it to feet, and displays
# the result rounded to two decimal places.
def meters_to_feet():
    feet_per_meter = 3.28084
    prompt = "Enter a length in meters"

    meters = get_number(prompt)

    if meters is None:
        return

    feet = meters * feet_per_meter

    print()
    print(str(meters) + " meter(s) is equal to " + str(round(feet, 2)) + " feet.")


# Prompts the user for a weight in kilograms, converts it to pounds, and
# displays the result rounded to two decimal places.
def kilograms_to_pounds():
    pounds_per_kilogram = 2.20462
    prompt = "Enter a weight in kilograms"

    kilograms = get_number(prompt)

    if kilograms is None:
        return

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
            print()
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
            print()
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
            print()
            print("Invalid choice. Please enter 0, 1, or 2.")


# ===========================================================================
# SECTION 3: BUSINESS CALCULATIONS
# ===========================================================================

# Prompts the user for the principal, annual interest rate (as a
# percentage), and number of periods, then displays the compound interest
# earned and the ending balance.  If the user enters a negative value, or
# the result is too large to calculate, the function displays an error
# message.
def compound_interest():
    principal = get_number("Enter the principal amount")

    if principal is None:
        return

    annual_rate = get_number("Enter the annual interest rate as a percent (for example, 5 for 5%)")

    if annual_rate is None:
        return

    periods = get_number("Enter the number of periods (years)")

    if periods is None:
        return

    interest = calculate_compound_interest(principal, annual_rate, periods)

    print()
    if interest is None:
        print("Can't calculate compound interest.  The values can't be negative, and very large results are out of range.")
    else:
        print("The compound interest earned is $" + str(interest) + ".")
        print("The ending balance is $" + str(round(principal + interest, 2)) + ".")


# Calculates the compound interest earned on a principal amount, using the
# formula (P x (1 + i)^n) - P, where P is the principal, i is the annual
# interest rate, and n is the number of periods.  The rate is a percentage
# (for example, 5 for 5%) and is converted to a decimal first.  Returns None
# if any value is negative or the result is too large to calculate.
# Otherwise, returns the interest rounded to two decimal places.
def calculate_compound_interest(principal, annual_rate, periods):
    if principal < 0 or annual_rate < 0 or periods < 0:
        return None

    rate = annual_rate / 100

    try:
        return round(principal * (1 + rate) ** periods - principal, 2)
    except OverflowError:
        return None


# Prompts the user for the fixed costs, sales price per unit, and variable cost
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
        print("No break-even point.  Fixed costs can't be negative, and the sales price must be greater than the variable cost.")
    else:
        print("The break-even point is " + str(units) + " units.")


# Calculates the break-even point in units, given the fixed costs, sale price
# per unit, and variable cost per unit.  Returns None if the fixed costs are
# negative, or if the sale price is less than or equal to the variable cost 
# (will never break even).  Otherwise, returns the break-even point rounded up
# to the next whole unit.
def calculate_break_even(fixed_costs, sale_price, variable_cost):
    contribution_margin = sale_price - variable_cost

    if fixed_costs < 0 or contribution_margin < 0:
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

# Top-level menu. Sends the user to a calculator type and keeps running until
# they choose to exit the program.
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
