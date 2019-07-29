# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # Recurrsion close condition
    if len(sequence) == 1:
        # print("End of recurrsion iteration------------------ for", sequence)
        return sequence
    else:
        # print("Inside recurrsion iteration------------------ for", sequence)
        permutations = []
        for partial_sequence in get_permutations(sequence[1:]):
            # print("Now inside iteration of------------------", sequence)
            # print("partial_sequence", partial_sequence)
            for index in range(0, len(partial_sequence)+1):
                # new_sequence = partial_sequence[0:i]+partial_sequence[i:]
                new_sequence = partial_sequence[0:index] + \
                               sequence[0] + \
                               partial_sequence[index:len(partial_sequence)]

                # print("new sequence generated for iteration", index, new_sequence)
                permutations.append(new_sequence)
        # print(permutations)
        return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    assert get_permutations('a') == 'a'
    assert get_permutations('ab') == ['ab', 'ba']
    assert get_permutations('abc') == ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
