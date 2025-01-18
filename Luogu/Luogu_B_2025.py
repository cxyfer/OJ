"""
Output:
  *
 ***
*****
 ***
  *
"""
for i in range(0, 5):
    if i < 3:
        print(" " * (2 - i) + "*" * (2 * i + 1) + " " * (2 - i))
    else:
        j = 4 - i
        print(" " * (2 - j) + "*" * (2 * j + 1) + " " * (2 - j))
