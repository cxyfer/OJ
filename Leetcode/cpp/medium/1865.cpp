/*
 * @lc app=leetcode.cn id=1865 lang=cpp
 * @lcpr version=30204
 *
 * [1865] 找出和为指定值的下标对
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class FindSumPairs {
public:
    unordered_map<int, int> cnt1, cnt2;
    vector<int> nums2;
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        for (int x : nums1) cnt1[x]++;
        for (int x : nums2) cnt2[x]++;
        this->nums2 = nums2;
    }
    
    void add(int index, int val) {
        cnt2[nums2[index]]--;
        nums2[index] += val;
        cnt2[nums2[index]]++;
    }
    
    int count(int tot) {
        int ans = 0;
        for (auto [k, v] : cnt1) ans += v * cnt2[tot - k];
        return ans;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */
// @lc code=end



/*
// @lcpr case=start
// ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"][[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]\n
// @lcpr case=end

 */

