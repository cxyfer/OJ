# @algorithm @lc id=71 lang=python3 
# @title simplify-path


from en.Python3.mod.preImport import *
# @test("/home/")="/home"
# @test("/home//foo/")="/home/foo"
# @test("/home/user/Documents/../Pictures")="/home/user/Pictures"
# @test("/../")="/"
# @test("/.../a/../b/c/../d/./")="/.../b/d"
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