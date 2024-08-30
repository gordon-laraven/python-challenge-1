# Order System
# Empty_list = [
#     {
#         "Item name": "string",
#         "Price": float,
#         "Quantity": int
#     },
#     {
#         "Item name": "string",
#         "Price": float,
#         "Quantity": int
#     },
#     {
#         "Item name": "string",
#         "Price": float,
#         "Quantity": int
#     }
# ]
# Menu items
menu_items = {
    "1": {"Item name": "General Tso's Chicken", "price": 12.99, "Quantity": 0},
    "2": {"Item name": "Szechuan Beef", "price": 13.99, "Quantity": 0},
    "3": {"Item name": "Chow Fun", "price": 8.50, "Quantity": 0}
}
# Print the menu
print("Menu: ")
for key, value in menu_items.items():
    print(f"{key}: {value['Item name']} - ${value['price']}")

while True:
    # Prompt the customer to enter their selection from the menu
    menu_selection = input("What would you like to order (1-3)? ")

    if not menu_selection.isdigit():
        print("Error: Please enter a number between 1 and 3")
        continue

    if int(menu_selection) in menu_items:
        print("Okay, I have added ", menu_selection, "to your order. What else would you like? ")
        continue

    # elif int(menu_selection) not in menu_items:
    #     print("Error: Sorry, We do not have that option avaiable. Please choose another option.")
    #     continue

    # Get the item name from the menu items dictionary
    item_name = list(menu_items.values())[int(menu_selection)-1]["Item name"]

    while True:
        # Ask the customer for the quantity of the menu item
        quantity = input(f"How many {item_name} would you like? (default is 1): ")
        if quantity.isnumeric():
            quantity = int(quantity)
            break
        else:
            quantity = 1

    # Append the customer's order to the order list in dictionary format 
    order = ({"Item name": item_name, "price": list(menu_items.values())[int(menu_selection)-1]["price"], "Quantity": quantity})

    # Ask if the customer wants to add more items or checkout
    response = input("Do you want to add more items or checkout? (add/check): ")
    place_order = False

    match response.lower():
        case 'yes':
            place_order = True
            break
        case 'no':
            place_order = False
            print("Thank you for your order")
            break
        case _:
            print("Invalid input. Please try again.")

    if place_order:
        break

# Print the receipt
print("\nOrder Receipt:")
receipt_format = "{:<15} | {:>5} | {:>10}\n--------------------------|--------|----------"
print(receipt_format.format("Item name", "Price", "Quantity"))

for item in order:
    price_per_item = item["Price"] * item["Quantity"]
    print(receipt_format.format(item["Item name"], "${:.2f}".format(item["Price"]), str(item["Quantity"])))

total_price = sum([item["Price"] * item["Quantity"] for item in order])
print("\nTotal price: ${:.2f}".format(total_price))