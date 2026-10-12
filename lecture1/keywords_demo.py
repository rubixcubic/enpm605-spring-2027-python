"""Python's reserved keywords (Lecture 1)."""

import keyword

print(keyword.iskeyword("if"))  # True
print(keyword.iskeyword("hello"))  # False
print(keyword.kwlist)  # Every keyword
print(keyword.softkwlist)  # Keywords only in some places, such as match
