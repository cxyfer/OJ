/*
 * @lc app=leetcode id=3635 lang=rust
 *
 * [3635] Earliest Finish Time for Land and Water Rides II
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn earliest_finish_time(land_start_time: Vec<i32>, land_duration: Vec<i32>, water_start_time: Vec<i32>, water_duration: Vec<i32>) -> i32 {
        let land: Vec<(i32, i32)> = land_start_time.iter().zip(land_duration.iter()).map(|(&s, &d)| (s, d)).collect();
        let water: Vec<(i32, i32)> = water_start_time.iter().zip(water_duration.iter()).map(|(&s, &d)| (s, d)).collect();

        fn calc(intervals1: &[(i32, i32)], intervals2: &[(i32, i32)]) -> i32 {
            let min_ed = intervals1.iter().map(|&(st, d)| st + d).min().unwrap();
            intervals2.iter().map(|&(st, d)| min_ed.max(st) + d).min().unwrap()
        }

        calc(&land, &water).min(calc(&water, &land))
    }
}
// @lc code=end

