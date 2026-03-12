/*
 * @lc app=leetcode id=3600 lang=rust
 *
 * [3600] Maximize Spanning Tree Stability with Upgrades
 */

// @lcpr-template-start
pub struct Solution;
// @lcpr-template-end
// @lc code=start
#[derive(Clone)]
struct UnionFind {
    pa: Vec<usize>,
    sz: Vec<usize>,
    cnt: usize,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        UnionFind {
            pa: (0..n).collect(),
            sz: vec![1; n],
            cnt: n,
        }
    }

    fn find(&mut self, mut x: usize) -> usize {
        if self.pa[x] != x {
            self.pa[x] = self.find(self.pa[x]);
        }
        self.pa[x]
    }

    fn union(&mut self, x: usize, y: usize) -> bool {
        let mut fx = self.find(x);
        let mut fy = self.find(y);
        if fx == fy {
            return false;
        }
        if self.sz[fx] < self.sz[fy] {
            std::mem::swap(&mut fx, &mut fy);
        }
        self.pa[fy] = fx;
        self.sz[fx] += self.sz[fy];
        self.cnt -= 1;
        true
    }
}

impl Solution {
    pub fn max_stability(n: i32, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let mut min_w = i32::MAX;
        let mut max_w = i32::MIN;
        
        // 必選邊不能成環
        let mut uf0 = UnionFind::new(n as usize);
        for e in &edges {
            let (u, v, w, must) = (e[0] as usize, e[1] as usize, e[2], e[3] == 1);
            min_w = min_w.min(w);
            max_w = max_w.max(w);
            if must && !uf0.union(u, v) {
                return -1;
            }
        }

        // 最大化最小值 -> 二分
        let check = |mid: i32| -> bool {
            let mut uf = uf0.clone();
            for e in &edges {
                let (u, v, w, must) = (e[0] as usize, e[1] as usize, e[2], e[3] == 1);
                if must && w < mid {  // 必選邊不能 < mid
                    return false;
                } else if !must && w >= mid {  // 非必選邊 >= mid 不用代價，直接使用
                    uf.union(u, v);
                }
            }

            let mut cost = 0;
            if k > 0 && uf.cnt > 1 {
                // 在代價邊數不超過 k 的情況下，使用支付代價後能 >= mid 的非必選邊
                for e in &edges {
                    let (u, v, w, must) = (e[0] as usize, e[1] as usize, e[2], e[3] == 1);
                    if !must && w < mid && 2 * w >= mid {
                        if uf.union(u, v) {
                            cost += 1;
                            if cost == k || uf.cnt == 1 {
                                break;
                            }
                        }
                    }
                }
            }
            uf.cnt == 1
        };

        // 每條邊只能操作最多一次，所以右界為 max_w * 2
        let mut left: i32 = min_w;
        let mut right: i32 = max_w * 2;
        while left <= right {
            let mid = left + (right - left) / 2;
            if check(mid) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        if right >= min_w { right } else { -1 }
    }
}
// @lc code=end

