/*
 * @lc app=leetcode.cn id=767 lang=cpp
 * @lcpr version=30204
 *
 * [767] 重构字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    string reorganizeString(string s) {
        int n = s.size();
        map<char, int> cnt;
        int mx = 0;
        for (char ch : s) {
            cnt[ch]++;
            mx = max(mx, cnt[ch]);
        }

        if (mx > (n + 1) / 2) return "";

        vector<pair<char, int>> vec;
        for (auto [ch, v] : cnt) vec.emplace_back(ch, v);
        sort(vec.begin(), vec.end(), [](pair<char, int> a, pair<char, int> b) {
            return a.second > b.second;
        });
        
        int idx = 0;
        vector<string> buckets(mx);
        for (auto [ch, v] : vec) {
            for (int i = 0; i < v; i++) {
                buckets[idx].push_back(ch);
                idx = (idx + 1) % mx;
            }
        }
        string ans;
        for (auto bucket : buckets) ans += bucket;
        return ans;
    }
};

class Solution2 {
public:
    string reorganizeString(string s) {
        int n = s.size();
        map<char, int> cnt;
        char m;
        int mx = 0;
        for (char ch : s) {
            cnt[ch]++;
            if (cnt[ch] > mx) {
                mx = cnt[ch];
                m = ch;
            }
        }

        if (mx > (n + 1) / 2) return "";

        string ans(n, ' ');
        int idx = 0;

        // 先填入出現次數最多的字元
        for (int j = 0; j < mx; j++) {
            ans[idx] = m;
            idx += 2;
        }
        cnt.erase(m);

        // 填入其他字元，注意當偶數位填滿時，要從奇數位開始填
        for (auto [ch, v] : cnt) {
            for (int i = 0; i < v; i++) {
                if (idx >= n) idx = 1;
                ans[idx] = ch;
                idx += 2;
            }
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

int main() {
    Solution sol = Solution();
    string s = "vvvlo";
    cout << sol.reorganizeString(s) << endl;  // "vlvov"
    return 0;
}

/*
// @lcpr case=start
// "aab"\n
// @lcpr case=end

// @lcpr case=start
// "aaab"\n
// @lcpr case=end

 */

