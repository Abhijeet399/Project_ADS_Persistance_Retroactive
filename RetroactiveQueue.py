class RetroactiveQueue:
    def __init__(self):
        self.versions = {0: []} 
        self.currentVersion = 0

    def getQueueAtTimestamp(self, timestamp):
        while timestamp not in self.versions and timestamp > 0:
            timestamp -= 1
        return self.versions.get(timestamp, []).copy()

    def updateFutureVersions(self, start_timestamp):
        for t in range(start_timestamp + 1, self.currentVersion + 1): 
                previous_version = self.versions[t-1]
                self.versions[t] = previous_version.copy()
                
    def enqueue(self, value, timestamp=None):
        if timestamp is None:
            timestamp = self.currentVersion

        if timestamp > self.currentVersion:
            print(f"Error: Timestamp {timestamp} does not exist yet.")
            return

        newQueue = self.getQueueAtTimestamp(timestamp)
        newQueue.append(value)
        self.versions[timestamp] = newQueue
        self.updateFutureVersions(timestamp)

        if timestamp == self.currentVersion:
            self.currentVersion += 1

    def dequeue(self, timestamp=None):
        if timestamp is None:
            timestamp = self.currentVersion

        if timestamp > self.currentVersion:
            print(f"Error: Timestamp {timestamp} does not exist yet.")
            return

        newQueue = self.getQueueAtTimestamp(timestamp)
        if not newQueue:
            print(f"Queue is empty at timestamp {timestamp}.")
            return

        newQueue.pop(0)
        self.versions[timestamp] = newQueue
        self.updateFutureVersions(timestamp)

    def printQueue(self, timestamp):
        if timestamp > self.currentVersion:
            print(f"Queue at t={timestamp} does not exist.")
            return
        print(f"Queue (t = {timestamp}): {self.getQueueAtTimestamp(timestamp)}")

rq = RetroactiveQueue()
rq.enqueue(10)    # t=0: [10]
rq.enqueue(20)    # t=1: [10, 20]
rq.enqueue(30)    # t=2: [10, 20, 30]
rq.enqueue(40)    # t=3: [10, 20, 30, 40]

rq.printQueue(0)
rq.printQueue(1)  
rq.printQueue(2) 
rq.printQueue(3)  

rq.enqueue(15, 0)  # insert 15 at t=0: [10, 15]
rq.enqueue(25, 0)  # insert 25 at t=0: [10, 15, 25]
rq.enqueue(35, 1)  # insert 35 at t=1: [10, 15, 25, 35]
rq.dequeue(2)      # dequeue from t=2: [15, 25, 35]

rq.printQueue(0)  # [10, 15, 25]
rq.printQueue(1)  # [10, 15, 25, 35]
rq.printQueue(2)  # [15, 25, 35]
rq.printQueue(3)  # [15, 25, 35]
