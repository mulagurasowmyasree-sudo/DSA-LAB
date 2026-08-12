def power(p, n):
    if n == 0:
        return 1
    else:
        return p * power(p, n - 1)

p = int(input("Enter the principal growth factor (p): "))
n = int(input("Enter the number of years (n): "))
result = power(p, n)
print("Result =", result)
