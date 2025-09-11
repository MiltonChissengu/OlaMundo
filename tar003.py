def calculate_discount(price, discount):
    if discount >= 20:
        return price - (discount/100)
    else:
        return price

price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))
print(calculate_discount(price, discount))