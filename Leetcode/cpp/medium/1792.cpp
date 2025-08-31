/*
 * @lc app=leetcode.cn id=1792 lang=cpp
 * @lcpr version=30204
 *
 * [1792] 最大平均通过率
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
考慮增加 1 個學生後的貢獻：
  (a + 1)/(b + 1) - a/b
= (ba + b - ab - a)/b(b + 1)
= (b - a)/b(b + 1)

為了避免除法，將比較關係改為乘法
   (b1 - a1) / b1(b1 + 1) > (b2 - a2) / b2(b2 + 1)
=> (b1 - a1) * b2(b2 + 1) > (b2 - a2) * b1(b1 + 1)
*/
// @lc code=start
struct Node {
    int a, b;
    Node (int a, int b) : a(a), b(b) {}
    bool operator < (const Node &other) const {
        return (other.b + 1LL) * other.b * (b - a) < (b + 1LL) * b * (other.b - other.a);
    }
};

class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        int n = classes.size();
        priority_queue<Node> hp;
        for (auto &c : classes) hp.push(Node(c[0], c[1]));
        while (extraStudents--) {
            auto [a, b] = hp.top();
            hp.pop();
            hp.push(Node(a + 1, b + 1));
        }
        double ans = 0;
        while (!hp.empty()) {
            auto [a, b] = hp.top(); hp.pop();
            ans += 1.0 * a / b;
        }
        return ans / n;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,2],[3,5],[2,2]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[2,4],[3,9],[4,5],[2,10]]\n4\n
// @lcpr case=end

 */

