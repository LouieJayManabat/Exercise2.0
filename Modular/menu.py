menu = {
    "Cheeseburger": 110,
    "Onion Rings": 70,
    "Grilled Chicken": 140,
    "Carbonara": 100,
    "Lasagna": 160,
    "Iced Tea Cucumber Flavor": 45
}


def display_menu():
    print("\n========== MENU ==========")

    for item, price in menu.items():
        print(f"{item:<30} ₱{price:.2f}")

    print("===========================")