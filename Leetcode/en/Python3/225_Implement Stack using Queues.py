# @algorithm @lc id=225 lang=python3 
# @title implement-stack-using-queues
from collections import deque

class MyStack1:
    """
    # 1. 使用兩個queue，在push時調整
    # 使得queue1維持stack的性質，queue2用來暫存queue1的元素
    # 時間複雜度：push(): O(n)、pop(): O(1)、top(): O(1)、empty(): O(1)
    """
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        """
        因為queue1要保持stack的性質，所以要把queue1的元素都移到queue2
        那麼queue2的元素就會維持stack的性質，最後再把兩者交換，讓queue1維持stack的性質
        """
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """
        在某些語言中的pop()可能不能處理size為0的情況，考試時要注意
        """
        return self.queue1.popleft() if self.queue1 else None

    def top(self) -> int:
        """
        Python的deque沒有top()，直接取[0]就好，另外和pop()相同，在某些語言中的top()可能不能處理size為0的情況，考試時要注意
        """
        return self.queue1[0] if self.queue1 else None

    def empty(self) -> bool:
        return not self.queue1
    
class MyStack2:
    """
    # 2. 使用兩個queue，在pop時調整
    # 使queue1維持queue的性質，queue2用來暫存queue1的元素
    # pop時對queue1做n-1次pop出來後push到queue2，然後再做1次pop把最後一個元素pop出來
    # 有些題解的方法是直接取back()，但是這樣就不是queue了，不符合題目要求
    # 時間複雜度：push(): O(1)、pop(): O(n)、top(): O(n)、empty(): O(1)
    """
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if not self.queue1:
            return None
        size = len(self.queue1)
        while size > 1:
            self.queue2.append(self.queue1.popleft())
            size -= 1
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.popleft()

    def top(self) -> int:
        """
        這裡可以用上述的pop()方法把top的元素pop出來，再把它push回去就好了
        """
        if not self.queue1:
            return None
        top = self.pop()
        self.push(top)
        return top

    def empty(self) -> bool:
        return not self.queue1

class MyStack3:
    """
    # 3. 使用一個queue
    # 和方法2.類似，但是不用兩個queue，而是用一個queue
    # 使queue1維持queue的性質，但不用暫存queue1的元素，直接push回queue1即可
    # pop時對queue1做n-1次pop和push，然後再做1次pop把最後一個元素pop出來
    # 時間複雜度：push(): O(1)、pop(): O(n)、top(): O(n)、empty(): O(1)
    """
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.queue:
            return None
        size = len(self.queue)
        while size > 1:
            self.queue.append(self.queue.popleft())
            size -= 1
        return self.queue.popleft()

    def top(self) -> int:
        """
        這裡可以用上述的pop()方法把top的元素pop出來，再把它push回去就好了
        """
        if not self.queue:
            return None
        top = self.pop()
        self.push(top)
        return top

    def empty(self) -> bool:
        return not self.queue

# class MyStack(MyStack1):
# class MyStack(MyStack2): 
class MyStack(MyStack3):
    pass