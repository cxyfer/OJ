s = """
tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481
"""

rating = {line.split(" ")[0]:line.split(" ")[1]  for line in s.strip().split('\n')}

user = input()
print(rating[user])