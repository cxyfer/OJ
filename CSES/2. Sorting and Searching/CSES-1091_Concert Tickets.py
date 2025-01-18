""" CSES - 1091. Concert Tickets
    CSES 不能用 SortedList 套件，因此要手刻AVL Tree或Red-Black Tree，
    用 C++ STL 的 multiset 來解會比較容易。

    手刻 AVL Tree 參考：https://vjudge.net/solution/46917751
"""

from sortedcontainers import SortedList

n, m = map(int, input().split())
H = SortedList(map(int, input().split()))
T = list(map(int, input().split()))

for t in T:
    idx = H.bisect_right(t)
    if idx == 0:
        print(-1)
    else:
        print(H[idx-1])
        H.remove(H[idx-1])
