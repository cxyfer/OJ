/*
 * @lc app=leetcode id=874 lang=rust
 *
 * [874] Walking Robot Simulation
 */

// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
        use std::collections::HashSet;

        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let (mut x, mut y): (i32, i32) = (0, 0);
        let mut d: usize = 0;
        let mut ans: i32 = 0;
        let obstacles: HashSet<(i32, i32)> = obstacles.into_iter().map(|p| (p[0], p[1])).collect();

        for command in commands {
            if command < 0 {
                if command == -1 {
                    d = (d + 1) % 4;
                } else {
                    d = (d + 3) % 4;
                }
            } else {
                for _ in 0..command as usize {
                    let nx = x + dirs[d].0;
                    let ny = y + dirs[d].1;
                    if obstacles.contains(&(nx, ny)) {
                        break;
                    }
                    (x, y) = (nx, ny);
                    ans = ans.max(x * x + y * y);
                }
            }
        }
        ans
    }
}
// @lc code=end
