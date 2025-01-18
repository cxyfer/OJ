# @algorithm @lc id=2213 lang=python3 
# @title find-all-people-with-secret


from en.Python3.mod.preImport import *
# @test(6,[[1,2,5],[2,3,8],[1,5,10]],1)=[0,1,2,3,5]
# @test(4,[[3,1,3],[1,2,2],[0,3,3]],3)=[0,1,3]
# @test(5,[[3,4,2],[1,2,1],[2,3,1]],1)=[0,1,2,3,4]
# @test(12, [[10,8,6],[9,5,11],[0,5,18],[4,5,13],[11,6,17],[0,11,10],[10,11,7],[5,8,3],[7,6,16],[3,6,10],[3,11,1],[8,3,2],[5,0,7],[3,8,20],[11,0,20],[8,3,4],[1,9,4],[10,7,11],[8,10,18]], 9)=[0,1,4,5,6,9,11]
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        pa = [i for i in range(n)] # parent

        def find(x: int) -> int:
            if pa[x] != x:
                pa[x] = find(pa[x])
            return pa[x]
        
        def union(x: int, y: int) -> None:
            pa[find(x)] = find(y)

        def isolate(x: int) -> None:
            pa[x] = x

        def isSame(x:int, y:int) -> bool:
            return find(x) == find(y)

        meetings.sort(key=lambda x: x[2]) # sort by time
        union(0, firstPerson) # firstPerson 知道秘密

        time = 0 # 同一時間的會議，需要有人知道秘密才能傳遞
        people = set() # 這個時間點進行會議的人
        for x, y, t in meetings:
            if t != time: # 進入下一個時間點，檢查前一個時間點是否有人知道秘密
                time = t
                for p in people:
                    if not isSame(firstPerson, p):
                        isolate(p)
                people = set()
            union(x, y)
            people.add(x)
            people.add(y)

        ans = []
        for i in range(n):
            if isSame(i, firstPerson):
                ans.append(i)
        return ans
