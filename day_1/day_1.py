
# Read in data, strip white space and append to list 
with open('day_1_data.txt') as f:
    data = [int(line.rstrip()) for line in f]

# PROBLEM 1

# Attempt 1 - Assuming we can have duplicates so cant use lists, 
# Loop over the list once, loop over a second time to then try each subsequent number with our first number
# Check using if statement 
for num_1 in data:
    for num_2 in range(len(data)-1):
        sums = num_1 + data[num_2+1]
        if sums == 2020:
            print(f'Sum: {sums}')
            print(f'Number 1: {num_1}') 
            print(f'Number 2: {data[num_2+1]}')
            print(f'Product: {num_1*data[num_2+1]} \n')

# PROBLEM 2:
# Same approach as above but with 3 loops D: 
for num_1 in data:
    for num_2 in range(len(data)-1):
        for num_3 in range(len(data)-2):
            sums = num_1 + data[num_2+1] + data[num_3+2]
            if sums == 2020:
                print(f'Sum: {sums}')
                print(f'Number 1: {num_1}') 
                print(f'Number 2: {data[num_2+1]}')
                print(f'Number 2: {data[num_3+2]}')
                print(f'Product: {num_1*data[num_2+1]*data[num_3+2]} \n')

