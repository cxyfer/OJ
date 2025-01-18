/*
 * @lc app=leetcode.cn id=53 lang=cpp
 *
 * [53] 最大子数组和
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
 public:
  int maxSubArray(vector<int>& nums) {
    int ans = INT_MIN, s = 0, mn = 0;
    for (int x : nums) {
      s += x;
      ans = max(ans, s - mn);
      mn = min(mn, s);
    }
    return ans;
  }
};

class Solution2a {
 public:
  int maxSubArray(vector<int>& nums) {
    int n = nums.size();
    vector<int> f(n + 1, -INT_MAX / 2);
    for (int i = 0; i < n; ++i) {
      f[i + 1] = max(f[i] + nums[i], nums[i]);
    }
    return *max_element(f.begin(), f.end());
  }
};

class Solution2b {
 public:
  int maxSubArray(vector<int>& nums) {
    int ans = INT_MIN, f = 0;
    for (int x : nums) {
      f = max(f + x, x);
      ans = max(ans, f);
    }
    return ans;
  }
};

struct Node {
  int lSum, rSum, mSum, tot;
};

class Solution3 {
 public:
  int maxSubArray(vector<int>& nums) {
    auto query = [&](auto&& query, int l, int r) -> Node {
      if (l == r) return Node{nums[l], nums[l], nums[l], nums[l]};
      int mid = (l + r) >> 1;
      auto ls = query(query, l, mid);
      auto rs = query(query, mid + 1, r);
      // Combine
      int lSum = max(ls.lSum, ls.tot + rs.lSum);
      int rSum = max(rs.rSum, rs.tot + ls.rSum);
      int mSum = max(max(ls.mSum, rs.mSum), ls.rSum + rs.lSum);
      int tot = ls.tot + rs.tot;
      return Node{lSum, rSum, mSum, tot};
    };
    return query(query, 0, nums.size() - 1).mSum;
  }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2a {};
// class Solution : public Solution2b {};
class Solution : public Solution3 {};
// @lc code=end
