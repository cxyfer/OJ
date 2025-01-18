# @algorithm @lc id=443 lang=python3 
# @title string-compression


from en.Python3.mod.preImport import *
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        idx = 0 # Ans
        right = 0
        while right < n:
            left = right
            while (right+1 < n) and (chars[right] == chars[right+1]):
                right += 1
            chars[idx] = chars[left]
            if right == left: # only one char
                idx += 1
            else: # more than one char
                str_len = len(str(right-left+1))
                
                for i in range(0, str_len):
                    chars[idx+1+i] = str(right-left+1)[i]
                idx += 1 + len(str(right-left+1))
            right += 1
        chars = chars[:idx]
        # print(chars)
        return idx