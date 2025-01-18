#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    """
        Stack
    """
    def simplifyPath(self, path: str) -> str:
        names = path.split('/')
        st = []
        for name in names:
            if name == '..':
                if st: st.pop()
            elif name and name != ".":
                st.append(name)
        return '/' + '/'.join(st)
# @lc code=end
sol = Solution()
print(sol.simplifyPath("/home/")) # "/home"
print(sol.simplifyPath("/home//foo/")) # "/home/foo"
print(sol.simplifyPath("/home/user/Documents/../Pictures")) # "/home/user/Pictures"
print(sol.simplifyPath("/../")) # "/"
print(sol.simplifyPath("/.../a/../b/c/../d/./")) # "/.../b/d"
