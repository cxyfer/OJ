/*
 * @lc app=leetcode id=1594 lang=rust
 *
 * [1594] Maximum Non Negative Product in a Matrix
 */

// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
const MOD: i64 = 1_000_000_007;

impl Solution {
    pub fn max_product_path(grid: Vec<Vec<i32>>) -> i32 {
        let (m, n): (usize, usize) = (grid.len(), grid[0].len());

        let mut memo: Vec<Vec<Option<(i64, i64)>>> = vec![vec![None; n]; m];
        fn dfs(
            i: usize,
            j: usize,
            m: usize,
            n: usize,
            grid: &Vec<Vec<i32>>,
            memo: &mut Vec<Vec<Option<(i64, i64)>>>,
        ) -> (i64, i64) {
            let x: i64 = grid[i][j] as i64;

            if i == m - 1 && j == n - 1 {
                return (x, x);
            }
            if let Some(res) = memo[i][j] {
                return res;
            }

            let (mut mx, mut mn) = (i64::MIN, i64::MAX);
            if i + 1 < m {
                let (mx1, mn1) = dfs(i + 1, j, m, n, grid, memo);
                mx = mx.max(x * mx1).max(x * mn1);
                mn = mn.min(x * mx1).min(x * mn1);
            }
            if j + 1 < n {
                let (mx2, mn2) = dfs(i, j + 1, m, n, grid, memo);
                mx = mx.max(x * mx2).max(x * mn2);
                mn = mn.min(x * mx2).min(x * mn2);
            }
            memo[i][j] = Some((mx, mn));
            (mx, mn)
        }
        let (ans, _) = dfs(0, 0, m, n, &grid, &mut memo);
        if ans >= 0 {
            (ans % MOD) as i32
        } else {
            -1
        }
    }
}
// @lc code=end
