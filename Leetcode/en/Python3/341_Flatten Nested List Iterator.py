# @algorithm @lc id=341 lang=python3 
# @title flatten-nested-list-iterator

from en.Python3.mod.preImport import *
class NestedInteger:
   ...
# @test([[1,1],2,[1,1]])=[1,1,2,1,1]
# @test([1,[4,[6]]])=[1,4,6]
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque()
        self.dfs(nestedList)
    
    def next(self) -> int:
        return self.queue.popleft()
        
    def hasNext(self) -> bool:
        return len(self.queue) > 0

    def dfs(self, nestedList):
        for nest in nestedList:
            if nest.isInteger():
                self.queue.append(nest.getInteger())
            else:
                self.dfs(nest.getList())