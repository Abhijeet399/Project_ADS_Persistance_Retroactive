class Node:
    def __init__(self, data):
        self.data = data
        self.back_pointers = []
        self.forward_pointers = []
        self.mods = []
        self.max_mods = 3

class PersistentRetroactiveQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.version = 0

    def enqueue(self, item, timestamp=None):
        if timestamp is None:
            timestamp = self.version

        if not self.head:
            self.head = self.tail = Node(item)
            self.head.back_pointers.append((timestamp, None))
            self.version += 1
            return

        if timestamp < self.version:
            # retroactive enqueue: insert a new node at the right position
            new_node = Node(item)
            current = self.head
            prev = None
            while current:
                for mod_ts, mod_node in current.back_pointers:
                    if mod_ts <= timestamp:
                        prev = mod_node
                        break
                current = prev

            if prev:
                prev.forward_pointers.append((timestamp, new_node))
                new_node.back_pointers.append((timestamp, prev))
            else:
                new_node.forward_pointers.append((timestamp, self.head))
                self.head.back_pointers.append((timestamp, new_node))
                self.head = new_node

            self.version += 1
            return

        # current time enqueue
        if len(self.tail.mods) < self.tail.max_mods:
            self.tail.mods.append(('enqueue', item, timestamp))
        else:
            new_node = Node(item)
            new_node.back_pointers.append((timestamp, self.tail))
            self.tail.forward_pointers.append((timestamp, new_node))
            self.tail = new_node

        self.version += 1

    def dequeue(self, timestamp=None):
        if not self.head:
            return None

        if timestamp is None:
            timestamp = self.version

        item = self.get_node_state_at_timestamp(self.head, timestamp)
        if item is None:
            return None

        if timestamp < self.version:
            self.head.mods.append(('dequeue', None, timestamp))
            self.version += 1
            return item

        next_node = None
        for ts, ptr in self.head.forward_pointers:
            if ts <= timestamp:
                next_node = ptr
                break

        old_head = self.head
        self.head = next_node

        if self.head:
            self.head.mods.append(('dequeue', item, timestamp))

        if not self.head:
            self.tail = None

        self.version += 1
        return item

    def get_node_state_at_timestamp(self, node, timestamp):
        if not node:
            return None
        state = node.data
        for op, mod_data, mod_ts in sorted(node.mods, key=lambda x: x[2]):
            if mod_ts <= timestamp:
                if op == 'enqueue':
                    state = mod_data
                elif op == 'dequeue':
                    return None
        return state

    def get_state_at_timestamp(self, timestamp):
        state = []
        visited = set()
        current = self.head

        while current and id(current) not in visited:
            visited.add(id(current))
            value = self.get_node_state_at_timestamp(current, timestamp)
            if value is not None:
                state.append(value)

            # move to next
            next_node = None
            for ts, ptr in current.forward_pointers:
                if ts <= timestamp:
                    next_node = ptr
                    break
            current = next_node

        return state

    def print_queue_structure(self):
        print("Queue Structure (Version {}):".format(self.version))
        current = self.head
        i = 0
        visited = set()
        while current and id(current) not in visited:
            visited.add(id(current))
            print(f"Node {i}: {current.data}")
            print("  Mods:", current.mods)
            print("  Back pointers:", [(ts, id(ptr) if ptr else None) for ts, ptr in current.back_pointers])
            print("  Forward pointers:", [(ts, id(ptr)) for ts, ptr in current.forward_pointers])
            if current.forward_pointers:
                current = current.forward_pointers[0][1]
            else:
                current = None
            i += 1
        print("End of Queue")
      
queue = PersistentRetroactiveQueue()
queue.enqueue(10)     # t=0
queue.print_queue_structure()
queue.enqueue(20)     # t=1
queue.print_queue_structure()
queue.enqueue(30)     # t=2
queue.print_queue_structure()
queue.enqueue(40)     # t=3
queue.print_queue_structure()
queue.enqueue(15, 0)  # retroactive enqueue at t=0
queue.print_queue_structure()
queue.enqueue(25, 0)  # retroactive enqueue at t=0
queue.print_queue_structure()
queue.dequeue(3)      # retroactive dequeue at t=3
queue.print_queue_structure()
queue.enqueue(35, 1)  # retroactive enqueue at t=1
queue.print_queue_structure()
queue.dequeue(2)      # retroactive deueue at t=2
queue.print_queue_structure()

print("State at t=0:", queue.get_state_at_timestamp(0))
print("State at t=1:", queue.get_state_at_timestamp(1))
print("State at t=2:", queue.get_state_at_timestamp(2))
print("State at t=4:", queue.get_state_at_timestamp(4))

item = queue.dequeue()
print("Dequeued:", item)

queue.enqueue(15, timestamp=1)
print("State after retro insert:", queue.get_state_at_timestamp(queue.version - 1))

ret_item = queue.dequeue(timestamp=1)
print("Retro dequeued:", ret_item)
print("Final state:", queue.get_state_at_timestamp(queue.version - 1))
