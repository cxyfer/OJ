# @algorithm @lc id=449 lang=python3 
# @title serialize-and-deserialize-bst


from en.Python3.mod.preImport import *
# @test([2,1,3])=[2,1,3]
# @test([])=[]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
        用BFS來encode和decode
    """
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans.append('null')
        while ans and ans[-1] == 'null': # 去掉最後面的null
            ans.pop()
        
        return '/'.join(ans)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        strs = data.split('/')
        root = TreeNode(int(strs[0]))
        queue = deque([root])
        idx = 1
        while idx < len(strs):
            cur = queue.popleft()
            if strs[idx] != 'null':
                cur.left = TreeNode(int(strs[idx]))
                queue.append(cur.left)
            idx += 1
            if idx < len(strs):
                if strs[idx] != 'null':
                    cur.right = TreeNode(int(strs[idx]))
                    queue.append(cur.right)
                idx += 1
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans