/*
 * @lc app=leetcode.cn id=1442 lang=cpp
 *
 * [1442] 形成两个异或相等数组的三元组数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int n;
    vector<int> pre;
    int countTriplets(vector<int>& arr) {
        n = arr.size();
        pre = vector<int>(n + 1);
        for (int i = 0; i < n; i++) pre[i + 1] = pre[i] ^ arr[i];
        // return solve1(arr);
        // return solve2(arr);
        // return solve3a(arr);
        return solve3b(arr);
    }
    int solve1(vector<int>& arr) {
        int ans = 0;
        for (int i = 0; i < n; i++) // i < j <= k
            for (int j = i+1; j < n; j++)
                for (int k = j; k < n; k++)
                    // if ((pre[i] ^ pre[j]) == (pre[j] ^ pre[k+1])) ans++;
                    if (pre[i] == pre[k+1]) ans++;
        return ans;
    }
    int solve2(vector<int>& arr) {
        int ans = 0;
        for (int i = 0; i < n; i++) // i < j <= k
            for (int k = i+1; k < n; k++)
                if (pre[i] == pre[k+1]) ans += k - i; // (i, i+1, k), (i, i+2, k), ..., (i, k, k)
        return ans;
    }
    int solve3a(vector<int>& arr) {
        int ans = 0;
        unordered_map<int, vector<int>> pos;
        for (int k = 0; k < n; k++) {
            if (pos.count(pre[k+1])) {
                for (int i : pos[pre[k+1]]) {
                    ans += k - i;
                }
            }
            pos[pre[k]].push_back(k);
        }
        return ans;
    }
    int solve3b(vector<int>& arr) {
        int ans = 0;
        unordered_map<int, int> cnt, tot;
        for (int k = 0; k < n; k++) {
            if (cnt.count(pre[k+1])) {
                ans += cnt[pre[k+1]] * k - tot[pre[k+1]];
            }
            cnt[pre[k]]++;
            tot[pre[k]] += k;
        }
        return ans;
    }
};
// @lc code=end

