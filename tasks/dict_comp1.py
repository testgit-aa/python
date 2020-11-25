


def merge_dicts(dict1,dict2,dict3):
    """
    Change the for loop to a one line dict comprehension
    """

    new_dict = {}
    for d in [dict1,dict2,dict3]:
        new_dict.update(d)