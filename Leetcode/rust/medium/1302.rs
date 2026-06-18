/*
 * @lc app=leetcode id=1302 lang=rust
 *
 * [1302] Deepest Leaves Sum
 */


// @lcpr-template-start
struct Solution;
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}
// @lcpr-template-end
// @lc code=start
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

struct Solution1;

impl Solution1 {
    pub fn deepest_leaves_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let (mut max_depth, mut max_depth_sum) = (0, 0);

        fn dfs(
            node: Option<Rc<RefCell<TreeNode>>>,
            depth: i32,
            max_depth: &mut i32,
            max_depth_sum: &mut i32,
        ) {
            if node.is_none() {
                return;
            }
            let node = node.unwrap();
            let node = node.borrow();
            if depth > *max_depth {
                *max_depth = depth;
                *max_depth_sum = node.val;
            } else if depth == *max_depth {
                *max_depth_sum += node.val;
            }
            if node.left.is_some() {
                dfs(node.left.clone(), depth + 1, max_depth, max_depth_sum);
            }
            if node.right.is_some() {
                dfs(node.right.clone(), depth + 1, max_depth, max_depth_sum);
            }
        }

        dfs(root, 0, &mut max_depth, &mut max_depth_sum);
        max_depth_sum
    }
}

struct Solution2;

impl Solution2 {
    pub fn deepest_leaves_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut q = VecDeque::new();
        if let Some(root) = root {
            q.push_back(root);
        }

        let mut max_depth_sum = 0;
        while !q.is_empty() {
            max_depth_sum = 0;
            for _ in 0..q.len() {
                let node = q.pop_front().unwrap();
                let node = node.borrow();
                max_depth_sum += node.val;
                if node.left.is_some() {
                    q.push_back(node.left.clone().unwrap());
                }
                if node.right.is_some() {
                    q.push_back(node.right.clone().unwrap());
                }
            }
        }
        max_depth_sum
    }
}

impl Solution {
    pub fn deepest_leaves_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        // Solution1::deepest_leaves_sum(root)
        Solution2::deepest_leaves_sum(root)
    }
}

// @lc code=end

