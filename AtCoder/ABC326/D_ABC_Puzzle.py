from itertools import permutations

N = int(input())
R = input() #
C = input()
Mt = [["." for _ in range(N)] for _ in range(N)]

def show(Mt):
    for row in Mt:
        print("".join(row))
    print()

def solve(i, j):
    if i > N-1 or j > N-1:
        if check():
            print("Yes")
            show(Mt)
            exit()
        return True if check() else False
    for ch in "ABC.":
        Mt[i][j] = ch
        # print(Mt, valid())
        if valid():
            if j == N-1:
                if solve(i+1, 0):
                    return True
            else:
                if solve(i, j+1):
                    return True


def valid(): # is valid
    for i in range(N):
        row = "".join(Mt[i]).replace(".", "")
        col = "".join([Mt[j][i] for j in range(N)]).replace(".", "")
        if row and row[0] != R[i]:
            return False
        if col and col[0] != C[i]:
            return False
        for ch in "ABC":
            if row.count(ch) > 1:
                return False
            if col.count(ch) > 1:
                return False
    return True
def check(): # is answer
    for i in range(N):
        row = "".join(Mt[i]).replace(".", "")
        col = "".join([Mt[j][i] for j in range(N)]).replace(".", "")
        if row and row[0] != R[i]:
            return False
        if col and col[0] != C[i]:
            return False
        for ch in "ABC":
            if row.count(ch) != 1:
                return False
            if col.count(ch) != 1:
                return False
    return True
solve(0, 0)
print("No")
