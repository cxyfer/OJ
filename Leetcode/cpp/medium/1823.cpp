/*
 * @lc app=leetcode.cn id=1823 lang=cpp
 *
 * [1823] 找出游戏的获胜者
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int findTheWinner(int n, int k) {
        queue<int> q;
        for (int i = 1; i <= n; i++) q.push(i);
        while (q.size() > 1) {
            for (int i = 0; i < k-1; i++) {
                q.push(q.front());
                q.pop();
            }
            q.pop();
        }
        return q.front();
    }
};

class Solution2 {
public:
    int findTheWinner(int n, int k) {
        return (n == 1) ? 1 : (findTheWinner(n-1, k) + k - 1) % n + 1;
    }
};

class Solution3 {
public:
    int findTheWinner(int n, int k) {
        int ans = 1;
        for (int i = 2; i <= n; i++) {
            ans = (ans + k - 1) % i + 1;
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
class Solution : public Solution3 {};
// @lc code=end

