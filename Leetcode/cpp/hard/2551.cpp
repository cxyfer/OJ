/*
 * @lc app=leetcode.cn id=2551 lang=cpp
 * @lcpr version=30204
 *
 * [2551] Put Marbles in Bags
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
 * 1. Greedy + Sorting: O(nlogn)
 * 2. Greedy + Quick Select: O(n)
 * 3. Greedy + Heap: O(nlogk)
 * 
 * 核心思路都是貪心，利用以下性質：
 * 1. 若選擇 [i, j] 區間，則 j + 1 必選，故可以將 weights[i] + weights[i+1] 視為一個 pair
 * 2. 頭尾 weights[0] 和 weights[n-1] 必選，故在中間的 n - 1 個 pair 中選擇 k - 1 個即可
 */
// @lc code=start
class Solution1 {
public:
    long long putMarbles(vector<int>& weights, int k) {
        if (k == 1) return 0;
        int n = weights.size();
        vector<long long> pairs;
        for (int i = 0; i < n - 1; i++)
            pairs.push_back(weights[i] + weights[i + 1]);
        sort(pairs.begin(), pairs.end());
        long long mn = accumulate(pairs.begin(), pairs.begin() + k - 1, 0LL);
        long long mx = accumulate(pairs.end() - k + 1, pairs.end(), 0LL);
        return mx - mn;
    }
};

class Solution2 {
public:
    long long putMarbles(vector<int>& weights, int k) {
        if (k == 1) return 0;
        int n = weights.size();
        vector<int> pairs;
        for (int i = 0; i < n - 1; i++)
            pairs.push_back(weights[i] + weights[i + 1]);
        long long ans = 0;
        nth_element(pairs.begin(), pairs.begin() + k - 1, pairs.end());
        ans -= accumulate(pairs.begin(), pairs.begin() + k - 1, 0LL);
        nth_element(pairs.begin(), pairs.end() - k + 1, pairs.end());
        ans += accumulate(pairs.end() - k + 1, pairs.end(), 0LL);
        return ans;
    }
};

class Solution3 {
public:
    long long putMarbles(vector<int>& weights, int k) {
        if (k == 1) return 0;
        int n = weights.size();
        // 維護大小為 k-1 的 Min/Max Heap 保存前 k-1 個最大/最小 pair
        priority_queue<int, vector<int>, greater<int>> hp1;
        priority_queue<int> hp2;
        for (int i = 0; i < n - 1; i++) {
            int sum = weights[i] + weights[i + 1];
            if (hp1.size() < k - 1) hp1.push(sum);
            else hp1.push(sum), hp1.pop();
            if (hp2.size() < k - 1) hp2.push(sum);
            else hp2.push(sum), hp2.pop();
        }
        long long ans = 0;
        while (!hp1.empty()) ans += hp1.top(), hp1.pop();
        while (!hp2.empty()) ans -= hp2.top(), hp2.pop();
        return ans;
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// using Solution = Solution3;
// @lc code=end



/*
// @lcpr case=start
// [1,3,5,1]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1, 3]\n2\n
// @lcpr case=end

 */

