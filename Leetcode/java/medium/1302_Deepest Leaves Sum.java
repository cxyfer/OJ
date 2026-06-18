/*
 * @lc app=leetcode id=1302 lang=java
 *
 * [1302] Deepest Leaves Sum
 */

// @lcpr-template-start
import java.util.*;

class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
// @lcpr-template-end
// @lc code=start

class Solution1 {

    private int maxDepth = 0;
    private int maxDepthSum = 0;

    public int deepestLeavesSum(TreeNode root) {
        dfs(root, 0);
        return maxDepthSum;
    }

    private void dfs(TreeNode node, int depth) {
        if (depth > maxDepth) {
            maxDepth = depth;
            maxDepthSum = node.val;
        } else if (depth == maxDepth) {
            maxDepthSum += node.val;
        }
        if (node.left != null) {
            dfs(node.left, depth + 1);
        }
        if (node.right != null) {
            dfs(node.right, depth + 1);
        }
    }
}

class Solution2 {

    public int deepestLeavesSum(TreeNode root) {
        int maxDepthSum = 0;
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        while (!q.isEmpty()) {
            maxDepthSum = 0;
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                TreeNode node = q.poll();
                maxDepthSum += node.val;
                if (node.left != null) {
                    q.add(node.left);
                }
                if (node.right != null) {
                    q.add(node.right);
                }
            }
        }
        return maxDepthSum;
    }
}

class Solution extends Solution1 {}
// class Solution extends Solution2 {}
// @lc code=end
