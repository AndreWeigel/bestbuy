class Product:
    """
    Represents a product with a name, price, and quantity.
    Manages product availability and purchasing logic.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a new product with a name, price, and quantity."""

        if not isinstance(name, str) or not name:
            raise ValueError("Product name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Product price must be a non-negative number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Product quantity must be a non-negative integer.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""

        return self.quantity

    def set_quantity(self, quantity: int):
        """Updates the product quantity and deactivates the product if quantity reaches zero."""

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Checks whether the product is currently active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""

        self.active = False

    def show(self) -> str:
        """Displays the product's details."""

        product_info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return product_info

    def buy(self, quantity: int) -> float:
        """Processes the purchase of a specified quantity of the product."""

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if quantity > self.quantity:
            raise ValueError("Insufficient product quantity.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        if self.quantity == 0:
            self.deactivate()

        return total_price


# Test
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
