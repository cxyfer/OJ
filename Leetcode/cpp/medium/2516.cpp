/*
 * @lc app=leetcode.cn id=2516 lang=cpp
 *
 * [2516] 每种字符至少取 K 个
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        將問題轉換為在 s 中找到最長的子字串，使得子字串外至少有 k 個 a, b, c
        用 cnt 統計窗口外的字元數量，當 cnt[ch] < k 時，表示窗口外的字元數量不足，
        需要移動 left 指針來縮小窗口，直到 cnt[ch] >= k 為止。
    */
    int takeCharacters(string s, int k) {
        int n = s.size();
        vector<int> cnt(3, 0); // 只有 a, b, c 三種字元
        for (char ch: s) cnt[ch - 'a']++;
        for (char i = 0; i < 3; i++) // 檢查是否每種字元都至少有 k 個
            if (cnt[i] < k) return -1;
        int mx = 0, left = 0;
        for (int right = 0; right < n; right++) {
            cnt[s[right] - 'a']--; 
            while (cnt[s[right] - 'a'] < k) { // 窗口外的字元數量不足，需要移動 left 指針來縮小窗口
                cnt[s[left] - 'a']++;
                left++;
            }
            mx = max(mx, right - left + 1); // 更新最大長度
        }
        return n - mx; // 返回需要移除的字元數量
    }
};
// @lc code=end

