from functools import reduce

def tree_counter(treemap, depth_of_hill, depth_counter, tree_count, no_tree_count, pos_index, across, down):
    
    # Loop over the map 
    for i in treemap:
        
        # STOPPING CONDITION FOR RECURSION:
        # If the depth counter hits this level, the next check of the row will be the last
        # the -1 is because list indexing is -1 the length (0 indexing)
        if depth_counter == (depth_of_hill-down-1):
            
            # Check if a # or not, update relevant counts
            # first index chooses the row of the list, the second the position within the row
            if treemap[depth_counter+down][pos_index+across] == '#':
                tree_count += 1
            else:
                no_tree_count += 1
            
            return tree_count, no_tree_count
        
        # Each time the index hits this level we need to reset the index and call the function again
        # to begin parsing once more 
        if (pos_index+across) > 30:
      
            pos_index = pos_index-31
          
            return tree_counter(treemap, depth_of_hill, depth_counter, 
                            tree_count, no_tree_count, pos_index, across, down)
        
        
        # Standard check if no stopping or reset criteria have been met 
        if treemap[depth_counter+down][pos_index+across] == '#':
            tree_count += 1
        else:
            no_tree_count += 1
        
        # Increase the depth counter by the steps we moved down 
        # Increase the pos_index by number of steps across
        depth_counter += down
        pos_index = pos_index+across
    
    return tree_count, no_tree_count

with open('day_3_data.txt') as f:
    treemap = [line.rstrip() for line in f]

# Parameters to pass in 
depth_of_hill = len(treemap) # Length of hill for stopping criteria
tree_count = 0 # Count of trees encountered
depth_counter = 0 # How many levels we've gone down
no_tree_count =  0 # Count of non trees at level, used for checks
pos_index = 0 # Pos_index looking at on each row
across = 1 # across distance
down = 2 # down distance

x = tree_counter(treemap, depth_of_hill, depth_counter, tree_count, no_tree_count, pos_index, across, down)
print(x)

#Part 2
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
# Calculate the product of all the trees encountered with each slope
trees = reduce(lambda x,y: x*y, [tree_counter(treemap, depth_of_hill, depth_counter, tree_count,
                    no_tree_count, pos_index,i,j)[0] for i,j in slopes])

print(trees)