# x: int = 55 sometimes variable classes are also given in this format
# print("hello", x) it outputs the same result as the variable demand
principal = 1000  # initial payment
rate = 0.05       # Interest rate
numyears = 5     # Number of years

year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    print(f'{year:>3d} {principal:0.2f}')
    year += 1

# Arithmetic operators
    # x + y  Addition
    # x - y  Subtraction
    # x * y  Multiplication
    # x / y  Division
    # x // y Truncating Division
    # x ** y Power (x to the y power)
    # x % y  Modulo (x mod y) Remainder
    # +x     Unary plus
    # -x     Unary minus

# Built-in Function
    # abs(x) absolute value
    # divmod(x, y)  Returns (x // y, x % y)
    # pow(x, y[,modulo]) Returns ( x ** y ) % modulo
    # round(x, [n]) Rounds to the newarest multiple of 10 to the nth power

# Bit manipulation
    # x << y  Left shift
    # x >> y  Right shift
    # X & y   Bitwise and
    # x ! y   Bitwise or
    # x ^ y   Bitwise xor (exclusive or)
    # ~x      Bitwise negation

# Comparison operators
    # x == y  Equals to
    # x != y  Not equal to
    # x > y   Greater than
    # x < y   Less than
    # x >= y  Greater than or equals to
    # x <= y  Less than or equals to

# Logical Operators
    # x or y  If x is false, return y; otherwise, return x
    # x and y if x is false, return x; otherwise, return y
    # not x   If x is false, return True; otherwise, return False
    # A value is considered false if it is literally False, None, numerically zero. or empty. Otherwise it's considered-
    # -True.
a = int(input("enter a number as you like"))
print("if your number is less than the preset value the computer does nothing but if it isn't then computer says no")
b = 50
if a < b:
    pass
else:
    print("NO!")

# Short if and else statement
maxval = a if a > b else b
print("the max value is: ", maxval)

# Walrus operator ( := )
x = 0
while (x:= x + 1) < 10:
    print(x)

# The Break Statement
y = 0
while y < 10:
    if y == 5:
        break
    print(y)
    y += 1
print("Done!!")

# The Continue Statement
z = 0
while z < 15:
    z += 1
    if z == 5:
        continue
    print(z)
print("Done !! (2)")

a = "hello world"
print(len(a))
b = a[:5] # b = a[4]
c = a[6:] # c = a[6]
d = a[-1] # d = a[0:]
e = a[3:8]
f = a[-5:]
print(b, c, d, e, f)

# Replacing strings, replace()
g = a.replace("hello", "hello cruel and rude")
print(g)
