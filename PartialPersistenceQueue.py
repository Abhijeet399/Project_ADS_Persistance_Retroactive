class PartialPersistenceQueue:
    def __init__(self):
        self.versions = [[]] 
        self.currentVersion = 0

    def getLatestQueue(self):
        return self.versions[self.currentVersion]

    def enqueue(self, value):
        newQueue = self.getLatestQueue().copy()  
        newQueue.append(value)
        self.currentVersion += 1
        self.versions.append(newQueue)

    def dequeue(self):
        if not self.versions[self.currentVersion]:
            print("Queue is empty.\n")
            return
        newQueue = self.getLatestQueue().copy()
        newQueue.pop(0)
        self.currentVersion += 1
        self.versions.append(newQueue)

    def printQueue(self, version):
        if version not in range(len(self.versions)):
            print(f"Version {version} does not exist.\n")
            return
        print(f"Queue (Version {version}): {self.versions[version]}")
        
pq = PatialPersistenceQueue()
pq.enqueue(10)
pq.enqueue(20)
pq.dequeue()
pq.printQueue(0)
pq.printQueue(1)
pq.printQueue(2)
pq.printQueue(3) 
print(pq.versions)
