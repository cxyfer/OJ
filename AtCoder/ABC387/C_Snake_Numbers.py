from functools import cache

def count(num: int) -> int:
    s = str(num)
    n = len(s)

    @cache
    def dfs(i: int, is_limit: bool, first_digit: int) -> int:
        """
        數位DP
        
        i: 當前位數
        is_limit: 當前位是否受到上界限制
        first_digit: 首位數字，相當於模板的 is_num
        """
        if i == n:
            return int(first_digit > 0)
        
        upper = int(s[i]) if is_limit else 9
        res = 0
        if not first_digit:
            res += dfs(i + 1, False, 0)
            for d in range(1, upper + 1):
                res += dfs(i + 1, is_limit and d == upper, d)
        else:
            for d in range(0, min(first_digit - 1, upper) + 1):
                res += dfs(i + 1, is_limit and d == upper, first_digit)
        return res
    
    return dfs(0, True, 0)

L, R = map(int, input().split())
print(count(R) - count(L - 1))