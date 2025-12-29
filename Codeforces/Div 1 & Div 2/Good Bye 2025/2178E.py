from random import randint, choice
from itertools import accumulate

DEBUG = False

class Judge:
    def __init__(self, n: int):
        self.n = n
        self.query_count = 0
        self.max_queries = 300
        self.array = self._generate_array(n)
        self.s = list(accumulate(self.array, initial=0))
        # print(f"[DEBUG] Generated array: {self.array}")
        
    def _generate_array(self, n: int):
        k = randint(1, 30)
        A, B = [1 << k], [1 << k]

        def flatten(arr):
            max_val = max(arr)
            idx = choice([i for i, x in enumerate(arr) if x == max_val])
            return arr[:idx] + [max_val // 2, max_val // 2] + arr[idx+1:]

        while len(A) < n:
            ops = []
            if max(A) > 1:
                ops.append('flatten_a')
            if max(B) > 1 and len(A) + len(B) + 1 <= n:
                ops.append('flatten_b')
            if len(A) + len(B) <= n:
                ops.append('concat')
            if not ops:
                k = randint(1, 30)
                A, B = [1 << k], [1 << k]
                continue
            op = choice(ops)
            if op == 'concat':
                new = A + B
                A = new[:]
                B = new[:]
            elif op == 'flatten_a':
                A = flatten(A)
            else:
                B = flatten(B)
        assert len(A) == n
        return A
        
    def query(self, l: int, r: int) -> int:
        assert 1 <= l <= r <= self.n
        self.query_count += 1
        assert self.query_count <= self.max_queries
        return self.s[r] - self.s[l - 1]
        
    def answer(self, x: int):
        print(f"[DEBUG] Answer: ! {x}")
        print(f"[DEBUG] Total queries used: {self.query_count}")
        
        if x == (ans := max(self.array)):
            print("[RESULT] Correct!")
        else:
            print(f"[DEBUG] Generated array: {self.array}")
            raise ValueError(f"Wrong answer: {x}, Correct answer: {ans}")

def query(l, r):
    print(f"? {l} {r}", flush=True)
    return int(input())

def answer(x):
    print(f"! {x}", flush=True)

def solve():
    n = int(input()) if not DEBUG else randint(1, 1500)
    
    if DEBUG:
        global query, answer
        judge = Judge(n)
        query = judge.query
        answer = judge.answer

    l, r = 1, n
    s = query(1, n)
    while l < r:
        # 找到分割點 x 使得 [l, x] 的區間和 == [x + 1, r] 的區間和
        s //= 2
        left, right = l, r - 1
        while left <= right:
            mid = (left + right) // 2
            if query(l, mid) < s:
                left = mid + 1
            else:
                right = mid - 1
        # 此時 [1, left] 的區間和 == [left + 1, r] 的區間和
        # 根據兩個區間的長度判斷最大值的位置
        if (left - l + 1) <= (r - left):
            r = left
        else:
            l = left + 1
    answer(s)

if __name__ == "__main__":
    t = int(input()) if not DEBUG else 10
    for _ in range(t):
        solve()