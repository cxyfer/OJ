#
# @lc app=leetcode id=2408 lang=python3
#
# [2408] Design SQL
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.tbls = {name: OrderedDict() for name in names}
        self.curIdx = {name: 1 for name in names}
        self.colSize = {name: column for name, column in zip(names, columns)}

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tbls or len(row) != self.colSize[name]:
            return False
        self.tbls[name][self.curIdx[name]] = row
        self.curIdx[name] += 1
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name in self.tbls and rowId in self.tbls[name]:
            del self.tbls[name][rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name in self.tbls and rowId in self.tbls[name] and 1 <= columnId <= self.colSize[name]:
            return self.tbls[name][rowId][columnId - 1]
        return "<null>"

    def exp(self, name: str) -> List[str]:
        if name not in self.tbls:
            return []
        return [",".join([str(rid)] + row) for rid, row in self.tbls[name].items()]
# @lc code=end