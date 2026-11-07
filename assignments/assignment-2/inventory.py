# Lab 2: Sales and Inventory Management System
# Group 3 Members: William Christopher Orazi & Christopher Kuhl

# datetime gives us the date and time of each sale.
# json lets us save our data to a file and load it back later.
import datetime
import json


# ------------------------------------
# Group 3's Product Catalog - Chris Kuhl
# Stores product information using a dictionary.
# ------------------------------------

product_catalog = {
    "P1": {"Name": "Laptop", "Price": 899.99, "Stock": 8},
    "P2": {"Name": "Keyboard", "Price": 49.99, "Stock": 20},
    "P3": {"Name": "Mouse", "Price": 24.99, "Stock": 35},
    "P4": {"Name": "Monitor", "Price": 199.99, "Stock": 12},
    "P5": {"Name": "USB Drive", "Price": 14.99, "Stock": 50}
}

# This list stores our sales history. Each sale is saved as a
# dictionary and added to this list when a sale is made.
sales_history = []


# ------------------------------------
# Format Money Helper - William Orazi
# One small function so every dollar amount is shown the same way,
# always with two decimal places (149.9 shows as $149.90).
# ------------------------------------

def format_money(amount):
    total_cents = round(amount * 100)   # 149.9 becomes 14990
    dollars = total_cents // 100        # floor division gives 149
    cents = total_cents % 100           # modulus gives the remainder, 90

    # Add a leading zero for 1 to 9 cents so 5 cents shows as .05
    if cents < 10:
        return "$" + str(dollars) + ".0" + str(cents)
    else:
        return "$" + str(dollars) + "." + str(cents)


# ------------------------------------
# View Catalog Function - Chris Kuhl
# Displays all products currently in the catalog.
# (Price formatting added by William Orazi.)
# ------------------------------------

def view_catalog():
    print("\nGroup 3's Product Catalog")
    print("--------------------------")

    # Loop through the dictionary and display product details
    for product_id, product_info in product_catalog.items():
        print("Product ID:", product_id)
        print("Name:", product_info["Name"])
        # format_money() shows the price with two decimals, like $899.99
        print("Price:", format_money(product_info["Price"]))
        print("Stock:", product_info["Stock"])
        print()


# ------------------------------------
# Update Product Function - Chris Kuhl
# Allows a user to update a product's price or stock quantity.
# (Price check and .strip() added by William Orazi.)
# ------------------------------------

def update_product():
    # Display products before updating
    view_catalog()

    # Ask the user which product to update. I added the .upper()
    # to account for the user entering either uppercase
    # or lowercase letters for the product id. The .strip()
    # removes any extra spaces before or after it. Both help
    # prevent errors from simple typing mistakes.
    product_id = input("Enter Product ID to update: ").strip().upper()

    # Make sure the product exists
    if product_id not in product_catalog:
        print("Product not found.")
        return

    print("\n1. Update Price")
    print("2. Update Stock")

    choice = input("Enter choice: ")

    # Update price
    if choice == "1":
        try:
            new_price = float(input("Enter new price: "))

            # Price must be positive, same idea as the stock check below
            if new_price <= 0:
                print("Price must be greater than zero.")
            else:
                product_catalog[product_id]["Price"] = new_price
                print("Price updated successfully.")

        except ValueError:
            print("Invalid price entered.")

    # Update stock quantity
    elif choice == "2":
        try:
            new_stock = int(input("Enter new stock quantity: "))

            if new_stock < 0:
                print("Stock cannot be negative.")
            else:
                product_catalog[product_id]["Stock"] = new_stock
                print("Stock updated successfully.")

        except ValueError:
            print("Invalid stock quantity.")

    else:
        print("Invalid option.")


# ------------------------------------
# Record Sale Function - William Orazi
# Does the business work of a sale: calculates the total,
# reduces stock, and saves a sale record to the sales history.
#
# No 'global' keyword is needed here. We change the contents of
# product_catalog and sales_history, but we never reassign them.
# ------------------------------------

def record_sale(product_id, quantity):
    # Total for this sale, rounded to cents
    total_amount = round(product_catalog[product_id]["Price"] * quantity, 2)

    # Reduce the stock on hand
    product_catalog[product_id]["Stock"] -= quantity

    # Build the sale record as a dictionary.
    # Sale IDs start at S1001 and count up with each sale.
    # The date is stored as text so it prints cleanly and can be saved to JSON.
    sale = {
        "Sale ID": "S" + str(1001 + len(sales_history)),
        "Date and Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Product ID": product_id,
        "Quantity": quantity,
        "Total Amount": total_amount
    }

    # Add the sale to our list of sales
    sales_history.append(sale)

    return sale


# ------------------------------------
# Make a Sale Function - William Orazi
# Gets the product and quantity from the user, checks for
# errors, then calls record_sale() to complete the sale.
# ------------------------------------

