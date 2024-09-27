class Restaurant:
    def __init__(self):
        self.menu = {
            'pizza': 40,
            'burger': 30,
            'fries': 10,
            'soda': 10,
            'salad': 50
        }
        self.order_total = 0

    def display_menu(self):
        print("Menu:")
        for key, value in self.menu.items():
            print(f"{key.capitalize():<10} ${value:>5}")

    def place_order(self):
        while True:
            item = input("Place your order: ")
            if item in self.menu:
                self.order_total += self.menu[item]
                print(f"Your order for {item} has been placed.")
            else:
                print(f"Sorry, {item} is not in our menu.")

            another_order = input("Do you want to place another order? (yes/no): ")
            if another_order.lower() != "yes":
                break

    def get_total_amount(self):
        return f"Your total amount is: ${self.order_total:.2f}"

    def run(self):
        print("Welcome to the restaurant!")
        self.display_menu()
        self.place_order()
        print(self.get_total_amount())

if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.run()