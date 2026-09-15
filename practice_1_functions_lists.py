prices = [120, 350, 80, 500]

def calculate_total(numbers):
    return sum(numbers)

def find_expensive(numbers, limit):
    return [price for price in numbers if price > limit]

def apply_discount(numbers, percent):
    return [price * (1 - percent / 100) for price in numbers]

print("Сумма:", calculate_total(prices))
print("Дороже 200:", find_expensive(prices, 200))
print("После скидки 10 процентов:", apply_discount(prices, 10))