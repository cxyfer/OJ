/*
 * @lc app=leetcode.cn id=2140 lang=cpp
 *
 * [2140] 解决智力问题
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        vector<long long> memo(n, -1);
        // 這題直接寫 lambda 會 TLE，需要用 auto && f
        auto f = [&](auto && f, int i) -> long long {
            if (i >= n) return 0;
            long long & res = memo[i];
            if (res != -1) return res;
            long long res1 = f(f, i + 1);
            long long res2 = questions[i][0] + f(f, i + questions[i][1] + 1);
            return res = max(res1, res2);
        };
        return f(f, 0);
    }
};

class Solution2 {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        vector<long long> f(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) {
            f[i] = max(f[i+1], questions[i][0] + f[min(i + questions[i][1] + 1, n)]);
        }
        return f[0];
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<vector<int>> questions = {{1,1},{2,2},{3,3},{4,4}};
    cout << sol.mostPoints(questions) << endl;
    return 0;
}