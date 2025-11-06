/*
 * @lc app=leetcode.cn id=3013 lang=cpp
 * @lcpr version=30204
 *
 * [3013] 将数组分成最小总代价的子数组 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long minimumCost(vector<int>& nums, int k, int dist) {
        int n = nums.size();
        long long s = accumulate(nums.begin(), nums.begin() + dist + 2, 0LL);
        multiset<int> L(nums.begin() + 1, nums.begin() + dist + 2), R;
        k -= 1;

        auto L2R = [&]() -> void {
            int x = *L.rbegin();
            L.erase(L.find(x));
            R.insert(x);
            s -= x;
        };

        auto R2L = [&]() -> void {
            int x = *R.begin();
            R.erase(R.find(x));
            L.insert(x);
            s += x;
        };

        while (L.size() > k)  // 維護 L 的大小
            L2R();

        long long ans = s;
        for (int r = dist + 2; r < n; ++r) {
            // 1. 入窗口
            int x = nums[r];
            if (x <= *L.rbegin()) {
                L.insert(x);
                s += x;
            } else
                R.insert(x);

            // 2. 出窗口
            int y = nums[r - dist - 1];
            if (L.find(y) != L.end()) {
                L.erase(L.find(y));
                s -= y;
            } else
                R.erase(R.find(y));

            // 3. 維護 L 的大小
            if (L.size() > k)
                L2R();
            else if (L.size() < k)
                R2L();

            // 4. 更新答案
            ans = min(ans, s);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,3,2,6,4,2]\n3\n3\n
// @lcpr case=end

// @lcpr case=start
// [10,1,2,2,2,1]\n4\n3\n
// @lcpr case=end

// @lcpr case=start
// [10,8,18,9]\n3\n1\n
// @lcpr case=end

 */

