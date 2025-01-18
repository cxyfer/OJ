/*
 * @lc app=leetcode id=1371 lang=cpp
 * @lcpr version=30122
 *
 * [1371] Find the Longest Substring Containing Vowels in Even Counts
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*  異或前綴和
        令 cur << i 為 1 表示第 i 個母音出現奇數次，0 表示出現偶數次。
        若某個狀態的 第 a, b 個母音為 1 ，則要找到另外一個狀態其第 a, b 個母音也為 1 ，兩者間構成的字串才能滿足條件，
        也就是滿足當前狀態的狀態就是自己本身，因此只需保存每個狀態「最早」出現的位置，當再次出現時計算兩者間的距離即可。
    */
    int findTheLongestSubstring(string s) {
        string vowels = "aeiou";
        // unordered_map<int, int> last; // 保存每個狀態「最早」出現的位置
        map<int, int> last; // 保存每個狀態「最早」出現的位置
        last[0] = -1; // 空字串
        int ans = 0, cur = 0;
        for (int i = 0; i < s.size(); i++) {
            int idx = vowels.find(s[i]);
            if (idx != -1) {
                cur ^= 1 << idx;
            }
            if (last.find(cur) == last.end()) { // 這個狀態還沒出現過
                last[cur] = i;
            } else { // 這個狀態出現過，那兩者之間的子串就是符合條件的子串
                ans = max(ans, i - last[cur]);
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "eleetminicoworoep"\n
// @lcpr case=end

// @lcpr case=start
// "leetcodeisgreat"\n
// @lcpr case=end

// @lcpr case=start
// "bcbcbc"\n
// @lcpr case=end

 */

