import numpy as np

# Ask for input
x = float(input("Enter number x: "))
y = float(input("Enter number y: "))

# Compute power and log
power = x ** y
log_x = np.log2(x)

# Print results
print("x**y =", power)
print("log(x) =", int(log_x))
