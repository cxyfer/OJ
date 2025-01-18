/*
 * @lc app=leetcode.cn id=2748 lang=cpp
 *
 * [2748] 美丽下标对的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int countBeautifulPairs(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                int y = nums[i];
                while (y >= 10) {
                    y /= 10;
                }
                int x = nums[j] % 10;
                if (gcd(y, x) == 1) { // or __gcd
                    ans++;
                }
            }
        }
        return ans;
    }
    int gcd(int a, int b) {
        return b ? gcd(b, a % b) : a;
    }
};

class Solution2 {
public:
    int countBeautifulPairs(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        vector<int> cnt(10);
        for (int x : nums) {
            for (int y = 1; y < 10; y++) {
                if (gcd(y, x % 10) == 1) { // or __gcd
                    ans += cnt[y];
                }
            }
            while (x >= 10) {
                x /= 10;
            }
            cnt[x]++;
        }
        return ans;
        
    }
    int gcd(int a, int b) {
        return b ? gcd(b, a % b) : a;
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// @lc code=end

