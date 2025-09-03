/*
 * @lc app=leetcode.cn id=493 lang=cpp
 * @lcpr version=30204
 *
 * [493] 翻转对
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class BIT {  // PURQ, 1-based
private:
    vector<int> tree;

public:
    BIT(int n) {
        tree = vector<int>(n + 1, 0);
    }

    void add(int k, int x) {  // 令 nums[k] += x
        for (; k < tree.size(); k += k & -k) tree[k] += x;
    }

    int preSum(int k) {  // 求 nums[:k+1] 之和
        int res = 0;
        for (; k > 0; k -= k & -k) res += tree[k];
        return res;
    }

    int query(int l, int r) {  // 求 nums[l:r+1] 之和
        if (l > r) return 0;
        return preSum(r) - preSum(l - 1);
    }
};

class Solution {
public:
    int reversePairs(vector<int>& nums) {
        int n = nums.size();
        // 離散化
        set<long long> B;
        for (auto x : nums) B.insert(x), B.insert(2LL * x);
        unordered_map<long long, int> mp;
        int idx = 1;
        for (auto x : B) mp[x] = idx++;

        // BIT
        int m = B.size();
        BIT bit(m);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += i - bit.query(1, mp[2LL * nums[i]]);
            bit.add(mp[nums[i]], 1);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,3,2,3,1]\n
// @lcpr case=end

// @lcpr case=start
// [2,4,3,5,1]\n
// @lcpr case=end

 */

