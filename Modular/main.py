from menu import display_menu
from ordering import ask_to_order, get_orders
from receipt import calculate_total, print_receipt


def main():
    display_menu()

    if ask_to_order():
        orders = get_orders()

        total = calculate_total(orders)

        print_receipt(orders, total)

    else:
        print("\nThank you! Have a nice day.")


if __name__ == "__main__":
    main()