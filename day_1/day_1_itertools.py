from itertools import combinations
from functools import reduce
import operator

# read in data
with open('day_1_data.txt') as f:
    data = [int(line.rstrip()) for line in f]

# Problem 1: 
combos = combinations(data, 2)
# Loop over each combo and check if they sum to 2020 
for i in combos:
    # Use tuple unpacking
    if operator.add(*i) == 2020:
        result = operator.mul(*i)

print(f'Product of 2 numbers: {result}\n')

# Get all combos of the 2 or 3 numbers
combos = combinations(data, 3)
# Loop over each combo and check if they sum to 2020 
for i in combos:
    # Use reduce as operator only accepts 2 args
    if reduce(operator.add, i) == 2020:
        result = reduce(operator.mul, i)


print(f'Product of 3 numbers: {result}')