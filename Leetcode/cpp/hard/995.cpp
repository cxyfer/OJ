/*
 * @lc app=leetcode id=995 lang=cpp
 *
 * [995] Minimum Number of K Consecutive Bit Flips
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
/*
    1. Differece Array
        把區間翻轉的操作轉換為差分陣列的操作
    2. Sliding Window

    相比 Python 程式碼，將只關注奇偶性的部分轉換為 XOR 運算
*/

class Solution1 {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0, cur = 0;
        vector<int> diff(n + 1, 0);
        for (int i = 0; i < n; i++) {
            cur ^= diff[i];
            if (nums[i] == cur) {
                if (i + k > n) return -1;
                ans++;
                cur ^= 1;
                diff[i + k] ^= 1;
            }
        }
        return ans;
    }
};

class Solution2 {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            if (i >= k && nums[i - k] > 1) {
                cur ^= 1;
                nums[i - k] -= 2;
            }
            if (nums[i] == cur) {
                if (i + k > n) return -1;
                nums[i] += 2;
                cur ^= 1;
                ans++;
            }
        }
        return ans;
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// @lc code=end

// class Solution(Solution1):
// # class Solution(Solution2):
//     pass