class Menu:
    def __init__(self):
        self.items = {
            "Cheeseburger": 110,
            "Onion Rings": 70,
            "Grilled Chicken": 140,
            "Carbonara": 100,
            "Lasagna": 160,
            "Iced Tea Cucumber Flavor": 45
        }

    def display(self):
        print("\n========== MENU ==========")
        for item, price in self.items.items():
            print(f"{item:<26} ₱{price:.2f}")
        print("==========================")

    def has_item(self, name):
        return name in self.items

    def get_price(self, name):
        return self.items[name]


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        self.items.append({
            "item": name,
            "quantity": quantity,
            "price": price,
            "total": price * quantity
        })

    def calculate_total(self):
        total = 0
        for entry in self.items:
            total += entry["total"]
        return total


class Receipt:
    def __init__(self, order):
        self.order = order

    def print_receipt(self):
        print("\n\n========== RECEIPT ==========")
        print(f"{'Item':<26}{'Qty':<6}{'Price':<10}{'Total':<10}")
        print("-" * 52)

        for entry in self.order.items:
            print(
                f"{entry['item']:<26}"
                f"{entry['quantity']:<6}"
                f"₱{entry['price']:<9.2f}"
                f"₱{entry['total']:<9.2f}"
            )

        print("-" * 52)
        print(f"TOTAL ORDER: ₱{self.order.calculate_total():.2f}")
        print("=" * 52)
        print("Thank you for ordering!")


class Restaurant:
    def __init__(self):
        self.menu = Menu()

    @staticmethod
    def ask_yes_no(prompt):
        while True:
            answer = input(prompt).lower()

            if answer in ("yes", "y"):
                return True
            elif answer in ("no", "n"):
                return False
            else:
                print("Please enter yes or no.")

    @staticmethod
    def ask_quantity():
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity
                print("Quantity must be greater than 0.")

            except ValueError:
                print("Please enter a valid number.")

    def take_order(self):
        order = Order()

        while True:
            item_name = input("\nEnter the menu item: ").title()

            if not self.menu.has_item(item_name):
                print("Sorry, that item is not on the menu.")
                continue

            quantity = self.ask_quantity()
            order.add_item(item_name, quantity, self.menu.get_price(item_name))

            if not self.ask_yes_no("\nDo you want to order another item? (yes/no): "):
                return order

    def run(self):
        self.menu.display()

        if self.ask_yes_no("\nDo you want to order? (yes/no): "):
            order = self.take_order()
            Receipt(order).print_receipt()
        else:
            print("\nThank you! Have a nice day.")