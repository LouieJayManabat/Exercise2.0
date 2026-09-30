def calculate_total(orders):
    total = 0

    for order in orders:
        total += order["total"]

    return total


def print_receipt(orders, total):
    print("\n\n========== RECEIPT ==========")

    print(
        f"{'Item':<30}"
        f"{'Qty':<8}"
        f"{'Price':<10}"
        f"{'Total':<10}"
    )

    print("-" * 58)

    for order in orders:
        print(
            f"{order['item']:<30}"
            f"{order['quantity']:<8}"
            f"₱{order['price']:<9.2f}"
            f"₱{order['total']:<9.2f}"
        )

    print("-" * 58)
    print(f"TOTAL ORDER: ₱{total:.2f}")
    print("==============================")
    print("Thank you for ordering!")