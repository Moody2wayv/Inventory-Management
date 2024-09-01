#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        Initialize the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Return the cost of the shoe.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Return a string representation of a class.
        '''
        return f"Shoe(country='{self.country}', code={self.code}, product={self.product}, cost={self.cost}, quantity={self.quantity})"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open('inventory.txt', 'r') as file:
            # Skip the first line
            next(file)
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    country, code, product, cost, quantity = parts
                    shoe = Shoe(country, code, product, float(cost), int(quantity))
                    shoe_list.append(shoe)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    try:
        country = input("Enter the country: ")
        code = input("Enter the code: ")
        product = input("Enter the product: ")
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        with open('inventory.txt', 'a') as file:
            file.write(f"{country},{code},{product},{cost},{quantity}\n")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organize your data in a table format
    by using Python’s tabulate module.
    '''
    from tabulate import tabulate

    if not shoe_list:
        print("No shoes to display.")
        return

    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    shoe_data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]
    print(tabulate(shoe_data, headers=headers, tablefmt="grid"))

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    if not shoe_list:
        print("No shoes available for re-stock.")
        return

    min_quantity_shoe = min(shoe_list, key=lambda x: x.quantity)

    # Prompt user to re-stock this shoe
    choice = input(f"The shoe '{min_quantity_shoe.product}' has the lowest quantity ({min_quantity_shoe.quantity}). Do you want to re-stock? (yes/no): ")
    if choice.lower() == 'yes':
        try:
            quantity_to_add = int(input("Enter the quantity to add: "))
            min_quantity_shoe.quantity += quantity_to_add

            # Update the file with the new quantity
            with open('inventory.txt', 'r') as file:
                lines = file.readlines()

            with open('inventory.txt', 'w') as file:
                for line in lines:
                    if line.strip().split(',')[1] == min_quantity_shoe.code:
                        parts = line.strip().split(',')
                        parts[4] = str(min_quantity_shoe.quantity)
                        file.write(','.join(parts) + '\n')
                    else:
                        file.write(line)

            print(f"Quantity updated successfully. New quantity for '{min_quantity_shoe.product}' is {min_quantity_shoe.quantity}.")
        except ValueError:
            print("Invalid input. Quantity must be a valid integer.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Re-stock canceled.")

def search_shoe():
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''
    code = input("Enter the shoe code to search for: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return shoe
    print("Shoe not found.")
    return None

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"The total value for {shoe.product} is {value}")

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    if not shoe_list:
        print("No shoes available.")
        return

    highest_quantity_shoe = max(shoe_list, key=lambda x: x.quantity)
    print(f"The shoe with the highest quantity is '{highest_quantity_shoe.product}' with {highest_quantity_shoe.quantity} units.")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
''' 
def menu():
    print("Welcome to the Nike Factory Inventory System!")
    print("1. Add new shoe")
    print("2. View all shoes")
    print("3. Re-stock")
    print("4. Search for a shoe")
    print("5. Calculate value per item")
    print("6. Find shoe with highest quantity")
    print("7. Exit")

shoes_list = []

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        capture_shoes()
    elif choice == '2':
        view_all()
    elif choice == '3':
        re_stock()
    elif choice == '4':
        search_shoe()
    elif choice == '5':
        value_per_item()
    elif choice == '6':
        highest_qty()
    elif choice == '7':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
