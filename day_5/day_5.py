
with open('day_5_data.txt') as f:
    row_list = []
    col_list = []
    # Read in row
    for line in f:
        line = line.rstrip()
        
        row = 127
        low = 0
        high = 127
        
        # First 6 values specify the columns
        for i in range(0,7):
            # When hitting an F, we reduce the high number 
            if line[i] == 'F':
                # floor the high numbers
                row = int((row + low)/2)
                high = row
            # When hitting a B, we increase the high number
            else:
                # round the low numbers
                low = round((row+low)/2)

            # Once i==6 we pick the min or max based on the final val
            # May not actually be needed is more a saftey option
            if i==6:
                if line[i] == 'F':
                    row = min(high,low) 
                else:
                    row = max(high,low)   
                
        row_list.append(row) # append row numbers
        
        # Loop over final 3 to get the column of seat
        # Pretty much the same process as above
        col = 7
        high_c = 7
        low_c = 0
        for i in range(7,10):
            if line[i] == 'L':
                col = int((col+low_c)/2)
                
                high_c = col
                                
            else:
                low_c = round((col+low_c)/2)

            if i==9:
                if line[i] == 'L':
                    col = min(high_c,low_c)

        col_list.append(col)        

    # Calculate the max seat_id
    max_seat_id = max(map(lambda x,y: (x * 8)+ y, row_list, col_list))
    print(max_seat_id)

## Part 2: Function to identify missing integer in list
def missing(seat_ids):
    start, end = seat_ids[0], seat_ids[-1]
    # Returns the set of values NOT IN seat_ids from the range that covers the range of integers
    # in seat_ids.  
    return sorted(set(range(min(seat_ids),max(seat_ids)+1)).difference(seat_ids))

print(missing(list(map(lambda x,y: (x * 8)+ y, row_list, col_list))))
