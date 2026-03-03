/*
 * @lc app=leetcode id=1545 lang=rust
 *
 * [1545] Find Kth Bit in Nth Binary String
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        let mut length = [0i32; 21];
        for i in 1..=20 {
            length[i] = length[i - 1] * 2 + 1;
        }

        fn dfs(n: usize, k: i32, length: &[i32; 21]) -> i32 {
            if n == 1 {
                return 0;
            }
            let m = length[n - 1] + 1;
            if k < m {
                dfs(n - 1, k, length)
            } else if k == m {
                1
            } else {
                dfs(n - 1, m - (k - m), length) ^ 1
            }
        }

        (b'0' + dfs(n as usize, k as i32, &length) as u8) as char
    }
}
// @lc code=end

