# builtin_usage.py

import math
import random
import platform

# Generate random number
random_number = random.randint(1, 100)

# Calculate square root and floor it
square_root = math.sqrt(random_number)
floored_root = math.floor(square_root)

# Display results
print("Random Number:", random_number)
print("Square Root (floored):", floored_root)

# Operating system information
print("Operating System:", platform.system())

# Python version
print("Python Version:", platform.python_version())