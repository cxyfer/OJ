s = input()
n = len(s)

# 如果數字的長度為奇數，則在前面補一個 '0' 使其變為偶數
if n & 1:
    s = '0' + s
    n += 1

digits = [0]  # 初始化數字對的列表，第一個元素設為 0

# 以兩位一組遍歷數字字串
for i in range(0, n, 2):
    x, y = int(s[i]), int(s[i + 1])

    if x == y:
        digits.append(x)  # 如果兩位數字相同，將其加入列表
        # 如果當前加入的數字與前一個數字相同，則中斷迴圈
        if digits[-1] == digits[-2]:
            break
    else:
        if x > y:
            digits.append(x)  # 如果第一位大於第二位，將第一位加入並中斷迴圈
        else:
            digits.append(x + 1)  # 如果第一位小於第二位，將第一位加一後加入並中斷迴圈
        break

# 處理進位
for i in range(len(digits) - 1, 0, -1):
    digits[i - 1] += digits[i] // 10  # 處理進位
    digits[i] %= 10  # 保留當前位數字

    # 當前位數字與前一位相同，進行調整
    while digits[i] == digits[i - 1]:
        digits[i] += 1  # 當前位數字加一
        digits[i - 1] += digits[i] // 10  # 處理可能的進位
        digits[i] %= 10  # 保留當前位數字

# 補齊數字對列表使其與原數字長度匹配
digits += [0] * (n // 2 - len(digits) + 1)

# 確保每對數字中不會有兩位相同的情況
for i in range(1, len(digits)):
    if digits[i] == digits[i - 1]:
        digits[i] = (digits[i - 1] + 1) % 10  # 如果相同，將當前位數字加一並取模以防止進位

ans = ''.join(str(d) * 2 for d in digits)
print(ans.lstrip('0'))