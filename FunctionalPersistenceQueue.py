class FunctionalPersistenceQueue:
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

    def printQueue(self, version):
        if version not in range(len(self.versions)):
            print(f"Version {version} does not exist.\n")
            return
        print(f"Queue (Version {version}): {self.versions[version]}")

pq = FunctionalPersistenceQueue()
pq.enqueue(10)
pq.enqueue(20)
pq.printQueue(0)
pq.printQueue(1)
pq.printQueue(2)
print(pq.versions)
