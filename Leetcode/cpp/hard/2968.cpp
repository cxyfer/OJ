/*
 * @lc app=leetcode id=2968 lang=cpp
 * @lcpr version=30112
 *
 * [2968] Apply Operations to Maximize Frequency Score
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;

class Solution {
public:
    int maxFrequencyScore(vector<int>& nums, long long k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        // prefix sum
        vector<LL> sum(n+1, 0); 
        for (int i=1; i<=n; i++){
            sum[i] = sum[i-1] + nums[i-1];
        }
        
        auto cost = [&](LL l, LL i, LL r) -> LL{
            LL d1 = (i - l) * nums[i] - (sum[i] - sum[l]);
            LL d2 = (sum[r+1] - sum[i+1]) - (r - i) * nums[i];
            return d1 + d2;
        };

        // sliding window
        int ans = 0, left = 0, right = 0;
        while (right < n){
            while (cost(left, (left+right)/2, right) > k){
                left++;
            }
            ans = max(ans, right - left + 1);
            right++;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,6,4]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,4,4,2,4]\n0\n
// @lcpr case=end

 */

