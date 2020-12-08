from collections import Counter

with open('day_6_data.txt') as f:

    question_count = [] # List of counts for qs answered by everyone in group
    letters = '' # String of all questions answered per group
    passenger_count = 0  # Counts passengers in a group
    for line in f:
        
        if line == '\n':
            
            # Count letters
            c = Counter(letters)
            
            # if there is only 1 passenger then all qs answered are valid
            if passenger_count == 1:
                question_count.append(len([k for k,v in c.items() if v == 1]))
            else:
                # In this case we count all letters with occurance equal to passenger_count.
                # This indicates the q was answered by all passengers in the group
                question_count.append(len([k for k,v in c.items() if v == passenger_count]))

            # Reset the Counter object, the passenger_count and letters string
            c = Counter()
            letters = ''
            passenger_count = 0
            
            continue
        
        # Accumulate the letters and increment passenger_count
        letters += line.rstrip()
        passenger_count += 1
       
# Once we reach the end of f, we need to check the counts for the last line
# as the \n criteria from earlier will not be met
if passenger_count == 1:
    c = Counter(letters)
    question_count.append(len([k for k,v in c.items() if v == 1]))
else:
    c = Counter(letters)
    question_count.append(len([k for k,v in c.items() if v == passenger_count]))

# Print result
print(sum(question_count))
