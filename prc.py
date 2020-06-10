"""Print out all of the numbers in the following array that are divisible by 3:"""
x = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
y = [i for i in x if i % 3 == 0]
print(y)
"""The expected output for the above input is:
27
81
8
27
99
63
42"""

