with open('day_2_data.txt') as f:
    # Strip and split the lines
    lines = map(lambda x: x.rstrip().split(': '), f)
    
    # Loop over the iterator and calculate valid passwords pw by pw 
    valid_pws = 0
    for i in lines:
        pw_combo = list(i)
        
        # Isolate the policy part and password 
        policy = pw_combo[0]
        pw = pw_combo[1]

        # Get min and max + letter
        # Need to isolate the letter of the policy and the indexes
        letter = policy[-1]
        
        index_1 = int(policy[:-1].rstrip().split('-')[0])-1
        index_2 = int(policy[:-1].rstrip().split('-')[1])-1
  
        # Check 1, check the letter occurs at the specified first index 
        if pw[index_1] == letter:
            # If True - Check if letter occurs at second index 
            if pw[index_2] != letter:
                valid_pws += 1
        
        # If the first char isn't the letter then check the second index 
        elif pw[index_2] == letter:
            valid_pws += 1

print(valid_pws)