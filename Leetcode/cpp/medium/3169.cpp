/*
 * @lc app=leetcode.cn id=3169 lang=cpp
 *
 * [3169] 无需开会的工作日
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
 * 1. Merge Intervals
 *    - Similar to 56. Merge Intervals
 * 2. Prefix Sum + Line Sweep
 */
// @lc code=start
const int BIT = 32;
const int LEN = 8;
const int SIZE = 1 << LEN;
const int MASK = SIZE - 1;

void radixSort(vector<pair<int, int>>& vec) {
    int n = vec.size();
    vector<pair<int, int>> temp(n);
    vector<int> buckets(SIZE);
    
    for (int shift = 0; shift < BIT; shift += LEN) {
        fill(buckets.begin(), buckets.end(), 0);
        
        for (const auto& x : vec)
            buckets[(x.first >> shift) & MASK]++;
        
        for (int i = 1; i < SIZE; i++)
            buckets[i] += buckets[i - 1];
        
        for (int i = n - 1; i >= 0; i--)
            temp[--buckets[(vec[i].first >> shift) & MASK]] = vec[i];
        
        swap(vec, temp);
    }
}

class Solution1a {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        vector<pair<int, int>> merged;
        for (auto& m : meetings) {
            int x = m[0], y = m[1];
            if (merged.empty() || merged.back().second < x)
                merged.emplace_back(x, y);
            else
                merged.back().second = max(merged.back().second, y);
        }

        int ans = days;
        for (auto& [x, y] : merged)  // [x, y] is invalid
            ans -= y - x + 1;
        return ans;
    }
};

class Solution1b {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        vector<pair<int, int>> vec;
        for (auto& m : meetings) vec.emplace_back(m[0], m[1]);
        radixSort(vec);
        int ans = days, st = 0, ed = -1;
        for (auto& [x, y] : vec) {
            if (x > ed) {
                ans -= (ed - st + 1);  // [st, ed] is invalid
                st = x;
                ed = y;
            } else
                ed = max(ed, y);
        }
        ans -= (ed - st + 1);  // [st, ed] is invalid
        return ans;
    }
};

class Solution1c {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        int ans = 0, ed = 0;
        for (auto& m : meetings) {
            int x = m[0], y = m[1];
            if (x > ed) {
                ans += x - ed - 1;  // [ed + 1, x - 1] is valid
                ed = y;
            } else
                ed = max(ed, y);
        }
        ans += days - ed;  // [ed + 1, days] is valid
        return ans;
    }
};

class Solution2 {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        map<int, int> mp;
        for (auto& m : meetings) {
            mp[m[0]] += 1;
            mp[m[1] + 1] -= 1;
        }
        int ans = 0, s = 0, pre = 1;
        for (auto& [d, v] : mp) {
            if (s == 0) ans += d - pre;  // [pre, d - 1] is valid
            s += v;
            pre = d;
        }
        ans += days - pre + 1;  // [pre, days] is valid
        return ans;
    }
};

class Solution2b {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        vector<pair<int, int>> vec;
        for (auto& m : meetings) {
            vec.emplace_back(m[0], 1);
            vec.emplace_back(m[1] + 1, -1);
        }
        radixSort(vec);
        
        int ans = 0, s = 0, pre = 1;
        for (int i = 0; i < vec.size(); i++) {
            auto [d, v] = vec[i];
            while (i + 1 < vec.size() && vec[i + 1].first == d) {
                v += vec[++i].second;
            }
            if (s == 0) ans += d - pre;  // [pre, d - 1] is valid
            s += v;
            pre = d;
        }
        ans += days - pre + 1;  // [pre, days] is valid
        return ans;
    }
};

// using Solution = Solution1a;
using Solution = Solution1b;
// using Solution = Solution1c;
// using Solution = Solution2;
// using Solution = Solution2b;
// @lc code=end