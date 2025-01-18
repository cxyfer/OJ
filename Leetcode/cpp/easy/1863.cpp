/*
 * @lc app=leetcode.cn id=1863 lang=cpp
 *
 * [1863] 找出所有子集的异或总和再求和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        1. Brute force + Backtracking / Bit Manipulation
          O(n * 2^n)
        2. Math + Bit Manipulation
          按位考慮，考慮每個子集中該位 1 的個數
          - 若該子集中該位 1 的個數為奇數，則該位的 XOR 和為 1
          - 若該子集中該位 1 的個數為偶數，則該位的 XOR 和為 0

          接著考慮所有子集中該位的 XOR 和
          - 若所有元素中的該位皆為 0 ，則所有 2^n 個子集中，該位的 XOR 和顯然為 0
          - 若至少有一個元素中的該位為 1，則總共有 2^(n-1) 個子集中該位 1 的個數為奇數、2^(n-1) 個子集中該位 1 的個數為偶數，證明參考官解

          若第 i 位中至少有一個元素的該位為 1，則該位對答案的貢獻為 2^(n-1) * 2^i
          所以只要用判斷所有元素中是否有一個元素的該位為 1 即可，可以計算所有元素的 OR 值，最後左移 n-1 位即可

          O(n)
    */
    int subsetXORSum(vector<int>& nums) {
        // return solve1(nums);
        return solve2(nums);
    }
    int solve1(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        for (int i = 1; i < (1 << n); i++) { // 枚舉所有子集，狀態壓縮
            int cur = 0; // 當前子集的 XOR 和
            for (int j = 0; j < n; j++){ // 當前元素是否在子集中
                if (i & (1 << j)) cur ^= nums[j];
            }
            ans += cur;
        }
        return ans;
    }
    int solve2(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        for (int x : nums) ans |= x;
        return ans << (n - 1);
    }
};
// @lc code=end

