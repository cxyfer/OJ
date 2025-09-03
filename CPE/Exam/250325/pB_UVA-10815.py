"""
UVA-10815 Andy's First Dictionary
https://vjudge.net/problem/UVA-10815
"""
# import sys

# st = set()
# for word in sys.stdin.read().split():
#     w = ""
#     for ch in word:
#         if ch.isalpha():
#             w += ch
#         elif w:
#             st.add(w.lower())
#             w = ""
#     if w:
#         st.add(w.lower())
    
# print("\n".join(sorted(st)))

import sys
import re

words = re.findall(r'[a-z]+', sys.stdin.read().lower())
print("\n".join(sorted(set(words))))