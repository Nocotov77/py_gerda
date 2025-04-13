from decimal import Decimal, getcontext

getcontext().prec = 50  # Увеличиваем точность вычислений

s = Decimal(input())
mercury = 2 * s
sulfur = s / Decimal(3)
salt = s / Decimal(8)
initial_mass = mercury + sulfur + salt
half_mass = initial_mass / Decimal(2)

hours = 0
current_mercury = mercury
current_salt = salt

current_total = current_mercury + sulfur + current_salt

while current_total > half_mass:
    hours += 1
    current_mercury *= Decimal('0.99')
    current_salt *= Decimal('0.995')
    current_total = current_mercury + sulfur + current_salt

print(hours, float(current_total))