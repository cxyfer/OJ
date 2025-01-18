class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # ans = 0
        # vowel = set("aeiou")
        # cnt = defaultdict(int)
        # cnt_vowel = 0
        # left = 0
        # for right, ch in enumerate(word):
        #     cnt[ch] += 1
        #     if ch in vowel:
        #         cnt_vowel += 1
        #     while (right - left + 1) - cnt_vowel > k:
        #         cnt[word[left]] -= 1
        #         if word[left] in vowel:
        #             cnt_vowel -= 1
        #         left += 1
        #     if all(cnt[ch] >= 1 for ch in vowel) and (right - left + 1) - cnt_vowel == k:
        #         print(left, right, word[left:right+1])
        #         ans += 1
        # return ans
        n = len(word)
        vowels = set('aeiou')
        ans = 0
        
        for i in range(n):
            cur = set() # set of vowels
            cnt = 0 # count of consonants
            for j in range(i, n):
                ch = word[j]
                if ch in vowels:
                    cur.add(ch)
                else:
                    cnt +=1
                if len(cur) == 5 and cnt == k:
                    ans +=1
        return ans