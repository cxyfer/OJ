/*
 * @lc app=leetcode.cn id=2053 lang=cpp
 *
 * [2053] 数组中第 K 个独一无二的字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, int> cnt;
        for (auto& s : arr) cnt[s]++;
        for (auto& s : arr)
            if (cnt[s] == 1 && --k == 0) return s;
        return "";
    }
};
// @lc code=end