def make_sale():
    # Show the catalog so the user can see IDs, prices, and stock
    view_catalog()

    # .strip() removes extra spaces and .upper() lets the user
    # type either "p1" or "P1"
    product_id = input("Enter Product ID to sell: ").strip().upper()

    # Make sure the product exists
    if product_id not in product_catalog:
        print("Product not found.")
        return

    product_name = product_catalog[product_id]["Name"]
    stock = product_catalog[product_id]["Stock"]

    # Nothing to sell if the product is out of stock
    if stock == 0:
        print("Sorry,", product_name, "is out of stock.")
        return

    # Make sure the quantity is a whole number
    try:
        quantity = int(input("Enter quantity to sell: "))
    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        return

    # Make sure the quantity is at least 1
    if quantity <= 0:
        print("Quantity must be at least 1.")
        return

    # Don't let the user buy more items than are in stock
    if quantity > stock:
        print("Not enough stock. Only", stock, "of", product_name, "available.")
        return

    # Everything checks out, so complete the sale
    sale = record_sale(product_id, quantity)

    print("\nSale completed!")
    print("Sale ID:", sale["Sale ID"])
    print("Product:", product_name)
    print("Quantity:", quantity)
    print("Total Sale Amount:", format_money(sale["Total Amount"]))
    print("Remaining Stock:", product_catalog[product_id]["Stock"])


# ------------------------------------
# View Sales History Function - William Orazi
# Displays every sale in the order it was made.
# ------------------------------------

def view_sales_history():
    print("\nGroup 3's Sales History")
    print("--------------------------")

    if len(sales_history) == 0:
        print("No sales have been made yet.")
        return

    for sale in sales_history:
        # The sale stores the Product ID, so we look up the name in the catalog
        product_name = product_catalog[sale["Product ID"]]["Name"]

        print("Sale ID:", sale["Sale ID"])
        print("Date and Time:", sale["Date and Time"])
        print("Product:", product_name)
        print("Quantity:", sale["Quantity"])
        print("Total Sale Amount:", format_money(sale["Total Amount"]))
        print()


# ------------------------------------
# View Sales Statistics Function - William Orazi
# Shows total sales revenue, the best-selling product, and the
# product with the highest revenue, then ranks products by revenue.
# ------------------------------------

def view_sales_statistics():
    print("\nGroup 3's Sales Statistics")
    print("--------------------------")

    if len(sales_history) == 0:
        print("No sales have been made yet.")
        return

    # Total revenue across every sale
    total_revenue = sum([sale["Total Amount"] for sale in sales_history])

    # Add up units sold and revenue for each product.
    # .get(product_id, 0) starts a product at 0 the first time we see it.
    units_by_product = {}
    revenue_by_product = {}

    for sale in sales_history:
        product_id = sale["Product ID"]
        units_by_product[product_id] = units_by_product.get(product_id, 0) + sale["Quantity"]
        revenue_by_product[product_id] = revenue_by_product.get(product_id, 0) + sale["Total Amount"]

    # Sort each dictionary by its values, highest first
    units_ranking = sorted(units_by_product.items(), key=lambda pair: pair[1], reverse=True)
    revenue_ranking = sorted(revenue_by_product.items(), key=lambda pair: pair[1], reverse=True)

    # The first item in each ranking is the top product
    best_seller_id, best_seller_units = units_ranking[0]
    top_revenue_id, top_revenue = revenue_ranking[0]

    print("Total Sales Revenue:", format_money(total_revenue))
    print("Best-Selling Product:", product_catalog[best_seller_id]["Name"],
          "-", best_seller_units, "units sold")
    print("Highest-Revenue Product:", product_catalog[top_revenue_id]["Name"],
          "-", format_money(top_revenue))

    print("\nProduct Ranking by Revenue:")
    rank = 1
    for product_id, revenue in revenue_ranking:
        print(str(rank) + ".", product_catalog[product_id]["Name"], "-", format_money(revenue))
        rank += 1


# ------------------------------------
# Save and Load Functions - William Orazi
# Saves the catalog and sales history together in one JSON file
# so our data is still there the next time the program runs.
# ------------------------------------

data_file = "group3_sims_data.json"


def save_data():
    program_data = {"catalog": product_catalog, "sales": sales_history}

    with open(data_file, "w") as file:
        json.dump(program_data, file)

    print("Data saved to", data_file)


def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)

    # No saved file yet, which is normal the first time we run
    except FileNotFoundError:
        return {}


# ------------------------------------
# Load Saved Data - William Orazi
# If we saved data last time, pick up where we left off.
# Otherwise, keep the default catalog and an empty sales history.
# ------------------------------------

saved_data = load_data()

if len(saved_data) > 0:
    product_catalog = saved_data["catalog"]
    sales_history = saved_data["sales"]
    print("Loaded saved data with", len(sales_history), "sales.")


# ------------------------------------
# Main Menu - Chris Kuhl
# Repeats until the user chooses to exit the program.
# (Sales statistics option and saving on exit added by William Orazi.)
# ------------------------------------

while True:
    print("\nMain Menu")
    print("1. View Group 3's Catalog")
    print("2. Make a Sale")
    print("3. View Group 3's Sales History")
    print("4. Update Product")
    print("5. View Group 3's Sales Statistics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # View all products in the catalog
    if choice == "1":
        view_catalog()

    # Sales function
    elif choice == "2":
        make_sale()

    # Sales history function
    elif choice == "3":
        view_sales_history()

    # Update product information
    elif choice == "4":
        update_product()

    # Sales statistics
    elif choice == "5":
        view_sales_statistics()

    # Save our data, then exit the program
    elif choice == "6":
        save_data()
        print("Exiting Group 3's Program")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please try again.")
