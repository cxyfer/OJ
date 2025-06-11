/*
 * @lc app=leetcode.cn id=3445 lang=cpp
 * @lcpr version=30204
 *
 * [3445] 奇偶频次间的最大差值 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.size();
        int ans = INT_MIN / 2;
        vector<int> cnt(10);
        for (int i = 0; i < n; i++) cnt[s[i] - '0']++;
        for (int a = 0; a < 10; a++) {
            for (int b = 0; b < 10; b++) {
                if (a == b || cnt[a] == 0 || cnt[b] == 0) continue;
                vector<int> sa(n + 1), sb(n + 1), mns(4, INT_MAX / 2);
                int left = 0;
                for (int i = 1; i <= n; i++) {
                    sa[i] = sa[i - 1] + (s[i - 1] - '0' == a);
                    sb[i] = sb[i - 1] + (s[i - 1] - '0' == b);
                    while (left <= i - k && sa[left] != sa[i] && sb[left] != sb[i]) {
                        int idx = ((sa[left] & 1) << 1) | (sb[left] & 1);
                        mns[idx] = min(mns[idx], sa[left] - sb[left]);
                        left++;
                    }
                    int idx = (((sa[i] & 1) ^ 1) << 1) | (sb[i] & 1);
                    ans = max(ans, sa[i] - sb[i] - mns[idx]);
                }
            }
        }
        return ans;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    // cout << sol.maxDifference("12233", 4) << endl;  // -1
    // cout << sol.maxDifference("1122211", 3) << endl;  // 1
    cout << sol.maxDifference("110", 3) << endl;  // 0
    return 0;
}


/*
// @lcpr case=start
// "12233"\n4\n
// @lcpr case=end

// @lcpr case=start
// "1122211"\n3\n
// @lcpr case=end

// @lcpr case=start
// "110"\n3\n
// @lcpr case=end

 */

