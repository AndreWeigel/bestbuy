from products import Product
from store import Store


# Menu string to be displayed to the user
MENU = """
==== Welcome to Best Buy ====
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""


def start(store):
    """Starts the interactive user interface for the store."""
    while True:
        print(MENU)
        choice = input("Please choose an option: ")

        if choice == '1':
            # Display all active products
            print("\nAvailable products:")
            for product in store.get_all_products():
                print(product.show())

        elif choice == '2':
            # Display total quantity of products in the store
            total_quantity = store.get_total_quantity()
            print(f"\nTotal amount of items in store: {total_quantity}")

        elif choice == '3':
            # Start making an order
            shopping_list = []
            while True:
                print("\nEnter product number (or press enter to finish):")
                # List all active products with index
                for i, product in enumerate(store.get_all_products(), start=1):
                    print(f"{i}. {product.name} (Price: ${product.price}, "
                          f"Quantity: {product.quantity})")
                selection = input()

                # Finish order if input is empty
                if selection == '':
                    break

                try:
                    selection = int(selection) - 1
                    product = store.get_all_products()[selection]
                    quantity = int(input(f"Enter quantity for {product.name}: "))
                    if quantity <= 0:
                        print("Quantity must be a positive number. Please try again.")
                        continue
                    if quantity > product.quantity:
                        print(
                            f"Only {product.quantity} units of {product.name} "
                            f"available. Please enter a valid quantity.")
                        continue
                    shopping_list.append((product, quantity))
                except (IndexError, ValueError):
                    print("Invalid selection or quantity. Please try again.")

            # Process shopping list if items were added
            if shopping_list:
                try:
                    total_cost = store.order(shopping_list)
                    print(f"\nOrder successful! Total cost: ${total_cost}")
                except Exception as e:
                    print(f"Error during order: {e}")

        elif choice == '4':
            # Exit the program
            print("\nThank you for visiting Best Buy! ")
            break

        else:
            print("\nInvalid option. Please choose again.")


def main():
    # Initializing default product inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    # Creating a store instance with the product inventory
    best_buy = Store(product_list)

    # Start the user interface
    start(best_buy)


if __name__ == "__main__":
    main()
