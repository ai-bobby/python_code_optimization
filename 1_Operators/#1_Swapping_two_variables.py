a = 5
b = 10

# Waey one
c = a
a = b
b = c
print(a)  # 10
print(b)  # 5


# Waye two
a = a + b
b = b - a
a = a - b

# Swapping
a, b = b, a

print(a)  # 10
print(b)  # 5
