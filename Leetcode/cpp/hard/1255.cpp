/*
 * @lc app=leetcode.cn id=1255 lang=cpp
 *
 * [1255] 得分最高的单词集合
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        // return solve1(words, letters, score);
        return solve2(words, letters, score);
    }
    int solve1(vector<string>& words, vector<char>& letters, vector<int>& score) {
        int n = words.size();
        vector<int> cnt(26);
        for (char ch : letters) cnt[ch - 'a']++;
        int ans = 0;
        function<void(int, int)> dfs = [&](int i, int cur) {
            if (i == n) {
                ans = max(ans, cur);
                return;
            }
            dfs(i + 1, cur); // 不選 words[i]
            for (char ch : words[i]) cnt[ch - 'a']--;
            bool flag = true;
            for (char ch : words[i]) {
                if (cnt[ch - 'a'] < 0) {
                    flag = false;
                    break;
                }
                cur += score[ch - 'a'];
            }
            if (flag) dfs(i + 1, cur); // 選 words[i]
            for (char ch : words[i]) cnt[ch - 'a']++;
        };
        dfs(0, 0);
        return ans;
    }
    int solve2(vector<string>& words, vector<char>& letters, vector<int>& score) {
        int n = words.size();
        vector<int> cnt(26); // 每個字母可使用的次數
        for (char ch : letters) cnt[ch - 'a']++;
        int ans = 0;
        for (int i = 1; i < (1 << n); i++) { // 枚舉所有可能的子集
            vector<int> tmp(26); // 當前子集需要的字母數量
            int cur = 0; // 當前子集的分數
            bool flag = true;
            for (int j = 0; j < n && flag; j++) {
                if (i & (1 << j)) { // words[j] 在當前子集中
                    for (char ch : words[j]) {
                        tmp[ch - 'a']++;
                        if (tmp[ch - 'a'] > cnt[ch - 'a']) { // 當前子集需要的字母數量超過可用的字母數量，不合法
                            flag = false;
                            break;
                        }
                        cur += score[ch - 'a'];
                    }
                }
            }
            if (flag) ans = max(ans, cur); // 若所有 words[j] 都能選，則更新答案
        }
        return ans;
    }
};
// @lc code=end

