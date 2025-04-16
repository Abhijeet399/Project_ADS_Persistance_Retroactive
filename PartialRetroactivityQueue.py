class PartialRetroactivityQueue:
    def __init__(self):
        self.operations = []  # (timestamp, insertion_order, op_type, value)
        self.queue = []
        self.op_counter = 0   # helps break ties when timestamps are equal

    def enqueue(self, value, t=None):
        self.insert_operation("enqueue", value, t)

    def dequeue(self, t=None):
        self.insert_operation("dequeue", None, t)

    def insert_operation(self, op_type, value, t):
        if t is None:
            t = len(self.operations)
        self.operations.append((t, self.op_counter, op_type, value))
        self.op_counter += 1
        self.operations.sort()  # sort by timestamp and insertion_order
        self.build_queue()

    def build_queue(self):
        self.queue = []
        for _, _, op, val in self.operations:
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
prq.enqueue(15, 0)  # insert 15 at t=0 => [10, 15, 20, 30, 40]
prq.enqueue(25, 0)  # insert 25 at t=0 => [10, 15, 25, 20, 30, 40]
prq.dequeue(3)      # dequeue from t=3 => [15, 25, 20, 30, 40]
prq.enqueue(35, 1)  # insert 35 at t=1 => [15, 25, 20, 35, 30, 40]
prq.dequeue(2)      # dequeue from t=2 => [25, 20, 35, 30, 40]
prq.getLatestQueue()
