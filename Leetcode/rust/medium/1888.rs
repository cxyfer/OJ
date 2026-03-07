/*
 * @lc app=leetcode id=1888 lang=rust
 *
 * [1888] Minimum Number of Flips to Make the Binary String Alternating
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
use std::cmp::min;

impl Solution {
    pub fn min_flips(s: String) -> i32 {
        let s = s.as_bytes();
        let n = s.len();
        let mut ans = n;
        let mut cnt = 0;
        for r in 0..(n * 2 - 1) {
            if (s[r % n] as usize ^ r) & 1 != 0 {
                cnt += 1;
            }
            if r >= n - 1 {
                ans = min(ans, min(cnt, n - cnt));
                let left = r - n + 1;
                if (s[left % n] as usize ^ left) & 1 != 0 {
                    cnt -= 1;
                }
            }
        }
        ans as i32
    }
}
// @lc code=end

