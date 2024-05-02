# 0x00. Python - Variable Annotations

## Description

This repository contains a series of Python scripts for the Variable Annotations project. The project aims to provide practice with type annotations in Python 3.

## Concepts

The main concept covered in this project is **Advanced Python**.

## Resources

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Learning Objectives

By completing this project, you should be able to:

- Explain type annotations in Python 3
- Use type annotations to specify function signatures and variable types
- Understand duck typing
- Validate your code with MyPy

## Requirements

### General

- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Use Pycodestyle style (version 2.5)
- All files must be executable
- The length of your files will be tested using `wc`
- All modules, classes, and functions should have documentation
- Documentation should explain the purpose of the module, class, or method in a clear sentence

## Tasks

### 0. Basic annotations - add

Write a type-annotated function `add` that takes two float arguments and returns their sum as a float.

### 1. Basic annotations - concat

Write a type-annotated function `concat` that takes two string arguments and returns a concatenated string.

### 2. Basic annotations - floor

Write a type-annotated function `floor` that takes a float argument and returns its floor as an integer.

### 3. Basic annotations - to string

Write a type-annotated function `to_str` that takes a float argument and returns its string representation.

### 4. Define variables

Define and annotate several variables with specified values.

### 5. Complex types - list of floats

Write a type-annotated function `sum_list` that takes a list of floats as argument and returns their sum as a float.

### 6. Complex types - mixed list

Write a type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum as a float.

### 7. Complex types - string and int/float to tuple

Write a type-annotated function `to_kv` that takes a string and an int or float as arguments and returns a tuple with the string and the square of the int or float.

### 8. Complex types - functions

Write a type-annotated function `make_multiplier` that takes a float as argument and returns a function that multiplies a float by the argument.

### 9. Let's duck type an iterable object

Annotate the function `element_length`'s parameters and return value with appropriate types.

### 10. Duck typing - first element of a sequence

Augment the function `safe_first_element` with correct duck-typed annotations.

### 11. More involved type annotations

Add type annotations to the function `safely_get_value` using TypeVar.

### 12. Type Checking

Use MyPy to validate and make necessary changes to the code in `zoom_array`.

## Repository Information

- GitHub repository: [alx-backend-python](https://github.com/ElvisMw/alx-backend-python)
- Directory: 0x00-python_variable_annotations
- All scripts are located in the corresponding files within the directory.
