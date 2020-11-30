

def group_count(input_list):
    """
    make this into a one line dict comprehension
    """
    
    group_count = {}
    for item in input_list:

        if item not in group_count:
            group_count[item] = 0
        
        group_count[item] += 1

    return group_count