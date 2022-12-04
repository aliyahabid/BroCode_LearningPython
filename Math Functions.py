# Math Functions
import math

print("Different versions of negative pi:")
neg_pi = -3.14
print(round(neg_pi))
print(math.ceil(neg_pi))
print(math.floor(neg_pi))
print(abs(neg_pi))
# pow() gives you a base value to a certain power.
print(pow(neg_pi, 2))
print(math.sqrt(abs(neg_pi)))

print(" ")
a = 4
b = 73
c = -23
print(max(a, b, c, neg_pi))
print(min(b, neg_pi))