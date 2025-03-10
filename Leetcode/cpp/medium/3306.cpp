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
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        
        // pre[i] 表示 word[i] 前面有多少個連續的母音 (不含 word[i])
        vector<int> pre(n);
        for (int i = 0; i < n - 1; i++)
            if (vowels.count(word[i]))
                pre[i + 1] = pre[i] + 1;

        /*
            使用滑動窗口維護 word[right] 為右端點的子字串
        */
        long long ans = 0;
        unordered_map<char, int> cnt;  // 記錄每個母音出現的次數
        int have = 0, consonants = 0, left = 0;  // 母音的種類, 子音的數量, 左端點
        for (int right = 0; right < n; right++) {
            char ch = word[right];
            // 1. 入窗口
            if (vowels.count(ch)) {
                if (cnt[ch] == 0) have++;
                cnt[ch]++;
            }
            else consonants++;

            // 2. 子音太多了，縮小窗口
            while (consonants > k) {
                char lc = word[left];
                if (vowels.count(lc)) {
                    cnt[lc]--;
                    if (cnt[lc] == 0) have--;
                }
                else consonants--;
                left++;
            }

            // 3. 更新答案
            if (consonants == k && have == 5) {
                // 把前綴中多餘的母音去掉
                while (vowels.count(word[left]) && cnt[word[left]] > 1) {
                    cnt[word[left]]--;
                    left++;
                }
                // pre[left] 即窗口可以向左延伸的長度
                ans += pre[left] + 1;
            }
        }
        return ans;
    }
};
// @lc code=end

