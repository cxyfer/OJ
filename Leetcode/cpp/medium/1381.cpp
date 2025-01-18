/*
 * @lc app=leetcode.cn id=1381 lang=cpp
 *
 * [1381] 设计一个支持增量操作的栈
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class CustomStack {
public:
    int top;
    vector<int> st;
    vector<int> lazy;
    CustomStack(int maxSize) {
        top = -1;
        st.resize(maxSize);
        lazy.resize(maxSize);
    }
    
    void push(int x) {
        if (top + 1 == st.size()) return;
        top++;
        st[top] = x;
    }
        
    int pop() {
        if (top == -1) return -1;
        int res = st[top] + lazy[top];
        if (top != 0) lazy[top - 1] += lazy[top]; // Propagate Lazy tag
        lazy[top] = 0; // Clear Lazy tag
        top--;
        return res;

    }
    
    void increment(int k, int val) {
        int idx = min(k - 1, top);
        if (idx >= 0) lazy[idx] += val;
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
// @lc code=end

