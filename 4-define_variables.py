#!/usr/bin/env python3
"""
4-define_variables module
Contains definitions and annotations for variables
"""

# Define and annotate variables
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"

if __name__ == "__main__":
    # Test the variables
    print("a is a {} with a value of {}".format(type(a), a))
    print("pi is a {} with a value of {}".format(type(pi), pi))
    print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
    print("school is a {} with a value of {}".format(type(school), school))
