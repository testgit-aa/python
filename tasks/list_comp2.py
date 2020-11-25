



def list_comp2(input_list):
    """
    make this into a list comprehension
    """
    flatten_list = []
    for sublist in input_list:
        for item in sublist:
            flatten_list.append(item)