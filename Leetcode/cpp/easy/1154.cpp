/*
 * @lc app=leetcode id=1154 lang=cpp
 * @lcpr version=30112
 *
 * [1154] Day of the Year
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
vector<int> month = {31,28,31,30,31,30,31,31,30,31,30,31};
vector<int> pre_sum(13,0);
void init(){
    for(int i=1;i<=12;i++){
        pre_sum[i] = pre_sum[i-1] + month[i-1];
    }
}
class Solution {
public:
    Solution(){
        init();
    }
    int dayOfYear(string date) {
        int y=0,m=0,d=0;
        y = stoi(date.substr(0,4));
        m = stoi(date.substr(5,2));
        d = stoi(date.substr(8,2));
        bool is_leap = (y%4==0 && y%100!=0) || y%400==0;
        if(is_leap && m>2) d++;
        return pre_sum[m-1] + d;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "2019-01-09"\n
// @lcpr case=end

// @lcpr case=start
// "2019-02-10"\n
// @lcpr case=end

 */

