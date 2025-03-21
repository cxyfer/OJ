/*
 * @lc app=leetcode.cn id=2115 lang=cpp
 * @lcpr version=30204
 *
 * [2115] Find All Possible Recipes from Given Supplies
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        int n = recipes.size();
        unordered_map<string, unordered_set<string>> g;
        unordered_map<string, int> indeg;
        for (int i = 0; i < n; i++) {
            for (auto& ing : ingredients[i]) {
                g[ing].insert(recipes[i]);
                indeg[recipes[i]]++;
            }
        }
        queue<string> q;
        for (auto& s : supplies) q.push(s);
        while (!q.empty()) {
            string u = q.front();
            q.pop();
            for (auto& v : g[u])
                if (--indeg[v] == 0) q.push(v);
        }
        vector<string> ans;
        for (auto& r : recipes)
            if (indeg[r] == 0) ans.push_back(r);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["bread"]\n[["yeast","flour"]]\n["yeast","flour","corn"]\n
// @lcpr case=end

// @lcpr case=start
// ["bread","sandwich"]\n[["yeast","flour"],["bread","meat"]]\n["yeast","flour","meat"]\n
// @lcpr case=end

// @lcpr case=start
// ["bread","sandwich","burger"]\n[["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]\n["yeast","flour","meat"]\n
// @lcpr case=end

// @lcpr case=start
// ["bread"]\n[["yeast","flour"]]\n["yeast"]\n
// @lcpr case=end

 */

