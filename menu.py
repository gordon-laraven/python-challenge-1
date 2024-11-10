# Menu dictionary
menu = {
    "Snacks": {
        "Crab Ragoon (8 pc) ": 8.99,
        "Fried Wontons": 3.69,
        "Chinese Donuts (8 pc) ": 8.49,
        "Chicken Wings (6 pc) ": 9.99
    },
    "Meals": {
        "General Tso's Chicken": 12.49,
        "Teriyaki Chicken": 9.99,
        "Szechuan Beef": 13.49,
        "Chow Fun": 8.99,
        "Sweet and Sour": {
            "Chicken": 8.99,
            "Shrimp": 10.99,
            "Tufu": 9.99
        },
        "Fried Rice": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Can Soda": {
            "Coke": 1.99,
            "Diet Coke": 1.49,
            "Sprite": 1.99
        },
        "Tea": {
            "Green Tea": 2.49,
            "Jasmine Tea": 2.99,
            "Homemade Iced Tea": 3.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Fresh Brewed": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Vanilla Ice Cream": 4.99,
        "Cheesecake": {
            "New York": 4.99,
            "Oreo": 6.99,
            "Strawberry": 6.49
        },
        "Chocolate Brownie": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_item_selection = input("Type item number: ")

            # 3. Check if the customer typed a number
            if menu_item_selection.isdigit():

                # Convert the menu selection to an integer
                menu_item_selection = int(menu_item_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_item_selection in menu_items:

                    # Store the item name as a variable
                    item_name = menu_items[menu_item_selection]["Item name"]
                    item_price = menu_items[menu_item_selection]["Price"]


                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_name} would you like? ")


                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        print("Invalid quantity, setting to 1.")
                        quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": quantity
                    })
                else:
                    print("Invalid menu option. Please try again.")
            else:
                print("Invalid input. Please enter a valid number.")
        else:
            # Tell the customer that their input isn't valid
            print(f"{menu_category} was not a valid menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        if keep_ordering.lower() == "y":

                # Keep ordering
                break
        elif keep_ordering.lower() == "n":

                # Exit the keep ordering question loop # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order!") # Complete the order
                place_order = False
                break # Exit the keep ordering question loop
        else: # Tell the customer to try again
            print("Please enter 'Y' for yes or 'N' for no.")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
total_cost = 0
for item in order:

    # 7. Store the dictionary items as variables
    item_name = item["Item name"]
    item_price = item["Price"]
    quantity = item["Quantity"]


    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 24 - len(item_name)


    # 9. Create space strings
    item_spaces = " " * num_item_spaces


    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | ${item_price:.2f} | {quantity}")


# 11. Calculate the cost of the order using list comprehension
    total_cost += item_price * quantity
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
print("\nTotal cost: ${:.2f}".format(total_cost))
