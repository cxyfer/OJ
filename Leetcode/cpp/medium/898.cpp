/*
 * @lc app=leetcode.cn id=898 lang=cpp
 * @lcpr version=30204
 *
 * [898] 子数组按位或操作
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1a {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        unordered_set<int> ans, st, st2;
        for (int x : arr) {
            st2.clear();
            for (int y : st)
                st2.insert(y | x);
            st2.insert(x);
            swap(st, st2);
            ans.insert(st.begin(), st.end());
        }
        return ans.size();
    }
};

class Solution1b {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        unordered_set<int> ans;
        vector<int> st;
        for (int x : arr) {
            vector<int> st2 = {x};
            for (int y : st)
                if ((y | x) != st2.back())
                    st2.push_back(y | x);
            st = st2;
            ans.insert(st.begin(), st.end());
        }
        return ans.size();
    }
};

class Solution1c {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        int n = arr.size();
        unordered_set<int> ans;
        for (int i = 0; i < n; i++) {
            ans.insert(arr[i]);
            for (int j = i - 1; j >= 0; j--) {
                if ((arr[j] | arr[i]) == arr[j]) break;
                arr[j] |= arr[i];
                ans.insert(arr[j]);
            }
        }
        return ans.size();
    }
};

// using Solution = Solution1a;
// using Solution = Solution1b;
using Solution = Solution1c;
// @lc code=end



/*
// @lcpr case=start
// [0]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,4]\n
// @lcpr case=end

 */

