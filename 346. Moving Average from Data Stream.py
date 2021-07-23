# my solution
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.total = 0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) <= self.size:
            return self.total/len(self.queue)
        else:
            self.total -= self.queue.popleft()
            return self.total/self.size
          
# nina's solution
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.total = 0
        
    def next(self, val: int) -> float:
        if self.size == len(self.queue):
            tmp = self.queue.popleft()
            self.total-=tmp
        self.queue.append(val)
        self.total+=val
        return self.total/len(self.queue)
