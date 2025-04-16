class Node: # each t is rep by a node
    def __init__(self, timestamp): 
        self.timestamp = timestamp
        self.enqueue_mods = [] # stores (value,timestamp) for insertions
        self.dequeue_mods = [] # stores (value,timestamp) for delete update
        self.forward_pointers = [] # (timestamp,next_node) 
        self.back_pointers = [] # (timestamp,prev_node)

    """
    1.if the node for this timestamp already exists, we return it. else, we create a new node.
    2.look for the position to insert t => can use bisect (locate the insertion point for arg2 in arg1 to maintain sorted order)
    3.I need to insert the timestamp into a sorted list to keep the order => use insort 
    4.if I am not inserting at 0 (first position/head), I need to check the previous timestamp
    5.using that I go the previous node with that timestamp
    6.update back pointers for my new node to point that previous node
    7.update that previous node's forward pointers
    8.if I am not at the tail, I need to do the exact same for the next as i did previously
    9.update fwd pts this time aorund for new node and back ptrs for next node
    """


from bisect import bisect_left, insort
from collections import deque

class ModifiedPersistentRetroactiveQueue:
    def __init__(self):
        self.nodes = {}  # maps timestamp to Node
        self.timestamps = []  # keeps timestamps in sorted order
        self.version = 0

    def _get_or_create_node(self, timestamp):
      if timestamp in self.nodes:
          return  self.nodes[timestamp]
      new_node = Node(timestamp) 
      self.nodes[timestamp] = new_node
      index = bisect_left(self.timestamps, timestamp)
      insort(self.timestamps, timestamp)
      if index > 0:
          prev_ts = self.timestamps[index - 1]
          prev_node = self.nodes[prev_ts]
          new_node.back_pointers.append((prev_ts, prev_node))
          prev_node.forward_pointers.append((timestamp, new_node))

      if index + 1 < len(self.timestamps):
          next_ts = self.timestamps[index + 1]
          next_node = self.nodes[next_ts]
          new_node.forward_pointers.append((next_ts, next_node))
          next_node.back_pointers.append((timestamp, new_node))

      return new_node


    def enqueue(self, value, timestamp=None):
        if timestamp is None:
            timestamp = self.version
        node = self._get_or_create_node(timestamp)
        insort(node.enqueue_mods, (value, timestamp))
        self.version += 1

    def dequeue(self, timestamp=None):
        if timestamp is None:
            timestamp = self.version
        node = self._get_or_create_node(timestamp)
        queue_before = self.get_state_at_timestamp(timestamp)
        if queue_before:
            removed = queue_before[0]
            insort(node.dequeue_mods, (removed, timestamp))
            self.version += 1
            return removed
        return None

    def get_state_at_timestamp(self, timestamp):
        result = deque()
        for ts in self.timestamps:
            if ts > timestamp:
                break
            node = self.nodes[ts]
            for val, _ in node.enqueue_mods:
                result.append(val)
            for _, _ in node.dequeue_mods:
                if result:
                    result.popleft() #popleft is faster than pop(0) with O(1) vs O(n)
        return result

    def print_queue_structure(self):
        print(f"Queue Structure (Version {self.version}):")
        for i, ts in enumerate(sorted(self.timestamps)):
            node = self.nodes[ts]
            print(f"Node {i} (t={ts}):")
            print(f"  Enqueue Mods: {node.enqueue_mods}")
            print(f"  Dequeue Mods: {node.dequeue_mods}")
            print(f"  Back Pointers: {[(t, id(n)) for t, n in node.back_pointers]}")
            print(f"  Forward Pointers: {[(t, id(n)) for t, n in node.forward_pointers]}")
        print("End of Queue\n")
q = ModifiedPersistentRetroactiveQueue()
q.enqueue(10, 0)
q.enqueue(20, 1)
q.enqueue(30, 2)
q.enqueue(40, 3)
q.enqueue(15, 0)
q.enqueue(25, 0)
q.dequeue(3)
q.enqueue(35, 1)
q.dequeue(2)
q.print_queue_structure()
print("Final state:", q.get_state_at_timestamp(q.version))
