/*
 * @lc app=leetcode id=3296 lang=rust
 *
 * [3296] Minimum Number of Seconds to Make Mountain Height Zero
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
struct Solution1;
impl Solution1 {
    pub fn min_number_of_seconds(mountain_height: i32, worker_times: Vec<i32>) -> i64 {
        let mountain_height = mountain_height as i64;
        let check = |m: i64| -> bool {
            let mut tot: i64 = 0;
            for &t in &worker_times {
                tot += ((-1 + (1 + 8 * m / (t as i64)).isqrt()) / 2) as i64;
                if tot >= mountain_height {
                    return true;
                }
            }
            false
        };

        let h: i64 = (mountain_height as f64 / worker_times.len() as f64).ceil() as i64;
        let max_t: i64 = *worker_times.iter().max().unwrap() as i64;

        let mut left: i64 = 0;
        let mut right: i64 = max_t * h * (h + 1) / 2;
        while left <= right {
            let mid = left + (right - left) / 2;
            if check(mid) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}

use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct Solution2;
impl Solution2 {
    pub fn min_number_of_seconds(mountain_height: i32, worker_times: Vec<i32>) -> i64 {
        let mut hp = BinaryHeap::new();
        for &t in &worker_times {
            hp.push(Reverse((t as i64, t as i64, 1)));
        }

        let mut ans: i64 = 0;
        for _ in 0..mountain_height {
            let Reverse((t, d, m)) = hp.pop().unwrap();
            ans = t;
            hp.push(Reverse((t + d * (m + 1), d, m + 1)));
        }
        ans
    }
}

impl Solution {
    pub fn min_number_of_seconds(mountain_height: i32, worker_times: Vec<i32>) -> i64 {
        Solution1::min_number_of_seconds(mountain_height, worker_times)
        // Solution2::min_number_of_seconds(mountain_height, worker_times)
    }
}
// @lc code=end

