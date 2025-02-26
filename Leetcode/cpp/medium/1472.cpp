/*
 * @lc app=leetcode id=1472 lang=cpp
 * @lcpr version=30122
 *
 * [1472] Design Browser History
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
1. Two Stacks
2. Dynamic Array
*/
// @lc code=start
class BrowserHistory1 {
   public:
    stack<string> st1, st2;

    BrowserHistory1(string homepage) {
        st1.push(homepage);
    }

    void visit(string url) {
        st1.push(url);
        while (!st2.empty()) st2.pop();  // clear forward
    }

    string back(int steps) {
        while (steps > 0 && st1.size() > 1) {
            st2.push(st1.top());
            st1.pop();
            steps--;
        }
        return st1.top();
    }

    string forward(int steps) {
        while (steps > 0 && !st2.empty()) {
            st1.push(st2.top());
            st2.pop();
            steps--;
        }
        return st1.top();
    }
};

class BrowserHistory2 {
   public:
    int idx;  // current index
    vector<string> pages;
    BrowserHistory2(string homepage) {
        pages.push_back(homepage);
        idx = 0;
    }

    void visit(string url) {
        pages.erase(pages.begin() + idx + 1, pages.end());  // clear forward
        pages.push_back(url);
        idx++;
    }

    string back(int steps) {
        idx = max(idx - steps, 0);
        return pages[idx];
    }

    string forward(int steps) {
        idx = min(idx + steps, (int)pages.size() - 1);
        return pages[idx];
    }
};

// class BrowserHistory : public BrowserHistory1 {};
class BrowserHistory : public BrowserHistory2 {};
// @lc code=end



/*
// @lcpr case=start
// ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"][["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]\n
// @lcpr case=end

 */
