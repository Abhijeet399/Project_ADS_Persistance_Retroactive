import uuid

class FullPersistenceQueue:
    def __init__(self):
        self.versions = {}
        initial_id = str(uuid.uuid4())
        self.versions[initial_id] = (0, None, []) 
        self.current_version = initial_id
        self.version_counter = 1
        self.version_map_by_timestamp = {0: [initial_id]}

    def get_queue_by_version(self, version_id):
        return self.versions[version_id][2]

    def enqueue(self, value, timestamp=None, base_version=None):
        if base_version is None:
            base_version = self.current_version

        base_ts, _, base_queue = self.versions[base_version]

        if timestamp is None:
            timestamp = base_ts + 1

        new_queue = base_queue.copy()
        new_queue.append(value)

        new_version_id = str(uuid.uuid4())
        self.versions[new_version_id] = (timestamp, base_version, new_queue)
        self.current_version = new_version_id

        if timestamp not in self.version_map_by_timestamp:
            self.version_map_by_timestamp[timestamp] = []
        self.version_map_by_timestamp[timestamp].append(new_version_id)

        return new_version_id

    def dequeue(self, timestamp=None, base_version=None):
        if base_version is None:
            base_version = self.current_version

        base_ts, _, base_queue = self.versions[base_version]

        if timestamp is None:
            timestamp = base_ts + 1

        new_queue = base_queue.copy()
        if not new_queue:
            print(f"Queue is empty at timestamp {timestamp}.")
            return None

        new_queue.pop(0)

        new_version_id = str(uuid.uuid4())
        self.versions[new_version_id] = (timestamp, base_version, new_queue)
        self.current_version = new_version_id

        if timestamp not in self.version_map_by_timestamp:
            self.version_map_by_timestamp[timestamp] = []
        self.version_map_by_timestamp[timestamp].append(new_version_id)

        return new_version_id

    def print_queue(self, version_id=None):
        if version_id is None:
            version_id = self.current_version

        timestamp, parent, queue = self.versions[version_id]
        print(f"Queue at version {version_id} (t = {timestamp}): {queue}")

    def get_versions_at_timestamp(self, timestamp):
        return self.version_map_by_timestamp.get(timestamp, [])

rq = FullPersistenceQueue()

v1 = rq.enqueue(10)   # t=1
v2 = rq.enqueue(20)   # t=2
v3 = rq.enqueue(30)   # t=3
v4 = rq.enqueue(40)   # t=4

# branch from t=1 (which is v1)
branch1 = rq.enqueue(15, 1, base_version=v1)
branch2 = rq.enqueue(25, 1, base_version=branch1)
branch3 = rq.enqueue(35, 2, base_version=branch2)
branch4 = rq.dequeue(3, base_version=branch3)

rq.print_queue(branch4)  # should show [15, 25, 35] with first element(30) removed
print(rq.version_map_by_timestamp)
