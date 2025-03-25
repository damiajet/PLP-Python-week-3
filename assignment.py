#Define the function calculate_discount

def calculate_discount(price, discount_percent):
    discount_price = round(((1 - (discount_percent/100)) * price), 2)
    return discount_price

price = float(input("Enter product price: "))

discount_percentage = float(input("Enter discount percentage: "))

discount_price = calculate_discount(price, discount_percentage)

print(f"The discount price is {discount_price}\n")