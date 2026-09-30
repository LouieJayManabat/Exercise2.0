from menu import menu


def ask_to_order():
    while True:
        answer = input(
            "\nDo you want to order? (yes/no): "
        ).lower()

        if answer == "yes" or answer == "y":
            return True

        elif answer == "no" or answer == "n":
            return False

        else:
            print("Please enter yes or no.")


def get_orders():
    orders = []

    while True:
        item_name = input(
            "\nEnter the menu item: "
        ).title()

        if item_name not in menu:
            print("Sorry, that item is not on the menu.")
            continue

        while True:
            try:
                quantity = int(
                    input("Enter quantity: ")
                )

                if quantity > 0:
                    break
                else:
                    print(
                        "Quantity must be greater than 0."
                    )

            except ValueError:
                print("Please enter a valid number.")

        price = menu[item_name]
        total_price = price * quantity

        orders.append({
            "item": item_name,
            "quantity": quantity,
            "price": price,
            "total": total_price
        })

        while True:
            another = input(
                "\nDo you want to order another item? "
                "(yes/no): "
            ).lower()

            if another == "yes" or another == "y":
                break

            elif another == "no" or another == "n":
                return orders

            else:
                print("Please enter yes or no.")