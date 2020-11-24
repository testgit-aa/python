


"""

Change this class so that one cannot (easily) access precious_variable and precious_function.
I.e. trying to access the function or variable by the name should not work:

>> needs_protection = ProtectMe()
>> needs_protection.precious_variable
>> needs_protections.precious_function()

restrictions:

1) you can only add 4 characters!


EXTENSION:
make precious_variable accessable by 

>> needs_protection.precious_variable

but make it impossible to change the value of the variable. e.g. the following code should 
throw an error:

>> needs_protection.precious_variable = "something else"

"""

class ProtectMe:

    def __init__(self):
        self.precious_variable = "you got it"

    
    def precious_function(self):
        return  "you got it"