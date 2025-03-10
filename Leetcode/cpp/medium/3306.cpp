/*
 * @lc app=leetcode id=3306 lang=cpp
 *
 * [3306] Count of Substrings Containing Every Vowel and K Consonants II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long countOfSubstrings(string word, int k) {
        int n = word.size();
        set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        
        vector<int> pre(n);
        for (int i = 0; i < n - 1; i++)
            if (vowels.count(word[i]))
                pre[i + 1] = pre[i] + 1;

        long long ans = 0;
        unordered_map<char, int> cnt_vowel;
        int have_vowel = 0, cnt = 0, left = 0;

        for (int right = 0; right < n; right++) {
            // 1. 入窗口
            char ch = word[right];
            if (vowels.count(ch)) {
                if (cnt_vowel[ch] == 0) have_vowel++;
                cnt_vowel[ch]++;
            }
            else cnt++;

            // 2. 子音太多了，縮小窗口
            while (cnt > k) {
                char lc = word[left];
                if (vowels.count(lc)) {
                    cnt_vowel[lc]--;
                    if (cnt_vowel[lc] == 0) have_vowel--;
                }
                else cnt--;
                left++;
            }

            // 3. 更新答案
            if (cnt == k && have_vowel == 5) {
                while (left < right && vowels.count(word[left]) && cnt_vowel[word[left]] > 1) {
                    cnt_vowel[word[left]]--;
                    left++;
                }
                ans += pre[left] + 1;
            }
        }
        return ans;
    }
};
// @lc code=end

