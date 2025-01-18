        N = random.choice(range(10000, 20000))
        f.write(f'{N}\n')
        A = random.choices(range(1, 10), k=N)
        f.write(f'{" ".join(map(str, A))}\n')