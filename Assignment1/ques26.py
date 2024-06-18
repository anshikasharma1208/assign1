#. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
string="Hello,world! "
prefix="Hello"
suffix="world! "

starts_with_prefix=string.startswith(prefix)
ends_with_suffix=string.endswith(suffix)
print(f"Does the string {string} start with {prefix} ? {starts_with_prefix}")
print(f"Does the string {string} end with {suffix} ? {ends_with_suffix}")