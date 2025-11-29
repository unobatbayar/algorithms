"""
Strategy Design Pattern

The Strategy pattern defines a family of algorithms, encapsulates each one,
and makes them interchangeable. Strategy lets the algorithm vary independently
from clients that use it.

Use cases:
    - When you have multiple ways to perform a task
    - When you want to avoid conditional statements for algorithm selection
    - When algorithms should be interchangeable at runtime
"""


from abc import ABC, abstractmethod


# Strategy interface
class PaymentStrategy(ABC):
    """Abstract strategy interface."""
    
    @abstractmethod
    def pay(self, amount):
        """Pay the amount."""
        pass


# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    """Concrete strategy: Credit card payment."""
    
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}"


class PayPalPayment(PaymentStrategy):
    """Concrete strategy: PayPal payment."""
    
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        return f"Paid ${amount} using PayPal account {self.email}"


class BitcoinPayment(PaymentStrategy):
    """Concrete strategy: Bitcoin payment."""
    
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin wallet {self.wallet_address[:8]}..."


# Context
class ShoppingCart:
    """Context that uses a payment strategy."""
    
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item, price):
        """Add item to cart."""
        self.items.append((item, price))
    
    def set_payment_strategy(self, strategy):
        """Set payment strategy."""
        self.payment_strategy = strategy
    
    def checkout(self):
        """Checkout using the selected payment strategy."""
        total = sum(price for _, price in self.items)
        if self.payment_strategy is None:
            raise ValueError("Payment strategy not set")
        return self.payment_strategy.pay(total)


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000)
    cart.add_item("Mouse", 20)
    
    # Use credit card
    cart.set_payment_strategy(CreditCardPayment("1234567890123456"))
    print(cart.checkout())
    
    # Change to PayPal
    cart.set_payment_strategy(PayPalPayment("user@example.com"))
    print(cart.checkout())
    
    # Change to Bitcoin
    cart.set_payment_strategy(BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    print(cart.checkout())

