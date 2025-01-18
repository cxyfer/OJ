""" Simulation
    R: 在這行寫 / 並且往上1行
    C: 在這行寫 _
    F: 先往下1行，再寫 \
"""
t = int(input())
N = 55

for kase in range(1, t + 1):
    S = input().strip()
    n = len(S)

    ans = [[" "]  * N ]
    cur = 0
    for j, ch in enumerate(S):
        if ch == 'C':
            ans[cur][j] = "_"
        elif ch == 'R':
            ans[cur][j] = "/"
            if cur == 0:
                ans.insert(0, [" "]  * N)
            else:
                cur -= 1
        elif ch == 'F':
            if cur == len(ans) - 1:
                ans.append([" "]  * N)
            cur += 1
            ans[cur][j] = "\\"
    print(f"Case #{kase}:")
    if all(ch == " " for ch in ans[0]): # remove the first row if it's empty
        ans.pop(0)
    for row in ans:
        print("| " + "".join(row).rstrip())
    print("+" + "-" * (n+2))
    print()
