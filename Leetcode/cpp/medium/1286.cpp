/*
 * @lc app=leetcode.cn id=1286 lang=cpp
 *
 * [1286] 字母组合迭代器
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class CombinationIterator {
public:
    int n, k;
    vector<int> comb;
    bool has_next;
    string s;

    CombinationIterator(string characters, int combinationLength) {
        n = characters.size();
        k = combinationLength;
        s = characters;
        comb = vector<int>(k);
        iota(comb.begin(), comb.end(), 0);
        has_next = true;
    }
    
    string next() {
        string ans = "";
        for (int i = 0; i < k; ++i) {
            ans += s[comb[i]];
        }
        bool flag = false;
        for (int i = k - 1; i >= 0 && !flag; --i) {
            if (comb[i] != n - k + i) {
                comb[i]++;
                for (int j = i + 1; j < k; ++j) {
                    comb[j] = comb[j - 1] + 1;
                }
                flag = true;
            }
        }
        if (!flag) {
            has_next = false;
        }
        return ans;
    }
    
    bool hasNext() {
        return has_next;
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
// @lc code=end

