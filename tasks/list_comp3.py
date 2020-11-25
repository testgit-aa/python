


def list_comp3(input_list):
    """
    make this into a list comprehension
    """
    all_words = []
    for sublist in input_list:
        for string in sublist:
            for word in string.split():
                all_words.append(word)