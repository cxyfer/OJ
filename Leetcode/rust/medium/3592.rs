/*
 * @lc app=leetcode id=3592 lang=rust
 *
 * [3592] Inverse Coin Change
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn find_coins(num_ways: Vec<i32>) -> Vec<i32> {
        let n = num_ways.len();
        let mut f = vec![0; n + 1];
        f[0] = 1;
        let mut ans = Vec::new();
        for i in 1..=n {
            let d = num_ways[i - 1] - f[i];
            if d == 1 {
                ans.push(i as i32);
                for j in i..=n {
                    f[j] += f[j - i];
                }
            } else if d != 0 {
                return Vec::new();
            }
        }
        ans
    }
}
// @lc code=end

