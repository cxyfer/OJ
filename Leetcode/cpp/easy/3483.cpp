/*
 * @lc app=leetcode.cn id=3483 lang=cpp
 * @lcpr version=30204
 *
 * [3483] Unique 3-Digit Even Numbers
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int totalNumbers(vector<int>& digits) {
        int n = digits.size();
        unordered_set<int> st;
        for (int i = 0; i < n; i++) {
            if (digits[i] == 0) continue;
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                for (int k = 0; k < n; k++) {
                    if (k == i || k == j || digits[k] & 1) continue;
                    st.insert(digits[i] * 100 + digits[j] * 10 + digits[k]);
                }
            }
        }
        return st.size();
    }
};

class Solution2 {
public:
    int totalNumbers(vector<int>& digits) {
        int ans = 0;
        vector<int> cnt(10);
        for (int x : digits) cnt[x]++;
        for (int x = 1; x < 10; x++) {
            if (cnt[x] == 0) continue;
            cnt[x]--;
            for (int y = 0; y < 10; y++) {
                if (cnt[y] == 0) continue;
                cnt[y]--;
                for (int z = 0; z < 10; z += 2) {
                    if (cnt[z] == 0) continue;
                    ans++;
                }
                cnt[y]++;
            }
            cnt[x]++;
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4]\n
// @lcpr case=end

// @lcpr case=start
// [0,2,2]\n
// @lcpr case=end

// @lcpr case=start
// [6,6,6]\n
// @lcpr case=end

// @lcpr case=start
// [1,3,5]\n
// @lcpr case=end

 */

