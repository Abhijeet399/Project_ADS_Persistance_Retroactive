class FullRetroactivityQueue:
    def __init__(self):
        self.operations = []  # list of (timestamp, op, value)
        self.max_time = -1

    def enqueue(self, value, timestamp=None):
        if timestamp is None:
            timestamp = self.max_time + 1
        self.operations.append((timestamp, 'enqueue', value))
        self.max_time = max(self.max_time, timestamp)

    def dequeue(self, timestamp=None):
        if timestamp is None:
            timestamp = self.max_time + 1
        self.operations.append((timestamp, 'dequeue', None))
        self.max_time = max(self.max_time, timestamp)

    def build_queue_at(self, t):
        ops = sorted(self.operations, key=lambda x: (x[0], 0 if x[1] == 'enqueue' else 1)) # sorting by t then by op (enqueue then dequeue)
        queue = []
        for timestamp, op, value in ops:
            if timestamp > t: 
                break # we're only interested in building the state up to t
            if op == 'enqueue':
                queue.append(value)
            elif op == 'dequeue' and queue:
                queue.pop(0)
        return queue

    def printQueue(self, t =None):
        if t is None:
            t = self.max_time
        print(f"Queue (t = {t}): {self.build_queue_at(t)}")

    def printListOfOps(self):
        op_count = 1
        print("\nList of Updates:")
        for timestamp, op, value in self.operations:
          if op =="enqueue":
            print(f"{op_count}: {op} value = {value} at t = {timestamp}")
          else: print(f"{op_count}: {op} at t = {timestamp}")
          op_count +=1 

prq = FullRetroactivityQueue()
prq.enqueue(10)    # t=0: [10]
prq.enqueue(20)    # t=1: [10, 20]
prq.enqueue(30)    # t=2: [10, 20, 30]
prq.enqueue(40)    # t=3: [10, 20, 30, 40]

print("Before any retroactive changes:")
prq.printQueue(0)
prq.printQueue(1)  
prq.printQueue(2) 
prq.printQueue(3)  
"""
Before any retroactive changes:
Queue (t = 0): [10]
Queue (t = 1): [10, 20]
Queue (t = 2): [10, 20, 30]
Queue (t = 3): [10, 20, 30, 40]
"""
print("\nAfter retroactive insert of 15 at t=0:") 
prq.enqueue(15, 0)  # insert 15 at t=0 
prq.printQueue(0)
prq.printQueue(1)  
prq.printQueue(2) 
prq.printQueue(3)  
"""
After retroactive insert of 15 at t=0:
Queue (t = 0): [10, 15]
Queue (t = 1): [10, 15, 20]
Queue (t = 2): [10, 15, 20, 30]
Queue (t = 3): [10, 15, 20, 30, 40]
"""
print("\nAfter retroactive insert of 25 at t=0:")
prq.enqueue(25, 0)  # insert 25 at t=0
prq.printQueue(0)
prq.printQueue(1)  
prq.printQueue(2) 
prq.printQueue(3)
"""
After retroactive insert of 25 at t=0:
Queue (t = 0): [10, 15, 25]
Queue (t = 1): [10, 15, 25, 20]
Queue (t = 2): [10, 15, 25, 20, 30]
Queue (t = 3): [10, 15, 25, 20, 30, 40]
"""  
print("\nAfter retroactive delete of the first element (10) at t=0:")
prq.dequeue(3)      # retro dequeue (10) from t=3
prq.printQueue(0)
prq.printQueue(1)  
prq.printQueue(2) 
prq.printQueue(3)
"""
After retroactive delete of the first element (10) at t=0:
Queue (t = 0): [10, 15, 25]
Queue (t = 1): [10, 15, 25, 20]
Queue (t = 2): [10, 15, 25, 20, 30]
Queue (t = 3): [15, 25, 20, 30, 40]
"""  
print("\nAfter retroactive insert of 35 at t=1:")
prq.enqueue(35, 1)  # insert 35 at t=1
prq.printQueue(0)
prq.printQueue(1)  
prq.printQueue(2) 
prq.printQueue(3)
"""
After retroactive insert of 35 at t=1:
Queue (t = 0): [10, 15, 25]
Queue (t = 1): [10, 15, 25, 20, 35]
Queue (t = 2): [10, 15, 25, 20, 35, 30]
Queue (t = 3): [15, 25, 20, 35, 30, 40]
"""  
print("\nAfter retroactive delete of the first element (25) at t=2:")
prq.dequeue(2)      # dequeue from t=2
prq.printQueue(0)
prq.printQueue(1)  
prq.printQueue(2) 
prq.printQueue(3)  
"""
After retroactive delete of the first element (25) at t=2:
Queue (t = 0): [10, 15, 25]
Queue (t = 1): [10, 15, 25, 20, 35]
Queue (t = 2): [15, 25, 20, 35, 30]
Queue (t = 3): [25, 20, 35, 30, 40]
"""
prq.printListOfOps()
