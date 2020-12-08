
with open('day_6_data.txt') as f:

    questions = []
    letters = '' 
    for line in f:
        
        if line == '\n':
            # Count unique letters and append
            # Set returns unique vals
            questions.append(len(set(letters)))
            letters = ''
            continue
        
        # Accumulate the letters
        letters += line.rstrip()
       
    # Once we reach the end of f, we need to run the last line
    questions.append(len(set(letters)))
    
print(sum(questions))
        