"""
    註解調的寫法只能用C++，用python會TLE，
    從時間複雜度來看，這個寫法是O(n^2)，而能AC的寫法是O(5000*n)
    但這題的 n 最大應該是 1000，有點奇怪
"""
import sys
input = sys.stdin.readline
print = sys.stdout.write
MAX_NUM = 5001
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    mark = [0] * MAX_NUM
    ans = 0

    # for i in range(n):
    #     tmp = 0
    #     for j in range(i):
    #         if A[j] <= A[i]:
    #             tmp += 1
    #     ans += tmp
    for i in range(n):
        ans += sum(mark[:A[i]+1])
        mark[A[i]] += 1
 
    print(f"{ans}\n")