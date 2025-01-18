/*
 * @lc app=leetcode id=881 lang=cpp
 * @lcpr version=30122
 *
 * [881] Boats to Save People
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int ans = 0;
        sort(people.begin(), people.end());
        int i = 0, j = people.size() - 1;
        while (i <= j) {
            if (people[i] + people[j] > limit) {
                j--;
            } else {
                i++; j--;
            }
            ans++;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2]\n3\n
// @lcpr case=end

// @lcpr case=start
// [3,2,2,1]\n3\n
// @lcpr case=end

// @lcpr case=start
// [3,5,3,4]\n5\n
// @lcpr case=end

 */

