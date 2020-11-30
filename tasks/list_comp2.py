



def list_comp2(input_list):
    """
    make this into a list comprehension

    example:

    >> list_comp2([[1,1],[2,2]])
    >> [1,1,2,2]
    """
    flatten_list = []
    for sublist in input_list:
        for item in sublist:
            flatten_list.append(item)

    return