#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    # Simulation question, 
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        ans = []
        right = 0 
        while True:
            left = right # Index of first word in this line.
            sumLen = 0 # Sum of words length in this line.
            # Calculate the right boundary of this line.
            # Notice that we need to leave at least one space between words. (right - left)
            while right < n and sumLen + len(words[right]) + (right - left) <= maxWidth:
                sumLen += len(words[right])
                right += 1
            # Last line or only one word in this line, left-justified.
            if right == n: 
                s = ' '.join(words[left:])
                ans.append(s + ' ' * (maxWidth - len(s)))
                break

            numWords = right - left
            numSpaces = maxWidth - sumLen
            # If there is only one word in this line, left-justified.
            if numWords == 1:
                ans.append(words[left] + ' ' * numSpaces)
                continue
            # Calculate the number of spaces between words in this line.
            avgSpaces = numSpaces // (numWords - 1)
            extraSpaces = numSpaces % (numWords - 1)
            # Generate this line.
            #   s1 = Extra spaces evenly distributed between words.
            s1 = (' ' * (avgSpaces + 1)).join(words[left:left + extraSpaces + 1]) 
            #   s2 = Remaining spaces evenly distributed between words.
            s2 = (' ' * avgSpaces).join(words[left + extraSpaces + 1:right]) 
            ans.append(s1 + ' ' * avgSpaces + s2)
        return ans
# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(sol.fullJustify(words, maxWidth))
