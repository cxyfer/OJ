/*
 * @lc app=leetcode id=1888 lang=cpp
 *
 * [1888] Minimum Number of Flips to Make the Binary String Alternating
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minFlips(string s) {
        int n = s.size();
        int ans = n;
        int cnt = 0;
        for (int r = 0; r < n * 2 - 1; r++) {
            if ((s[r % n] ^ r) & 1) cnt++;
            if (r >= n - 1) {
                ans = min({ans, cnt, n - cnt});
                int left = r - n + 1;
                if ((s[left] ^ left) & 1) cnt--;
            }
        }
        return ans;
    }
};
// @lc code=end

