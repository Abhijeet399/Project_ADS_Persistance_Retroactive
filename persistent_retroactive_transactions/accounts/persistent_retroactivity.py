class PersistentRetroactiveAccountSystem:
    def __init__(self):
        self.accounts = {}  # Holds the latest state of accounts
        self.operations = []  # List of all operations: (timestamp, operation_type, data)
        self.max_time = -1

    def _update_max_time(self, timestamp):
        self.max_time = max(self.max_time, timestamp)

    def _sort_operations(self):
        self.operations.sort(key=lambda x: x[0])

    def create_account(self, name, initial_balance, timestamp=None):
        if name in self.accounts:
            return False  # Account already exists

        if timestamp is None:
            timestamp = self.max_time + 1
        self._update_max_time(timestamp)

        self.accounts[name] = initial_balance
        self.operations.append((timestamp, 'create', (name, initial_balance)))
        self._sort_operations()
        return True

    def deposit(self, name, amount, timestamp=None):
        if name not in self.accounts:
            return False

        if timestamp is None:
            timestamp = self.max_time + 1
        self._update_max_time(timestamp)

        self.operations.append((timestamp, 'deposit', (name, amount)))
        self._sort_operations()
        return True

    def withdraw(self, name, amount, timestamp=None):
        if name not in self.accounts:
            return False

        if timestamp is None:
            timestamp = self.max_time + 1
        self._update_max_time(timestamp)

        self.operations.append((timestamp, 'withdraw', (name, amount)))
        self._sort_operations()
        return True

    def transfer(self, sender, receiver, amount, timestamp=None):
        if sender not in self.accounts or receiver not in self.accounts:
            return False

        if timestamp is None:
            timestamp = self.max_time + 1
        self._update_max_time(timestamp)

        self.operations.append((timestamp, 'transfer', (sender, receiver, amount)))
        self._sort_operations()
        return True

    def rollback(self, timestamp, operation_type=None):
        removed = False
        new_operations = []

        for op in self.operations:
            if op[0] == timestamp and (operation_type is None or op[1] == operation_type):
                # Reverse this specific operation
                if op[1] == 'create':
                    self.accounts.pop(op[2][0], None)
                elif op[1] == 'deposit':
                    self.accounts[op[2][0]] -= op[2][1]
                elif op[1] == 'withdraw':
                    self.accounts[op[2][0]] += op[2][1]
                elif op[1] == 'transfer':
                    sender, receiver, amount = op[2]
                    self.accounts[sender] += amount
                    self.accounts[receiver] -= amount
                removed = True
                continue  # Skip adding this operation to the list
            new_operations.append(op)

        if removed:
            self.operations = new_operations
            self.operations.append((self.max_time + 1, 'rollback', (timestamp, operation_type)))
            self.max_time += 1
            return True

        return False  # No matching operation found to rollback


    def get_balance(self, name, timestamp=None):
        if timestamp is None:
            return self.accounts.get(name)

        if timestamp > self.max_time or timestamp < 0:
            return None

        temp_balances = {}
        for t, op, data in sorted(self.operations):
            if t > timestamp:
                break
            if op == 'create':
                n, init = data
                temp_balances[n] = init
            elif op == 'deposit':
                n, amount = data
                if n in temp_balances:
                    temp_balances[n] += amount
            elif op == 'withdraw':
                n, amount = data
                if n in temp_balances:
                    temp_balances[n] -= amount
            elif op == 'transfer':
                s, r, amount = data
                if s in temp_balances and temp_balances[s] >= amount:
                    temp_balances[s] -= amount
                    temp_balances[r] = temp_balances.get(r, 0) + amount
        return temp_balances.get(name)

    def get_all_accounts(self):
        return self.accounts
