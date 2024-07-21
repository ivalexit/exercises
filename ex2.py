price = float(input("Enter book price"))

fractional = price - int(price)

fractional_calc = fractional * 100

result = fractional_calc > 50

print(result)