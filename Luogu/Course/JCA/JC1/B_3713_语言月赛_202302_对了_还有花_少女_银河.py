n, m = map(int, input().split())

tasks = [input() for _ in range(m)]

for _ in range(n):
    name = input()
    for task in tasks:
        s = input()
        t = f"{name}.zip/{name}/{task}/{task}.cpp"

        print("Fusu is happy!" if s == t else "Fusu is angry!")