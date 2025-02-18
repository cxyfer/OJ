/*
 * @lc app=leetcode.cn id=2080 lang=cpp
 *
 * [2080] 区间内查询数字的频率
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class RangeFreqQuery {
public:
    unordered_map<int, vector<int>> pos;
    RangeFreqQuery(vector<int>& arr) {
        for (int i = 0; i < arr.size(); i++)
            pos[arr[i]].push_back(i);
    }
    
    int query(int left, int right, int value) {
        auto& p = pos[value];
        return upper_bound(p.begin(), p.end(), right) - lower_bound(p.begin(), p.end(), left);
    }
};
// @lc code=end

