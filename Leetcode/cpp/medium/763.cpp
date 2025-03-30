/*
 * @lc app=leetcode.cn id=763 lang=cpp
 * @lcpr version=30204
 *
 * [763] 划分字母区间
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size();
        vector<vector<int>> pos(26);
        for (int i = 0; i < n; i++) {
            pos[s[i] - 'a'].push_back(i);
        }

        vector<pair<int, int>> intervals;
        for (auto& p : pos) {
            if (p.empty()) continue;
            intervals.push_back({p.front(), p.back()});
        }
        sort(intervals.begin(), intervals.end());

        vector<int> ans;
        int st = intervals[0].first, ed = intervals[0].second;
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i].first > ed) {
                ans.push_back(ed - st + 1);
                st = intervals[i].first;
                ed = intervals[i].second;
            } else {
                ed = max(ed, intervals[i].second);
            }
        }
        ans.push_back(ed - st + 1);
        return ans;
    }
};

class Solution2 {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size();
        vector<int> last(26, -1);
        for (int i = 0; i < n; i++)
            last[s[i] - 'a'] = i;

        vector<int> ans;
        int st = 0, ed = 0;
        for (int i = 0; i < n; i++) {
            ed = max(ed, last[s[i] - 'a']);
            if (i == ed) {
                ans.push_back(ed - st + 1);
                st = ed + 1;
            }
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// "ababcbacadefegdehijhklij"\n
// @lcpr case=end

// @lcpr case=start
// "eccbbbbdec"\n
// @lcpr case=end

 */

