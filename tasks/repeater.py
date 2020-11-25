


"""
create a decorator that repeats a function N times. 
the decorator should take and argument nr_times which determins how many 
times its should be repeated

example, if we have the decorator on the following function:

@repeater(nr_times=4)
def do_something():
    print("does something")

running,
>> do_something()

will return
>> "does something"
>> "does something"
>> "does something"
>> "does something"

"""