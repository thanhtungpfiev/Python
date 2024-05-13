# Created by Admin at 5/14/2022
income = 15_000
tax_coefficient = 0
if income < 10_000:
    tax_coefficient = 0.0
elif income < 30_000:
    tax_coefficient = 0.2
elif income < 100_000:
    tax_coefficient = 0.35
else:
    tax_coefficient = 0.45

print('I will pay:', income * tax_coefficient, 'in taxes')

order_total = 247
discount = 25 if order_total > 100 else 0
