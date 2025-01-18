/*
 * @lc app=leetcode.cn id=1521 lang=cpp
 *
 * [1521] 找到最接近目标值的函数值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Same to 3171. Find Subarray With Bitwise AND Closest to K
        AND 只會讓數字變小，所以可以用 Stack 來保存所有可能的 AND 結果
    */
    int closestToTarget(vector<int>& arr, int target) {
        int n = arr.size();
        int ans = INT_MAX;
        vector<int> st;
        for (int x : arr) {
            vector<int> st2;
            st2.push_back(x);
            for (int y : st) {
                if ((y & x) != st2.back()) {
                    st2.push_back(y & x);
                }
            }
            st = st2;
            for (int y : st) {
                ans = min(ans, abs(y - target));
            }
        }
        return ans;
    }
};
// @lc code=end

