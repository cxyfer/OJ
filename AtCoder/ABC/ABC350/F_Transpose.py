"""
    Simulation + Stack + Recursion
"""
import sys
sys.setrecursionlimit(10**6) # S <= 5 * 10^5

s = input()
n = len(s)

pos = [-1] * n # 預處理括號對應位置
st = []
for i, ch in enumerate(s):
    if ch == '(':
        st.append(i)
    if ch == ')':
        pos[i] = st[-1]
        pos[st[-1]] = i
        st.pop()

def dfs(i, j, flag):
    if i > j:
        return
    if flag: # 正向處理
        k = i
        while k <= j:
            ch = s[k]
            if ch == '(': # 遞迴處理括號內容
                dfs(k+1, pos[k]-1, flag^1)
                k = pos[k]
            else:
                print(ch, end='')
            k += 1
    else: # 反向處理
        while j >= i:
            ch = s[j]
            if s[j] == ')': # 遞迴處理括號內容
                dfs(pos[j]+1, j-1, flag^1)
                j = pos[j]
            else:
                print(ch.upper() if ch.islower() else ch.lower(), end='') # 大小寫轉換
            j -= 1

dfs(0, n-1, 1)
