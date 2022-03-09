import numpy as np
numbers = np.array([1,2,3,4,5,6,7,8])
print("Original array:")
print(numbers)
p = 2
new_numbers = np.zeros(len(numbers) + (len(numbers)-1)*(p))
new_numbers[::p+1] = numbers
print("\nNew array:")
print(new_numbers)