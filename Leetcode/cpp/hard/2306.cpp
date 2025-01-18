/*
 * @lc app=leetcode.cn id=2306 lang=cpp
 *
 * [2306] 公司命名
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
/*
    1. 按照首字母分組
    2. 按照後綴分組 -> C++ 會 TLE
    3. 按照後綴分組 + 預處理集合和交集大小
*/
class Solution1 {
public:
    long long distinctNames(vector<string>& ideas) {
        vector<unordered_set<string>> groups(26);
        for (const string& idea : ideas) {
            groups[idea[0] - 'a'].insert(idea.substr(1));
        }
        long long ans = 0;
        for (int i = 0; i < 26; ++i) {
            for (int j = i + 1; j < 26; ++j) {
                long long intersection = 0;
                for (const string& suffix : groups[i]) {
                    if (groups[j].count(suffix)) {
                        ++intersection;
                    }
                }
                long long unique_A = groups[i].size() - intersection;
                long long unique_B = groups[j].size() - intersection;
                ans += unique_A * unique_B * 2;
            }
        }
        return ans;    
    }
};

class Solution3 {
public:
    long long distinctNames(vector<string>& ideas) {
        vector<int> sz(26, 0);
        vector<vector<int>> intersection(26, vector<int>(26, 0));
        unordered_map<string, vector<int>> groups;
        for (const string& idea : ideas) {
            string suffix = idea.substr(1);
            int B = idea[0] - 'a';
            sz[B]++;
            for (int A : groups[suffix]) {
                intersection[A][B]++;
                intersection[B][A]++;
            }
            groups[suffix].push_back(B);
        }
        long long ans = 0;
        for (int i = 0; i < 26; ++i) {
            for (int j = i + 1; j < 26; ++j) {
                long long m = intersection[i][j];
                ans += (sz[i] - m) * (sz[j] - m) * 2;
            }
        }
        return ans;
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution3 {};
// @lc code=end
int main() {
    Solution sol = Solution();
    vector<string> ideas = {"coffee","donuts","time","toffee"};
    cout << sol.distinctNames(ideas) << endl; // 6
    ideas = {"lack","back"};
    cout << sol.distinctNames(ideas) << endl; // 0
    return 0;
}