/*
 * @lc app=leetcode.cn id=2982 lang=cpp
 *
 * [2982] 找出出现至少三次的最长特殊子字符串 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        1. Counter
          O(n + 26 * n)
        2. Sort
          O(n + 26 nlogn)
        3. Min Heap
          O(n log 3 + 26 * 3 log 3)
    */
    int maximumLength(string s) {
        return solve1(s);
        // return solve2(s);
        // return solve3(s);
    }
    int solve1(string s) {
        int n = s.size(), i = 0;
        vector<vector<int>> groups(26, vector<int>(n+1, 0));
        while (i < n){ // 分組循環
            int st = i++;
            while (i < n && s[i] == s[st]) i++;
            // for (int k = 1; k <= i - st; k++) // 長度為 k 的子字串有 i - st - k + 1 個
            for (int k = i - st; k >= max(1, i - st - 2); k--) // 其實最多考慮 3 個就夠了
                groups[s[st] - 'a'][k] += (i - st) - k + 1; 
        }
        int ans = -1;
        for (auto g : groups)
            // for (int i = n; i > 0; i--)
            for (int i = n-2; i > 0; i--) // 需要出現至少 3 次
                if (g[i] >= 3){ // 滿足條件
                    ans = max(ans, i);
                    break;
                }
        return ans;
    }
    int solve2(string s) {
        int n = s.size(), i = 0;
        vector<vector<int>> groups(26, vector<int>());
        while (i < n){
            int st = i++;
            while (i < n && s[i] == s[st]) i++;
            groups[s[st] - 'a'].push_back(i - st);
        }
        int ans = 0;
        for (auto g : groups){
            int m = g.size();
            if (m == 0) continue;
            sort(g.begin(), g.end(), greater<int>());
            ans = max(ans, g[0] - 2);
            if (m > 1) ans = max(ans, min(g[0] - 1, g[1]));
            if (m > 2) ans = max(ans, g[2]);
        }
        return ans > 0 ? ans : -1;
    }
    int solve3(string s) {
        int n = s.size(), i = 0;
        priority_queue<int, vector<int>, greater<int>> groups[26]; // Min heap
        while (i < n){
            int st = i++;
            while (i < n && s[i] == s[st]) i++;
            groups[s[st] - 'a'].push(i - st);
            if (groups[s[st] - 'a'].size() > 3) groups[s[st] - 'a'].pop();
        }
        int ans = 0;
        for (auto g : groups){
            int m = g.size();
            if (m == 0) continue;
            vector<int> tmp(3, 0);
            for (int i = m-1; i >= 0; i--) tmp[i] = g.top(), g.pop();
            ans = max({ans, tmp[0] - 2, min(tmp[0] - 1, tmp[1]), tmp[2]});
        }
        return ans > 0 ? ans : -1;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    cout << sol.maximumLength("aaaa") << endl; // 2
    cout << sol.maximumLength("abcdef") << endl; // -1
    cout << sol.maximumLength("abcaba") << endl; // 1
    return 0;
}