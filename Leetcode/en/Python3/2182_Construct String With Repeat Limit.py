# @algorithm @lc id=2300 lang=python3 
# @title construct-string-with-repeat-limit


from en.Python3.mod.preImport import *
# @test("cczazcc",3)="zzcccac"
# @test("aababab",2)="bbabaa"
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = []
        cnt = Counter(s)
        keys = sorted(cnt.keys(), reverse=True)
        n = len(keys)
        print(cnt)
        for i, k in enumerate(keys): # 由大到小
            if cnt[k] == 0:
                continue
            j = i + 1
            while True:
                if ans and ans[-1] == k:
                    ans.pop()
                    cnt[k] += 1
                num = min(cnt[k], repeatLimit) # 重複次數
                if num == 0:
                    break
                ans.append(k*num)
                cnt[k] -= num
                while j < n and cnt[keys[j]] == 0:
                    j += 1
                if j == n:
                    break
                ans.append(keys[j])
                cnt[keys[j]] -= 1
        return "".join(ans)