# Input 
H, W = map(int, input().split())
c = [list(input()) for _ in range(H)] # Matrix of characters

# Preprocess
A = 26 # 字母個數 # c_(i,j) is a lowercase English letter.
row = [[0] * A for _ in range(H)] # row[i][j] 表示在第i橫列中字母j出現的次數
row_c = [0] * H # row_c[i] 表示在第i橫列中不同字母的個數
col = [[0] * A for _ in range(W)] # col[i][j] 表示在第i直行中字母j出現的次數
col_c = [0] * W # col_c[i] 表示在第i直行中不同字母的個數
num_row, num_col = H, W # 剩餘的橫列和直行的數量
for i in range(H):
    for j in range(W):
        idx = ord(c[i][j]) - ord('a') # 字母的索引
        # 依照上述的定義更新 row, row_c, col, col_c
        row[i][idx] += 1
        if row[i][idx] == 1:
            row_c[i] += 1
        col[j][idx] += 1
        if col[j][idx] == 1:
            col_c[j] += 1

# Start
while True:
    del_row, del_col = [], []
    for i in range(H):
        if row_c[i] == 1 and num_col >= 2: # 依照題目的定義刪除橫列
            del_row.append(i)
    for j in range(W):
        if col_c[j] == 1 and num_row >= 2: # 依照題目的定義刪除直行
            del_col.append(j)
    if del_row == [] and del_col == []:
        break
    def remove(i, j): # 刪除c[i][j]，並更新 row, row_c, col, col_c
        if c[i][j] != ' ':
            idx = ord(c[i][j]) - ord('a')
            row[i][idx] -= 1
            if row[i][idx] == 0:
                row_c[i] -= 1
            col[j][idx] -= 1
            if col[j][idx] == 0:
                col_c[j] -= 1
            c[i][j] = ' '
    for i in del_row:
        for j in range(W):
            remove(i, j)
    num_row -= len(del_row)
    for j in del_col:
        for i in range(H):
            remove(i, j)
    num_col -= len(del_col)
# Output
print(num_row * num_col)