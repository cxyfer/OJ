/*
 * @lc app=leetcode id=3134 lang=cpp
 * @lcpr version=30122
 *
 * [3134] Find the Median of the Uniqueness Array
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    int medianOfUniquenessArray(vector<int>& nums) {
        int n = nums.size();
        LL m = ((LL) n) * (n + 1) / 2; // 非空子陣列的數量
        LL k = (m + 1) / 2; // 中位數是第 k 小的數
        set<int> st(nums.begin(), nums.end()); 
        int left = 1, right = st.size();
        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(mid, k, nums)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    bool check(int upper, LL k, vector<int>& nums) {
        LL cnt = 0; // distinct 值 <= upper 的子陣列數量
        int l = 0;
        unordered_map<int, int> f;
        for (int r = 0; r < nums.size(); r++) {
            f[nums[r]]++;
            while (f.size() > upper) { // 當前子陣列的 distinct 值數量 > upper
                int out = nums[l];
                f[out]--;
                if (f[out] == 0) {
                    f.erase(out);
                }
                l++;
            }
            cnt += r - l + 1;
            if (cnt >= k) {
                return true;
            }
        }
        return false;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [3,4,3,4,5]\n
// @lcpr case=end

// @lcpr case=start
// [4,3,5,4]\n
// @lcpr case=end

 */

