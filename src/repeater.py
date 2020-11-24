


"""
create a decorator that repeats a fucntion 3 times

e.g.


@repeater
def do_something():
    print("does something")

>> do_something()
>> "does something"
>> "does something"
>> "does something"


#EXTENSION:

allow the repeater to take an argument "nr_times", which determins how many 
times its should be repeated

@repeater(nr_times=4)
def do_something():
    print("does something")

>> "does something"
>> "does something"
>> "does something"
>> "does something"


"""