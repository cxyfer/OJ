/*
 * @lc app=leetcode.cn id=509 lang=cpp
 * @lcpr version=30204
 *
 * [509] 斐波那契数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int fib(int n) {
        vector<int> memo(n + 1, -1);

        // C++ 23
        auto dfs = [&](this auto&& dfs, int n) -> int {
            if (n <= 1) return n;
            int& res = memo[n];
            if (res != -1) return res;
            return res = dfs(n - 1) + dfs(n - 2);
        };
        return dfs(n);

        // C++ 20
        // auto dfs = [&](auto &&dfs, int n) -> int {
        //     if (n <= 1) return n;
        //     int& res = memo[n];
        //     if (res != -1) return res;
        //     return res = dfs(dfs, n - 1) + dfs(dfs, n - 2);
        // };
        // return dfs(dfs, n);

        // C++ ?
        // function<int(int)> dfs = [&](int n) -> int {
        //     if (n <= 1) return n;
        //     int& res = memo[n];
        //     if (res != -1) return res;
        //     return res = dfs(n - 1) + dfs(n - 2);
        // };
        // return dfs(n);
    }
};

using Solution = Solution1;
// @lc code=end

int main() {
    Solution sol = Solution();
    for (int i = 0; i < 20; i++) {
        cout << sol.fib(i) << endl;
    }
    return 0;
}

/*
// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

// @lcpr case=start
// 4\n
// @lcpr case=end

 */

