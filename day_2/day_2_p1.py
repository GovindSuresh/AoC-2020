with open('day_2_data.txt') as f:
    
    lines = map(lambda x: x.rstrip().split(': '), f)
    valid_pws = 0
    for i in lines:
        pw_combo = list(i)
        #print(pw_combo)
        policy = pw_combo[0]
        pw = pw_combo[1]

        # Get min and max + letter
        # Need to isolate the counts of the policy and the letter
        letter = policy[-1].rstrip()
        min_c = int(policy[:-1].rstrip().split('-')[0])
        max_c = int(policy[:-1].rstrip().split('-')[1])
        

        if letter in pw:
            letter_count = pw.count(letter)
            # check if letter is within the min and max counts
            if letter_count >= min_c and letter_count <= max_c:
                valid_pws += 1

        else:
            continue 

print(valid_pws)