# Inventory Management System

A Python-based Inventory Management System designed to streamline the process of managing shoe inventory data. This project reads data from an `inventory.txt` file, allowing users to perform various operations such as viewing all items, adding new inventory, restocking items, and more. The system is designed with an intuitive menu interface and emphasizes code readability and maintainability.

## Features

- **View All Shoes**
  - Displays a list of all shoes in the inventory along with their details, such as country, code, product name, cost, and quantity.

- **Capture New Shoes**
  - Allows users to input and add new shoe data to the inventory. The data is saved both in the program and to the `inventory.txt` file.

- **Restock Shoes**
  - Identifies shoes with the lowest quantity in stock and provides the option to restock them. The updated quantity is saved back to the `inventory.txt` file.

- **Search for Shoes**
  - Enables users to search for a shoe by its unique code and displays the relevant shoe's details.

- **Calculate Value per Item**
  - Computes the total value of each shoe in the inventory (cost * quantity) and displays this information.

- **Identify Highest Quantity Product**
  - Identifies and highlights the shoe product with the highest quantity, marking it as a priority for sale.

## Code Overview

- **Class: `Shoe`**
  - Attributes:
    - `country`: The country of origin of the shoe.
    - `code`: The unique code identifier for the shoe.
    - `product`: The name of the shoe product.
    - `cost`: The cost of the shoe.
    - `quantity`: The quantity of the shoe available in stock.
  - Methods:
    - `get_cost()`: Returns the cost of the shoe.
    - `get_quantity()`: Returns the quantity of the shoe.
    - `__str__()`: Returns a string representation of the shoe object.

- **Functions**
  - `read_shoes_data()`: Reads data from `inventory.txt`, creates `Shoe` objects, and stores them in the `shoes_list`.
  - `capture_shoes()`: Captures new shoe data from the user and adds it to the inventory.
  - `view_all()`: Iterates over the `shoes_list` and prints details of all shoes.
  - `re_stock()`: Finds the shoe with the lowest quantity and allows the user to update the quantity.
  - `search_shoe()`: Searches for a shoe by its code and returns its details.
  - `value_per_item()`: Calculates and prints the total value for each item in the inventory.
  - `highest_qty()`: Identifies and prints the shoe with the highest quantity.

## How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Inventory-Management.git
   cd Inventory-Management
