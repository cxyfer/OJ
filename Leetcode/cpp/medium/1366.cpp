/*
 * @lc app=leetcode.cn id=1366 lang=cpp
 * @lcpr version=30204
 *
 * [1366] 通过投票对团队排名
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string rankTeams(vector<string>& votes) {
        int m = votes[0].size();
        unordered_map<char, vector<int>> cnts;
        for (char c : votes[0]) cnts[c] = vector<int>(m, 0);
        for (auto& vote : votes)
            for (int i = 0; i < m; i++)
                cnts[vote[i]][i]++;

        string ans = votes[0];
        sort(ans.begin(), ans.end(), [&](char a, char b) {
            for (int i = 0; i < m; i++) {
                if (cnts[a][i] != cnts[b][i]) {
                    return cnts[a][i] > cnts[b][i];
                }
            }
            return a < b;
        });
        return ans;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<string> votes;
    votes = {"ABC","ACB","ABC","ACB","ACB"};
    cout << sol.rankTeams(votes) << endl;
    votes = {"WXYZ","XYZW"};
    cout << sol.rankTeams(votes) << endl;
    votes = {"ZMNAGUEDSJYLBOPHRQICWFXTVK"};
    cout << sol.rankTeams(votes) << endl;
    return 0;
}

/*
// @lcpr case=start
// ["ABC","ACB","ABC","ACB","ACB"]\n
// @lcpr case=end

// @lcpr case=start
// ["WXYZ","XYZW"]\n
// @lcpr case=end

// @lcpr case=start
// ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]\n
// @lcpr case=end

 */

