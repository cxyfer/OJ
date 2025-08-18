/*
 * @lc app=leetcode.cn id=3654 lang=cpp
 * @lcpr version=30204
 *
 * [3654] 删除可整除和后的最小数组和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    long long minArraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> f(n + 1);
        vector<int> mp(k, -1);
        int s = 0;
        mp[0] = 0;
        for (int i = 0; i < n; ++i) {
            s = (s + nums[i]) % k;
            f[i + 1] = min(f[i] + nums[i], mp[s] == -1 ? LLONG_MAX : f[mp[s]]);
            mp[s] = i + 1;
        }
        return f[n];
    }
};

class Solution2 {
public:
    long long minArraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> mp(k, LLONG_MAX);
        int s = 0;
        long long f = 0;
        mp[0] = 0;
        for (int i = 0; i < n; ++i) {
            s = (s + nums[i]) % k;
            f = min(f + nums[i], mp[s]);
            mp[s] = f;
        }
        return f;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [1,1,1]\n2\n
// @lcpr case=end

// @lcpr case=start
// [3,1,4,1,5]\n3\n
// @lcpr case=end

 */

