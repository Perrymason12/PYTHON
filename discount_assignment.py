# Assignment Solution

# 1. Create a function named calculate_discount(price, discount_percent)
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# 2. Prompt the user to enter original price and discount percentage
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)
    print("Final Price after discount:", final_price)
except ValueError:
    print("Invalid input. Please enter numeric values.")
