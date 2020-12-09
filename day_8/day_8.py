import collections

def file_process(file, struct):
    '''
    Read in and process file
    '''
    def instruction_set(line, struct):
        instr, val = line.rstrip().split(' ')
        return struct(instr, int(val))

    Instruction = collections.namedtuple("Instruction", ["instr", "val"])

    with open(file) as f:
        instructions = [instruction_set(line, struct) for line in f]

    return instructions

def instruction_parser(instructions, index, prev_steps, accumulator):
    '''
    Recursive solution to Part 1:
    
    The beginning of the function checks whether the `index` value passed in is contained in the `prev_steps`
    list. If it is, we are stuck in an infinite loop so we simply return the accumulator to this point. 

    If not, we check the Instruction tuple at the current index
    At each step we append of the index value into the list `prev_steps` 
    
    Start  at the beginning of the instructions (index=0):
        - If nop: increment index by 1, call function with new `index` and `prev_steps`. All else same.
        
        - If acc: increment accumulator by val of the Instruction tuple, increment index by 1.
                  Call function with new `index`,`prev_steps`, and `accumulator. All else same.
        
        - If jmp: Change index by Instruction tuple val. Call function with new `index` and `prev_steps`.
                  All else same. 

    '''
    # If this becomes false, we have reached the end of the instruction list, a stopping condition.
    while index < len(instructions):
        
        # If this evaluates to true, 
        # the stopping condition is met. Return the accumulated value.
        if index in prev_steps:
        
            return accumulator

        # In this case all we do is append the step index and increase index by 1
        # We then recall the function again but with the updated index and prev_steps.
        if instructions[index].instr == 'nop':
            prev_steps.append(index)
            index += 1
            return instruction_parser(instructions, index, prev_steps, accumulator)

        # In this case all we also increase the accumulator value by the value of the acc 
        # instruction. We then recall the function with the updated values.
        elif instructions[index].instr == 'acc':
            accumulator += instructions[index].val
            prev_steps.append(index)
            index += 1
            return instruction_parser(instructions, index, prev_steps, accumulator)
            
        # In this case, the index is changed by the value of the jmp instruction
        # We then recall the function with the updated values.
        elif instructions[index].instr == 'jmp':
            prev_steps.append(index)
            index += instructions[index].val

            return instruction_parser(instructions, index, prev_steps, accumulator )

    return accumulator

def instruction_parser2(instructions, index, prev_steps, accumulator, nop_jmp):
    '''
    Recursive solution to Part 2:
    
    Follows a similar process to part 1 except:
        - We keep track of the indexes all nops' and jmps' in our first run through
        - The case in which we hit an `index` in the `prev_steps` list.

    When we hit a previously visited index: 
        - We go to our list tracking the nops' and jmps' `nop_jmp` and
          pop the previous step index. The Instruction tuple instr attribute at this stage is flipped.
        
        - The `index`, `prev_steps`, and `accumulator` are then reset.
        
        - Within an infinite While loop We then call a similar function `instruction_parser_no_record` 
          which follows a similar process without the tracking of nops and jmps or flipping.

          `instruction_parser_no_record` returns False when it hits an index it previously visited. 
          We a brought back into this function, where we pop another element at the end of `nop_jmp`, perform the flip
          and call `instruction_parser_no_record` once more. 
          
          instruction_parser_no_record will continue to return False until such a time we pass in a path 
          which gets us to the final index of the instructions list. At which point it returns the tuple 
          (True, accumulator). The True will break the infinite while loop, and we can return the accumulator
          value from this function.   

    '''
    target = len(instructions)-1
    
    while index < len(instructions):

        if index in prev_steps:
           while True:
                # Get index of previous step and remove from list of nops and pops
                prior = nop_jmp.pop()

                # Flip the instruction at this index starting with the most recent
                if instructions[prior].instr == 'jmp':
                    instructions[prior] = Instruction('nop', instructions[prior].val)
                else:
                    instructions[prior] = Instruction('jmp', instructions[prior].val)

                # Reset the state back to the beginning, but with a flipped instruction
                index = 0
                prev_steps= []
                accumulator = 0

                # Perform the same function without tracking
                # If false, we will try flipping the next most recent nop/jmp and try again
                results = instruction_parser_no_record(instructions, index, prev_steps, accumulator, nop_jmp)
                
                breaker = results[0]

                # If breaker is True, it means we managed to find a complete path
                if breaker == True:
                    
                    # results[1] is the accumulated value
                    return results[1]

        if instructions[index].instr == 'nop':
            prev_steps.append(index)
            nop_jmp.append(index)
            index += 1
            return instruction_parser2(instructions, index, prev_steps, accumulator, nop_jmp)

        elif instructions[index].instr == 'acc':
            accumulator += instructions[index].val
            prev_steps.append(index)
            index += 1
            return instruction_parser2(instructions, index, prev_steps, accumulator, nop_jmp)
            

        elif instructions[index].instr == 'jmp':
            prev_steps.append(index)
            nop_jmp.append(index)
            index += instructions[index].val

            return instruction_parser2(instructions, index, prev_steps, accumulator, nop_jmp)

    return accumulator

def instruction_parser_no_record(instructions, index, prev_steps, accumulator, nop_jmp):
    '''
    Helper function for part 2. Called from within the `instruction_parser2` function. Full explanation
    of how the functions combine can be found in docstring for `instruction_parser2`.

    This function will return (False,False) until such a time it is provided a path that leads it to the
    final index value in the instructions list. At that point it will return (True, accumulator), the latter
    value being the accumulated value from acc steps. 

    '''
    target = len(instructions)-1
    
    while index < len(instructions):

        if index in prev_steps:
            return (False, False)

        if instructions[index].instr == 'nop':
            prev_steps.append(index)
            index += 1
            return instruction_parser_no_record(instructions, index, prev_steps, accumulator, nop_jmp)

        elif instructions[index].instr == 'acc':
            accumulator += instructions[index].val
            prev_steps.append(index)
            index += 1
            return instruction_parser_no_record(instructions, index, prev_steps, accumulator, nop_jmp)
            

        elif instructions[index].instr == 'jmp':
            prev_steps.append(index)
            index += instructions[index].val

            return instruction_parser_no_record(instructions, index, prev_steps, accumulator, nop_jmp)
    
    # Set loop breaker to True 
    return (True, accumulator)


if __name__ == '__main__':

    Instruction = collections.namedtuple("Instruction", ["instr", "val"])
    instructions = file_process('day_8_data.txt', Instruction)


    val = instruction_parser(instructions, index=0, prev_steps=[], accumulator=0)

    val2 = instruction_parser2(instructions, index=0, prev_steps=[], accumulator=0, nop_jmp=[])

    print(val)
    print(val2)