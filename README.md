# Interactive Food Truck Ordering System

## Table of Contents
1. [Background](#background)
2. [Files](#files)
3. [Challenge Instructions](#challenge-instructions)
   - [Order System](#order-system)
   - [Order Receipt](#order-receipt)
4. [Code Implementation](#code-implementation)
5. [References](#references)

## Background
This project involves designing an interactive ordering system for a food truck menu using Python. Customers will be able to view the menu, place orders, and receive a receipt that includes the total price of all items ordered. The implementation demonstrates core programming skills such as working with lists, dictionaries, input validation, loops, and conditionals.

## Files
- `menu.py`: Contains the code for the food truck menu and ordering system.

## Challenge Instructions
The interactive ordering system has two main components: 
1. **Order System**: Users can select menu items and specify quantities.
2. **Order Receipt**: The system will output a formatted receipt including the total cost of the order.

### Order System
1. Create an empty list `order` to store each customer's order in dictionary format.
   ```python
   order = []
   ```

2. Display the menu options to the customer by looping through the main categories.
3. Validate the customer’s input to ensure they select a valid menu category and item.
4. Prompt the customer for the quantity of the selected item and validate this input.
5. Store the customer's selection in the `order` list.

### Order Receipt
1. After completing the order, display a formatted receipt including item names, prices, and quantities.
2. Calculate the total price of the order using list comprehension.

## Code Implementation

The code implementation for the Interactive Food Truck Ordering System is organized into several key components:

1. **Menu Definition**: 
   The menu is defined as a nested dictionary, where categories (Snacks, Meals, Drinks, Dessert) contain items and their respective prices.

   ```python
   menu = {
       "Snacks": {...},
       "Meals": {...},
       "Drinks": {...},
       "Dessert": {...}
   }
   ```

2. **Order List Initialization**: 
   An empty list named `order` is created to store the user's selected items in dictionary format.

   ```python
   order = []
   ```

3. **User Input for Menu Selection**: 
   A continuous loop prompts the user to select a menu category, validating input to ensure it corresponds to a valid menu option.

   ```python
   menu_category = input("Type menu number: ")
   ```

4. **Item Selection and Quantity Input**: 
   After displaying item options, the program allows the user to select a specific item and provide a quantity, with validation for the quantity input.

   ```python
   quantity = input(f"How many {item_name} would you like? ")
   ```

5. **Storing Orders**: 
   Each selected item, along with its name, price, and quantity, is appended to the `order` list as a dictionary.

   ```python
   order.append({"Item name": item_name, "Price": item_price, "Quantity": quantity})
   ```

6. **Receipt Generation**: 
   The program iterates through the `order` list to generate a formatted receipt that includes item names, prices, and quantities, while calculating and displaying the total cost.

   ```python
   total_cost += item_price * quantity
   ```

7. **Final Output**: 
   The final receipt is printed, providing clear and formatted information about the customer’s order.

   ```python
   print(f"\nTotal cost: ${total_cost:.2f}")
   ```

This structured implementation allows the program to effectively manage user inputs, process orders, and present results clearly, enhancing the overall user experience.

## References
- [Python Documentation](https://docs.python.org/3/) 


