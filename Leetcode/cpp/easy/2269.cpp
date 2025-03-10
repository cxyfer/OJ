/*
 * @lc app=leetcode id=2269 lang=cpp
 *
 * [2269] Find the K-Beauty of a Number
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int divisorSubstrings(int num, int k) {
        string s = to_string(num);
        int n = s.size(), ans = 0;
        for (int i = 0; i <= n - k; i++) {
            int x = stoi(s.substr(i, k));
            ans += (x && num % x == 0);
        }
        return ans;
    }
};

class Solution2 {
public:
    int divisorSubstrings(int num, int k) {
        long long base = pow(10, k);
        int ans = 0;
        for (int t = num; t >= base / 10; t /= 10) {
            int x = t % base;
            ans += (x && num % x == 0);
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

int main() {
    Solution sol = Solution();
    cout << sol.divisorSubstrings(240, 2) << endl; // 2
    cout << sol.divisorSubstrings(430043, 2) << endl; // 2
    cout << sol.divisorSubstrings(1000000000, 10) << endl; // 1
    return 0;
}