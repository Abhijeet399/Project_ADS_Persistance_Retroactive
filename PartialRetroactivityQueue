class PartialRetroactivityQueue:
    def __init__(self):
        self.operations = []
        self.queue = []

    def enqueue(self, value, t=None):
        self.insert_operation("enqueue", value, t)

    def dequeue(self, t=None):
        self.insert_operation("dequeue", None, t)

    def insert_operation(self, op_type, value, t):
        if t is None:
            t = len(self.operations)
        self.operations.insert(t, (op_type, value))
        self.build_queue()

    def build_queue(self):
        self.queue = []
        for op, val in self.operations:
            if op == "enqueue":
                self.queue.append(val)
            elif op == "dequeue" and self.queue:
                self.queue.pop(0)

    def getLatestQueue(self):
        return self.queue 

prq = PartialRetroactivityQueue()
prq.enqueue(10)    # t=0: [10]
prq.enqueue(20)    # t=1: [10, 20]
prq.enqueue(30)    # t=2: [10, 20, 30]
prq.enqueue(40)    # t=3: [10, 20, 30, 40]
prq.enqueue(15, 0)  # insert 15 at t=0 => [15, 10, 20, 30, 40]
prq.enqueue(25, 0)  # insert 25 at t=0 => [25, 15, 10, 20, 30, 40]
prq.dequeue(3)      # dequeue from t=3 => [15, 10, 20, 30, 40]
prq.enqueue(35, 1)  # insert 35 at t=1 => [35, 15, 10, 20, 30, 40]
prq.dequeue(2)      # dequeue from t=2 => [15, 10, 20, 30, 40]
prq.getLatestQueue()
