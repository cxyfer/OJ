def isMatchingPossible(S, T, X):
    n = len(S)
    m = len(T)
    x = list(X)  # 将字符串X转换为列表以便修改字符

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if x[i + j] != '#' and x[i + j] != T[j]:  # 如果X中的字符不是'#'且与T中的字符不匹配
                match = False
                break

        if match:
            for j in range(m):
                x[i + j] = T[j]  # 将X中对应位置的字符替换为T中的字符

    return ''.join(x) == S

# 示例用法
S = "ABCBABC"
T = "ABC"
X = "#######"
matching_possible = isMatchingPossible(S, T, X)
print(matching_possible)
