import random

N = 10000
with open("./pB_hack.in", "w") as f:
    for i in range(N):
        f.write(f"{random.randint(1, 10000)}\n")
    