/*
 * @lc app=leetcode.cn id=528 lang=cpp
 * @lcpr version=30204
 *
 * [528] 按权重随机选择
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
    int n;
    vector<int> w, s;
    mt19937 gen;
    uniform_int_distribution<int> dis;
public:
    Solution(vector<int>& w) {
        n = w.size();
        this->w = w;
        s.assign(n, 0);
        s[0] = w[0];
        for (int i = 1; i < n; i++)
            s[i] = s[i - 1] + w[i];
        
        // Initialize random number generator
        random_device rd;
        gen = mt19937(rd());
        dis = uniform_int_distribution<int>(1, s.back());  // [1, sum(w)]
    }
    
    int pickIndex() {
        int x = dis(gen);
        return lower_bound(s.begin(), s.end(), x) - s.begin();
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["Solution","pickIndex"][[[1]],[]]\n
// @lcpr case=end

// @lcpr case=start
// ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"][[[1,3]],[],[],[],[],[]]\n
// @lcpr case=end

 */

