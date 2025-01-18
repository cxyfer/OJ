mp = {
    'c': [2, 3, 4, 7, 8, 9, 10],
    'd': [2, 3, 4, 7, 8, 9],
    'e': [2, 3, 4, 7, 8],
    'f': [2, 3, 4, 7],
    'g': [2, 3, 4],
    'a': [2, 3],
    'b': [2],
    'C': [3],
    'D': [1, 2, 3, 4, 7, 8, 9],
    'E': [1, 2, 3, 4, 7, 8],
    'F': [1, 2, 3, 4, 7],
    'G': [1, 2, 3, 4],
    'A': [1, 2, 3],
    'B': [1, 2],
}

t = int(input())
for _ in range(t):
    s = input()
    cnt = [0] * 11
    # st = set()
    st = 0
    for ch in s:
        new_st = 0
        for i in mp[ch]:
            # if i not in st:
            if not (1 << i) & st: # i not in set
                cnt[i] += 1
            new_st |= 1 << i
        # st = set(mp[ch])
        st = new_st
    print(*cnt[1:])