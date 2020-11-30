



def list_comp1(input_data):
    """
    make this into a list comprehension

    example:
    >> list_comp1([1,0,90,40])
    >> [0,0,1,1]
    """

    transformed_data = []
    for i in input_data:

        if i >= 0:

            if i < 10:
                transformed_data.append(0)
            else:
                transformed_data.append(1)
    
    return transformed_data
            