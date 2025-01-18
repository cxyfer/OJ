/*
 * @lc app=leetcode id=71 lang=cpp
 * @lcpr version=30122
 *
 * [71] Simplify Path
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

// class Solution:
//     """
//         Stack
//     """
//     def simplifyPath(self, path: str) -> str:
//         names = path.split('/')
//         st = []
//         for name in names:
//             if name == '..':
//                 if st: st.pop()
//             elif name and name != ".":
//                 st.append(name)
//         return '/' + '/'.join(st)

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> names;
        // split path by '/'
        string name;
        for (char ch : path) {
            if (ch == '/') {
                if (name.size()) {
                    names.push_back(name);
                    name.clear();
                }
            } else {
                name.push_back(ch);
            }
        }
        if (name.size()) {
            names.push_back(name);
        }
        // Stack
        stack<string> st;
        for (string name : names) {
            if (name == "..") {
                if (!st.empty()) st.pop();
            } else if (name.size() && name != ".") {
                st.push(name);
            }
        }
        // Answer
        string ans;
        while (!st.empty()) {
            ans = "/" + st.top() + ans;
            st.pop();
        }
        return ans.size() ? ans : "/";
    }
};
// @lc code=end



/*
// @lcpr case=start
// "/home/"\n
// @lcpr case=end

// @lcpr case=start
// "/home//foo/"\n
// @lcpr case=end

// @lcpr case=start
// "/home/user/Documents/../Pictures"\n
// @lcpr case=end

// @lcpr case=start
// "/../"\n
// @lcpr case=end

// @lcpr case=start
// "/.../a/../b/c/../d/./"\n
// @lcpr case=end

 */

