from collections import deque

class PersistentQueue:
    def __init__(self, initial_balance):
        self.versions = {0: deque([initial_balance])}  # Queue stores balances
        self.current_version = 0
    
    def _get_latest_queue(self):
        return deque(self.versions[self.current_version])
    
    def deposit(self, amount):
        new_queue = self._get_latest_queue()
        new_balance = new_queue[-1] + amount
        new_queue.append(new_balance)
        self.current_version += 1
        self.versions[self.current_version] = new_queue
    
    def withdraw(self, amount):
        new_queue = self._get_latest_queue()
        if new_queue[-1] < amount:
            print("Insufficient funds.")
            return
        new_balance = new_queue[-1] - amount
        new_queue.append(new_balance)
        self.current_version += 1
        self.versions[self.current_version] = new_queue
    
    def get_balance(self, version=None):
        if version is None:
            version = self.current_version
        if version not in self.versions:
            return None  # or raise an error if preferred
        return self.versions[version][-1]
    
    def get_current_version(self):
        return self.current_version

# Driver Code
if __name__ == "__main__":
    account = PersistentQueue(100)
    
    # Perform operations
    account.deposit(50)  # Version 1
    account.withdraw(30) # Version 2
    account.deposit(20)  # Version 3
    
    # Retrieve balances
    account.get_balance(1)  # Output: Balance at version 1: 150
    account.get_balance(2)  # Output: Balance at version 2: 120
    account.get_balance(3)  # Output: Balance at version 3: 140
    account.get_balance()   # Output: Current Balance: 140
