"""
Trend Micro | OA | Sequence of Successive Numbers
https://leetcode.com/discuss/post/5657614/trend-micro-oa-sequence-of-successive-nu-nnm3/

Given a number n (1 <= n <= 10^10), the task is to find all the possible sequences of successive
positive integer numbers (p. p+1, ..., p+m) that satisfy the equation: n = p^2 + (p+1)*2 + ... +
(p+m)^2.
Input
The input consists of a single integer n.
Output
The output is an array of strings consisting of two parts. The first element should display the total number of possible sequences, denoted as k. The following k elements should contain the descriptions of the sequences. Each element is a string starts with the count of numbers in the corresponding sequence, denoted as c, followed by c integers representing the successive positive integer numbers, seperated by a space. These k elements should be ordered in descending order of C.
Sample Input
2030
Sample Output
["2",4 21 22 23 24",”3 25 26 27”]
"""

import math
from bisect import bisect_left


def solve():
    n = int(input())
    sq = math.isqrt(n) + 1

    s = [0] * (sq + 1)
    for i in range(1, sq + 1):
        s[i] = s[i - 1] + i * i

    ans = []
    for l in range(sq + 1):
        # s[r] - s[l] >= n
        idx = bisect_left(s, s[l] + n)
        if idx <= sq and s[idx] - s[l] == n:
            ans.append([idx - l] + list(range(l + 1, idx + 1)))
    ans.sort(key=lambda x: x[0], reverse=True)

    ret = [str(len(ans))]
    for lst in ans:
        ret.append(" ".join(map(str, lst)))
    return ret


if __name__ == "__main__":
    print(solve())
