/*
 * @lc app=leetcode id=2967 lang=cpp
 * @lcpr version=30112
 *
 * [2967] Minimum Cost to Make Array Equalindromic
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
    long long minimumCost(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        LL ans = 0;
        LL median = nums[n/2];

        if (check(median)){
            for (int i=0; i<n; i++){
                ans += abs(nums[i] - median);
            }
            return ans;
        }
        int l = median - 1, r = median + 1;
        while (!check(l)){
            l--;
        }
        while (!check(r)){
            r++;
        }
        LL cost1=0, cost2=0;
        for (int i=0; i<n; i++){
            cost1 += abs(nums[i] - l);
            cost2 += abs(nums[i] - r);
        }
        return min(cost1, cost2);
    }
    bool check(LL num){
        string s = to_string(num);
        int n = s.size();
        for (int i=0; i<n/2; i++){
            if (s[i] != s[n-i-1]){
                return false;
            }
        }
        return true;
    }
};
// @lc code=end
int main() {
    Solution sol = Solution();
    vector<int> nums1 = {1,2,3,4,5};
    cout << sol.minimumCost(nums1) << endl;
    vector<int> nums2 = {10,12,13,14,15};
    cout << sol.minimumCost(nums2) << endl;
    vector<int> nums3 = {206,215,216,219,220,221};
    cout << sol.minimumCost(nums3) << endl;
    vector<int> nums4 = {102,103,105,106,109};
    cout << sol.minimumCost(nums4) << endl;
    return 0;
}


/*
// @lcpr case=start
// [1,2,3,4,5]\n
// @lcpr case=end

// @lcpr case=start
// [10,12,13,14,15]\n
// @lcpr case=end

// @lcpr case=start
// [22,33,22,33,22]\n
// @lcpr case=end

 */

