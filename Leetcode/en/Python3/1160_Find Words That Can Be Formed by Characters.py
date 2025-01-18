# @algorithm @lc id=1112 lang=python3 
# @title find-words-that-can-be-formed-by-characters


from en.Python3.mod.preImport import *
# @test(["cat","bt","hat","tree"],"atach")=6
# @test(["hello","world","leetcode"],"welldonehoneyr")=10
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0
        for word in words:
            cnt_w = Counter(word)
            if all(cnt_w[ch] <= cnt[ch] for ch in cnt_w):
                ans += len(word)
        return ans