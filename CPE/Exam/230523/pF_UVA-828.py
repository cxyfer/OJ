"""
    模擬(Simulation)
    關鍵是能不能找到規則：
    - 對於加密後的字串，優先檢查是不是 Rule 3，如果是就直接解密
    - 如果不是的話，就檢查是不是 Rule 2，如果是就解密，否則就是錯誤的加密
"""
def rotateLeft(ch: str, N: int): # rotate left N times
    return chr(ord('A') + (ord(ch) - ord('A') - N) % 26)

t = int(input())
for kase in range(t):
    input() # skip blank line
    if kase > 0: # print a blank line between test cases
        print()
    
    L = input()
    N = int(input())
    q = int(input())
    st = set(L)

    for _ in range(q):
        s = input()
        i = m = 0
        ans = ""

        while (i < len(s)):
            ch = s[i]
            if ch == " ": # Rule 1
                ans += ch
                i += 1
            elif i + 2 < len(s) and ch == L[m] and s[i+2] == L[(m+1) % len(L)]: # Rule 3
                ori = rotateLeft(s[i+1], N)
                if ori not in st: # original charater should in L
                    ori = rotateLeft(ch, N) # Rule 2
                    if ori in st: # original charater should not in L
                        print("error in encryption")
                        break
                    ans += ori
                    i += 1
                    continue
                ans += ori
                i += 3
                m = (m + 1) % len(L)
            else: # Rule 2
                ori = rotateLeft(ch, N)
                if ori in st: # original charater should not in L
                    print("error in encryption")
                    break
                ans += ori
                i += 1
        else:
            print(ans)
