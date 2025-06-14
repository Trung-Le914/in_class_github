import numpy as np
import math

nums = [3, 2, 5, 6, 6, 4]
ans = [x**2 for x in nums if x % 2 == 0]
print(f'List of square of even numbers is {ans}')
