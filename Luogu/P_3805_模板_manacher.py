"""
    Python 會 MLE
"""
s = input()
t = '#'.join("^" + s + "$")

halfLen = [0] * (len(t) - 2)
halfLen[1] = 1
boxM = boxR = 0
max_i = 0 # 最長回文子字串的中心位置
for i in range(2, len(halfLen)):
    hl = 1
    if i < boxR:
        hl = min(halfLen[boxM * 2 - i], boxR - i)
    while t[i - hl] == t[i + hl]:
        hl += 1
        boxM, boxR = i, i + hl
    halfLen[i] = hl
    if hl > halfLen[max_i]:
        max_i = i
print(halfLen[max_i] - 1)