/*
 * @lc app=leetcode id=3592 lang=java
 *
 * [3592] Inverse Coin Change
 */

// @lcpr-template-start
import java.util.*;
// @lcpr-template-end
// @lc code=start
class Solution {
    public List<Integer> findCoins(int[] numWays) {
        int n = numWays.length;
        int[] f = new int[n + 1];
        f[0] = 1;
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            int d = numWays[i - 1] - f[i];
            if (d == 1) {
                ans.add(i);
                for (int j = i; j <= n; j++) {
                    f[j] += f[j - i];
                }
            }
            else if (d != 0) {
                return new ArrayList<>();
            }
        }
        return ans;
    }
}
// @lc code=end