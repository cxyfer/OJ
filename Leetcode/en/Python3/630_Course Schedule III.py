# @algorithm @lc id=630 lang=python3 
# @title course-schedule-iii


from en.Python3.mod.preImport import *
# @test([[100,200],[200,1300],[1000,1250],[2000,3200]])=3
# @test([[1,2]])=1
# @test([[3,2],[4,3]])=0
class Solution:
    """
        Greedy: Early Deadline First (EDF)
        Heap-regret Greedy (反悔貪心)

        heapq實作的是min heap，所以加負號變成max heap
        - heapreplace(): 從 heap 取出並回傳最小的元素，接著將新的 item 放進heap。heap 的大小不會改變。
    """
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1]) # 按照Deadline由小到大排序
        h = [] # Heap
        day = 0 # 已使用天數
        for duration, last_day in courses:
            if day + duration <= last_day: # 沒有超過 last_day，可以上這門課程
                day += duration
                heappush(h, -duration) # 因為heapq實作的是min heap，所以加負號變成max heap
            elif h and duration < -h[0]: # 這門課程的時間比之前的最長時間要短
                # 反悔
                # 取出最長時間的課程，改為上新的這門課程
                day -= -heapreplace(h, -duration)
                day += duration
        return len(h)