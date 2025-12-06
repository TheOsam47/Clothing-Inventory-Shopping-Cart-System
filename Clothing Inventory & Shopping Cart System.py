class Product:
    def __init__(self, name, category, size, gender, color, price, quantity):
        self.name = name
        self.category = category
        self.size = size
        self.gender = gender
        self.color = color
        self.price = price
        self.quantity = quantity

    def reduce_stock(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print("Not enough quantity available.")

    def info(self):
        return f"{self.name} | Size: {self.size} | Color: {self.color} | Price: Rs {self.price}"


class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, amount):
        if amount <= 0:
            print("Quantity must be at least 1.")
            return

        if product.quantity >= amount:
            product.reduce_stock(amount)
            self.items.append((product, amount))
            print(amount, product.name, "added to cart.")
        else:
            print("Not enough stock available!")

    def show_cart(self):
        if len(self.items) == 0:
            print("Cart is empty.")
            return

        total = 0
        print("\nYour cart:")
        for item in self.items:
            p = item[0]
            amt = item[1]
            print("-", p.name, "| Color:", p.color, "| Size:", p.size,
                  "| Qty:", amt, "| Price each:", p.price)
            total += p.price * amt

        print("Cart total: Rs", total)


# ---------------------------------------------------
# SAFE INTEGER INPUT (BEGINNER FRIENDLY + try/except)
# ---------------------------------------------------
def input_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print("Please enter a number greater than or equal to", min_value)
                continue

            if max_value is not None and value > max_value:
                print("Please enter a number less than or equal to", max_value)
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a valid number.")


# -----------------------------------------------
# PRODUCT LIST
# -----------------------------------------------
products = [
    Product("Leather Jacket", "Jacket", "L", "Male", "Black", 5000, 5),
    Product("Leather Jacket", "Jacket", "M", "Male", "Black", 5000, 10),
    Product("Leather Jacket", "Jacket", "S", "Male", "Black", 5000, 5),

    Product("Denim Jacket", "Jacket", "L", "Male", "Blue", 5500, 6),
    Product("Denim Jacket", "Jacket", "M", "Male", "Blue", 5500, 10),
    Product("Denim Jacket", "Jacket", "L", "Male", "Black", 6000, 10),

    Product("Formal Shirt", "Shirt", "M", "Male", "White", 3000, 10),
    Product("Formal Shirt", "Shirt", "M", "Male", "Black", 4000, 15),

    Product("Casual Jeans", "Jeans", "L", "Male", "Blue", 2500, 15),
    Product("Casual Jeans", "Jeans", "M", "Male", "Blue", 2500, 15),

    Product("Cotton Pants", "Pants", "M", "Female", "Beige", 3000, 7),
    Product("Cotton Pants", "Pants", "L", "Male", "Blue", 2000, 7)
]

cart = Cart()
categories = ["Jacket", "Shirt", "Jeans", "Pants"]

print("Welcome to our Shop!")
print("Select a category:")

for i in range(len(categories)):
    print(i + 1, ".", categories[i])

keep_shopping = "yes"

# -----------------------------------------------
# MAIN SHOP LOOP
# -----------------------------------------------
while keep_shopping.lower() in ["yes", "sure", "yup", "continue", "ok"]:

    # Choose category
    cat_choice = input_int("Enter category number (1-4): ", 1, len(categories))
    selected_category = categories[cat_choice - 1]

    print("\nProducts in", selected_category + ":")

    # Collect product names
    product_names = []
    for p in products:
        if p.category == selected_category and p.name not in product_names:
            product_names.append(p.name)

    # Show product names
    for i in range(len(product_names)):
        print(i + 1, ".", product_names[i])

    # Choose product name
    prod_num = input_int("Enter product number: ", 1, len(product_names))
    chosen_name = product_names[prod_num - 1]

    # All variants
    variants = []
    for v in products:
        if v.name == chosen_name and v.category == selected_category:
            variants.append(v)

    # COLORS
    colors = []
    for v in variants:
        if v.color not in colors:
            colors.append(v.color)

    print("\nAvailable Colors:")
    for i in range(len(colors)):
        print(i + 1, ".", colors[i])

    color_num = input_int("Enter color number: ", 1, len(colors))
    selected_color = colors[color_num - 1]

    # SIZES
    sizes = []
    for v in variants:
        if v.color == selected_color and v.size not in sizes:
            sizes.append(v.size)

    print("\nAvailable Sizes:")
    for i in range(len(sizes)):
        print(i + 1, ".", sizes[i])

    size_num = input_int("Enter size number: ", 1, len(sizes))
    selected_size = sizes[size_num - 1]

    # Find exact product variant
    selected_variant = None
    for v in variants:
        if v.color == selected_color and v.size == selected_size:
            selected_variant = v
            break

    print("\nSelected item:")
    print(selected_variant.info())

    # Quantity
    qty = input_int(
        "Enter quantity to add to cart (Available: " + str(selected_variant.quantity) + "): ",
        1,
        selected_variant.quantity
    )

    cart.add_to_cart(selected_variant, qty)

    keep_shopping = input("Do you want to continue shopping? (yes/no): ")

# END
print("\nFinal Cart:")
cart.show_cart()
