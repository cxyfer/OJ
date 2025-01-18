/*
 * @lc app=leetcode.cn id=1122 lang=cpp
 *
 * [1122] 数组的相对排序
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> rank;
        for (int i = 0; i < arr2.size(); i++) rank[arr2[i]] = i;
        sort(arr1.begin(), arr1.end(), [&](int x, int y) {
            if (rank.count(x)) {
                return rank.count(y) ? rank[x] < rank[y] : true;
            } else {
                return rank.count(y) ? false : x < y;
            }
        });
        return arr1;
    }
};

class Solution2 {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        vector<int> cnt(1001);
        for (int x : arr1) cnt[x]++;
        int i = 0;
        for (int x : arr2)
            while (cnt[x]-- > 0)
                arr1[i++] = x;
        for (int x = 0; x < 1001; x++)
            while (cnt[x]-- > 0)
                arr1[i++] = x;
        return arr1;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

    