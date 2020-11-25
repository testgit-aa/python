

"""
Add depth to the current package stucture (src) so that the import statement bellow words.

restrictions:
1) shallow, deeper, deepest, too_deep should all be folders
2) deepseafish is the follwoing functions:

    def deepseafish():
        return "bluop  bluop bluop"

3) deepseafish() should be located in a file called "something_in_the_deep.py"
"""

from src.shallow.deeper.deepest.too_deep import deepseafish

def whats_at_the_bottom():
    return deepseafish()