
""""

implemet a child-class of dict called RangeDict that takes pairs of ints; (int, int) which
signifies a range. eg. (1,10), (30,34).
Given an int will return the value of the range the int is inside

so if out dict contain the keys (1,10), (30,34), and we run:

>> my_range_dict[7]
>> (1,10)

furthermore;

when you try to add a range that overlaps with an existing range, for example
trying to add (5,11) when we have (1,10), overwrite the overlapping span.

>> my_range_dict
>> {(1,10):1, (30,34): 2}
>> my_range_dict[(5,11)] = 3
>> my_range_dict
>> {(30,34): 2, (5,11):3}

""""