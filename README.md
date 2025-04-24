# **Implementing Persistent and Retroactive Data Structures Using Queues**
Welcome to our git repository for persistent and retroactive queues!
## **Why Did We Undergo This Project?**
Well, traditional queue implementations follow the FIFO (First-In-First-Out) principle and are inherently ephemeral (and it’s also a perfect opportunity to apply the theory we have seen in class).
Once an operation is executed, its effect becomes permanent and there's no way to "look back" or "modify the past".

So in this project we attempted to introduce persistence and retroactivity to queue-based systems specifically (**+** an attempt for persistent stacks).And eventually, we apply them to a banking system where versioning and historical accuracy are critical.
## **Background Information**
### **Persistence**
* **Partial Persistence**: You can **query any previous version of a queue** (e.g., get balances at timestamp t), but you can only **insert new operations at the latest version**.
* **Full Persistence**: You can **query and update any version** of the queue. Allows branching versions.
### **Retroactivity**
* **Partial Retroactivity:** You can insert or delete past operations, but only observe their effect **on the latest state**.
* **Full Retroactivity**: You can insert or delete past operations and also **query any past version** as if history was always that way.

### **Useful Resources**
https://courses.csail.mit.edu/6.851/fall17/scribe/lec1.pdf

https://erikdemaine.org/papers/Retroactive_TALG/paper.pdf

## The Repository’s Structure
Our repo has different folders and files as follows:

Files:
* `PersistentQueue.java` and `Client.java` go together and are under the same package Partial_persistance_Queues 
* `FullPersistenQueue.py`
* `FullRetroactivityNoPersistenceQueue.py`
* `FullRetroactivityQueue.py`
* `ModifiedPersistentRetroactiveQueue.py`
* `ModifiedPersistentRetroactiveQueueMerge.py`
* `ModifiedPersistentRetroactiveQueueVersions.py`
* `PartialPersistenceQueue.py`
* `PartialRetroactivityQueue.py`

Folders:
* Partial_Persistance_Stacks/
* persistent_retroactive_transactions/


## **Persistent Queue in Java**

The persistence is **partial**, meaning you can access and print any previous version, but modifications are only applied to the latest one. Each operation (enqueue/dequeue) increments the version count, maintaining a copy of the queue at that point in time.

**PersistentQueue.java** has the core data structure implementation.

**Client.java** is a sample driver code to demonstrate usage.

### **Features**

**PersistentQueue\<T\>**

This generic class supports the following operations:

- **`enqueue(T value)`**

  - Adds an element to the end of the queue.

  - Creates a new version of the queue.

- **`dequeue()`**

  - Removes the element at the front of the queue.

  - Creates a new version.

  - Handles empty queues.

- **`printQueue(int version)`**

  - Prints the queue content at a specific version.

  - If the version doesn\'t exist, a warning is shown.

- **`getCurrentVersion()`**

  - Returns the latest version number of the queue.

**Client**

- Demonstrates the usage of PersistentQueue by performing a sequence of operations.

- Useful if you want to test and understand the behavior of the persistent queue.

### **Requirements**

- **Java 8 or higher**

- No external libraries or frameworks needed but you can use a Java IDE of your preference.

### **Running the Project**

- **Clone the Repository**

  - `git clone https://github.com/Abhijeet399/Project_ADS_Persistance_Retroactive.git`

- **Compile both Java files**:

  - `javac Partial_persistance_Queues/PersistentQueue.java Partial_persistance_Queues/Client.java`

- **Run the main program**:

  - `java Partial_persistance_Queues.Client`

## **Partial Persistence Queue in Python**
 
 This program is the same as the Java version but in Python for Python lovers. It shows a **partially persistent queue**. In a similar manner, modifications (enqueue and dequeue) can only be made at the **latest version**, but you can access and view any previous version of the queue at any time.
 
 ### **Features**
 
 - **`enqueue(value)`**
 
   - Adds a new value to the end of the queue and creates a new version.
 
 - **`dequeue()`**
 
   - Removes the element from the front of the queue (if not empty) and creates a new version.
 
 - **`getLatestQueue()`**
 
   - Returns the queue at the current (latest) version.
 
 - **`printQueue(version`**
   - Prints the state of the queue at a specified version. If the version doesn't exist, it prints a warning.
 
 ### **Requirements**
 
 - **Python 3.6+**
 
 - Uses only Python standard features, no extra packages required
 
 ### **Running the Program**
 
 - Save the script (via git clone or manual save) and run it directly:
 
     - `python3 PartialPersistenceQueue.py`
 
 ## **Partial Retroactivity Queue**
 
 This program implements a **partially retroactive queue**. It allows inserting enqueue or dequeue operations not only at the end of the operation timeline, but also at **any point in the past**. After each change, the queue is rebuilt to reflect the retroactive effect.
 
 ### **Features**
 
 - **`enqueue(value, t=None)`**
 
   - Inserts the given value into the queue. If t is not provided, it adds the operation at the end of the current timeline.
 
 - **`dequeue(t=None)`**
 
   - Removes the element at the front of the queue. If t is not provided, it dequeues at the end of the current timeline. Otherwise, it applies the dequeue at the specified timestamp.
 
 - **`insert_operation(op_type, value, t)`**
 
   - Helper method to insert either enqueue or dequeue operation into the operations list. Maintains timestamp and order.
 
 - **`build_queue()`**
 
   - Rebuilds the queue from scratch using the sorted list of operations.
 
 - **`getLatestQueue()`**
   - Returns the most recent state of the queue after applying all retroactive operations.
 
 ### **Requirements**
 
 - **Python 3.6+**
 
 - No third-party libraries needed
 
 ### **Running the Program**
 
 - Save the script (via git clone or manual save) and run it directly:
 
   - `python3 PartialRetroactivityQueue.py`
 ## **(Somewhat) Full Persistent Queue in Python**
 
 This implementation is for an almost fully persistent queue, a data structure where every version is immutable and can serve as the base for new versions which can allow us to branch histories and logical timestamp allows multiple versions to coexist. 
 
 Each version is uniquely identified using a UUID and is stored with a logical timestamp, parent version, and the queue's state. 
 
 Note that the UUIDs are dynamically generated, so they'll differ each time you run the code and that the version history can branch at any point.
 
 The file contains the full implementation and usage demo.
 
 - **`enqueue(value, timestamp=None, base_version=None)`**
 
   - Adds an element to the end of the queue.
 
   - Creates a new version ID.
 
   - Supports specifying a custom base version and timestamp, enabling branching.
 
 - **`dequeue(timestamp=None, base_version=None)`**
 
   - Removes the element at the front of the queue.
 
   - Creates a new version ID from a specified base version.
 
   - Also handles empty queues.
 
 - **`print_queue(version_id=None)`**
 
   - Prints the queue contents at a specific version.
 
   - If no version is given, defaults to the latest version.
 
 - **`get_queue_by_version(version_id)`**
 
   - Returns the queue as a list for the given version ID.
 
 - **`get_versions_at_timestamp(timestamp)`**
 
   - Returns a list of all version IDs associated with a given logical timestamp.
 
 ### **Requirements**
 
 - **Python 3.6+**
 
 - Uses built-in uuid and copy functionality. No external libraries are required.
 
 ### **Running the Program**
 
 - **Clone the repo (or save the file)**
 
   - `git clone https://github.com/Abhijeet399/Project_ADS_Persistance_Retroactive.git`
 
 - **Run it**:
   - `python3 FullPersistenceQueue.py`
 ## **Fully Retroactive Queue (No Persistence)**
 
 This implementation demonstrates a **fully retroactive queue** that allows insertion and deletion operations to be performed at **any past timestamp**, with all future versions automatically updated to reflect the change. However, it **doesn’t keep track of old versions of the queue**, meaning each timestamp points to only one version of the queue.
 
 => Retroactive edits can alter the state of the queue at future timestamps and versions are not immutable so the structure reflects only one version per timestamp.
 
 ### **Features**
 
 - **`enqueue(value, timestamp=None)`**
 
   - Adds an element to the queue at a specific timestamp.
 
   - All following timestamps get updated.
 
   - Defaults to appending at the latest version if no timestamp is provided.
 
 - **`dequeue(timestamp=None)`**
 
   - Removes the front element of the queue at the given timestamp.
 
   - Like enqueue, updates all future versions accordingly.
 
 - **`printQueue(timestamp)`**
 
   - Prints the queue contents at the given timestamp.
 
   - Handles nonexistent timestamps.
 
 - **`getQueueAtTimestamp(timestamp)`**
 
   - Retrieves the queue as it was at or before the given timestamp.
 
 ### **Requirements**
 
 - **Python 3.6+**
 
 - Pure Python, no external libraries required.
 
 ### **Running the Program**
 
 - **Clone the repository (or save the file)**
 
   - `git clone https://github.com/Abhijeet399/Project_ADS_Persistance_Retroactive.git`
 
 - **Run it**:
   - `python3 PartialRetroactivityQueue.py`

## **Fully Retroactive Queue (Operation-Based History)**

This Python implementation showcases a **fully retroactive queue** that keeps a complete list of enqueue and dequeue operations along with their timestamps. You can insert or delete any operation at **any point in time**, and reconstruct the queue at any moment based on the sorted history of operations.

The queue maintains a full list of all operations and their timestamps. When a queue needs to be inspected at time t, all operations are sorted and replayed up to that point: first by timestamp, then prioritizing enqueue over dequeue for correct sequencing. Note that no persistence model is used so this is an in-memory operation log.

### **Features**

A fully retroactive queue with full operation logging and rebuild-on-demand behavior.

- **`enqueue(value, timestamp=None)`**

  - Inserts a value at the specified timestamp.

  - Defaults to the next available timestamp if none is given.

- **`dequeue(timestamp=None)`**

  - Removes the front element from the queue at the given timestamp.

  - Like enqueue, defaults to the next timestamp if not specified.

- **`build_queue_at(t)`**

  - Rebuilds the queue up to a specific timestamp using a sorted list of operations.

- **`printQueue(t=None)`**

  - Displays the queue at the provided timestamp (defaults to latest).

- **`printListOfOps()`**

  - Prints a numbered list of all enqueues and dequeues with their timestamps.

### **Requirements**

- **Python 3.6+**

- No third-party dependencies. Runs with the standard library.

### **Running the Program**

- Save the script (via git clone or manual save) and run it directly:

  - `python3 FullRetroactivityQueue.py`

It will output a step-by-step demonstration of how the queue evolves through retroactive operations.

## **Modified Persistent Retroactive Queue**

This is a more complex implementation of a **retroactive queue** using **linked timestamp nodes**, with support for **persistent** tracking of enqueue and dequeue modifications.

Each operation is stored at its respective timestamp node, and all nodes are linked bidirectionally to allow fast traversal and updates in time.

Each timestamp is represented as a Node that contains:

- A list of enqueue operations performed at that time.

- A list of dequeue operations (which remove the front of the queue as seen _before_ that timestamp).

- **Forward and backward pointers** to maintain a temporal linked structure (think of it as a timeline where each moment can influence future or past states).

This approach allows:

- Retroactive edits at any point in time.

- Efficient state rebuilding up to a given timestamp.

- Easy traversal of time through bidirectional links.

However, please note that:

- This is **not purely persistent** in a functional programming sense: it mutates state but maintains temporal fidelity through structure (i.e., state is changing but changes are kept track of ;) )
.

- Bidirectional pointers make it extensible for features like _range queries_, _time intervals_, and _branching versions_.

### **Features**

- **`enqueue(value, timestamp=None)`**

  - Enqueues a value at a specific time. Defaults to the next available version.

- **`dequeue(timestamp=None)`**

  - Records a dequeue operation at the given time, based on the queue state up to that point.

  - Removes the front of the queue if not empty.

- **`get_state_at_timestamp(timestamp)`**

  - Reconstructs the queue as it would exist at a specific timestamp.

- **`print_queue_structure()`**

  - Prints the internal structure, including enqueue/dequeue mods and forward/backward time links.
### **Requirements**

- **Python 3.6+**

### **Running the Program**

- Save the script (via git clone or manual save) and run it directly:

  - `python3 ModifiedPersistentRetroactiveQueue.py`
## **Modified Persistent Retroactive Queue with Version Control**

This program implements a **Modified Persistent Retroactive Queue** with a more detailed and advanced structure. It uses **timestamped nodes** to record operations and build queue state over time. It supports both **persistent** and **retroactive** features, with the ability to trace or reconstruct the queue state at specific **timestamps or versions**.

Similar to the preceding implementation it allows enqueue and dequeue at any specified timestamp and stores nodes with full modification history (enqueue and dequeue mods). We still maintain both **forward and back pointers** between nodes to represent the evolution of the queue and support viewing queue state at any **timestamp** or **version**. We used **deep copy** to maintain version history.

**Features**

- **`_get_or_create_node(timestamp)`**

  - Returns the existing node at timestamp, or creates a new one while maintaining forward/back pointers to adjacent nodes.

- **`enqueue(value, timestamp=None)`**

  - Inserts a value at the specified timestamp. If not provided, the current version timestamp is used.

- **`dequeue(timestamp=None)`**

  - Removes the front element at the specified timestamp. Uses queue state before that time to determine what to remove.

- **`get_state_at_timestamp(timestamp)`**

  - Returns the queue's state after applying all modifications up to the given timestamp.

- **`get_state_at_version(version_number)`**

  - Returns the state of the queue after a specific operation version.

- **`print_queue_structure()`**
  - Debug function to show internal node data, modifications, and pointers for each timestamped node.

### **Requirements**

- **Python 3.6+** 

- Uses the following standard libraries:

  - bisect for efficient sorted insertions

  - collections.deque for fast front-element removals

  - copy for deep-copying node state

### **Running the Program**

- Save the script (via git clone or manual save) and run it directly:

  - `python3 ModifiedPersistentRetroactiveQueueVersions.py`

## **Partial Persistence Stacks (Java)**

This project implements a **partially persistent stack** in Java, allowing users to access past versions of the stack while continuing to make changes in the present. It supports operations like push, pop, and viewing the state of the stack at any previous version. The persistent nature of the stack is managed internally using versioned references.

### **Features**

- **`push(T data)`**

  - Adds an element to the top of the stack and saves the new version.

- **`pop()`**

  - Removes and returns the top element from the stack, creating a new version afterward.

- **`copyStack(Node<T> top)`**

  - Creates a deep copy of the stack starting from the given top node. Used to persist past versions.

- **`makePersistent(T data)`**

  - Creates a new Persistance_Stacks object based on the current stack, pushes the new data, and returns the new stack.

- **`getVersion(int version)`**

  - Returns the top node of the stack at the specified version number.

- **`printStack(Node<T> top)`**
  - Prints the contents of the stack from the given top node down to the bottom.

### **Requirements**

- Java Development Kit (JDK) 8 or higher

### **Running the program**

- `git clone https://github.com/Abhijeet399/Project_ADS_Persistance_Retroactive.git`

- `cd Partial_Persistance_Stacks`

- **Compile the files**:

  - `javac Partial_Persistance_Stacks/\*.java`

- **Run the program**:
  - `java Partial_Persistance_Stacks.Client\$Main`

Note: Client\$Main is required because Main is a nested class inside Client.

## **Persistent Retroactive Banking System**

This is a Django-based web application that simulates a fully retroactive and partially persistent banking system. It allows users to:

- Create accounts with an initial balance

- Perform **deposits**, **withdrawals**, and **transfers**

- Add operations retroactively by specifying a timestamp

- View balances at any past version (timestamp)

- Retroactively **insert** or **rollback** operations by timestamp and type

The backend is powered by a custom **PersistentRetroactiveAccountSystem** class that simulates partial persistence and partial retroactivity in memory.

### **Implementation**

- **Backend Class:** PersistentRetroactiveAccountSystem

- Keeps an operations list of tuples: (timestamp, operation_type, data)

- All operations (create, deposit, withdraw, transfer, rollback) are versioned.

- Balances are recalculated using historical simulation (get_balance()).

- Rollback removes only the specified operation.

### **Web Interface**

- Built using Django

- Views handle GET requests with optional timestamps

- Balances are dynamically computed using versioned history

### **Steps to Import and run the application**

- **Clone the Repository**

  - `git clone https://github.com/Abhijeet399/Project_ADS_Persistance_Retroactive.git`

  - `cd persistent-retroactive-transactions`

- **Installation Instructions**

  - Manually install Django: `pip install Django` (preferably version \>=4)

- **Run the Web Application**

  - _Run Migrations_

    python manage.py migrate

  - _Start the Development Server_

    python manage.py runserver

  - _Access the App_

    Open a browser and go to:

    http://127.0.0.1:8000/

### **Sample Use Case to Try**

- **Create accounts**:

  - Create user1 with a balance of 120 at t0

  - Create user2 with a balance of 520 at t1

- **Deposit to user1**:

  - Deposit 120 to user1 at t2

- **Withdraw from user2**:

  - Withdraw 30 from user2 at t3

- **Transfer**:

  - Transfer 50 from user2 to user1 at t4

- **Retroactive Operation**:

  - Withdraw 50 from user1 at t2 (retroactively)

- **View Balance**:

  - Go to View Balances and enter timestamp 2

You should see:

- `user1: 120 (initial) + 120 (deposit) - 50 (withdraw) = 190`

- `user2: 520 (no change by t2) = 520`

**Rollback a specific operation**:

Enter:

- `Timestamp: 2`

- `Operation: withdraw`

This will undo only the **withdraw operation at t2** without touching future operations.

## **Modified Persistent Retroactive Queue (Experimental Merge Version)**

This  program implements a Modified Persistent Retroactive Queue just like seen previously, supporting advanced retroactive queue operations and version tracking. It allows retroactive enqueue and dequeue operations, as well as viewing the queue's state at any version or timestamp but it also attempts to provide a **merge feature** to combine two historical versions into a new one.

### **Status**

**Remains In Progress -- Merge Functionality Under Development!!!**

### **Features**

- Supports retroactive insertions/removals via timestamped nodes.

- Maintains a versioned history of the queue using deep copies.

- Tracks modifications (enqueue_mods, dequeue_mods) at each timestamped node.

- Allows querying queue state at any version or timestamp.

- Includes a merge function to combine operations from two versions.

### **Example**

```
State at version 8: [25, 20, 35, 30, 40]

State at version 4: [10, 15, 20, 30, 40]

Merged version created at index 9

State at version 9: [30, 30, 40, 40] # Incorrect we've got duplicates & missing elements
```

**Expected Output**

```
Start with [10, 15, 25, 20, 35, 30, 40]
Apply dequeues from version 8 (in order):
Dequeue 1: removes 10
Dequeue 2: removes 15
Final queue after all operations (merged with later dequeue ops):
Final result with deque: [25, 20, 35, 30, 40]

Final queue after all enqueue operations (merged without later dequeue ops):
Final result: [10, 15, 25, 20, 35, 30, 40]
```

### **Issues**

- Incorrectly merged node operations without properly considering their timestamps and sequence

- Failed to properly track which items should be dequeued

- In our merge function, we were trying to use sets to eliminate duplicate pointers, but Node objects can't be properly compared that way.

- After merging two versions, the pointers need to be reconstructed to maintain the correct linked structure.

- When making deep copies, the pointers are referring to the old Node objects, not the newly created ones in the merged version.

### **Requirements**

- **Python 3.6+**

- Uses the following standard libraries:

  - bisect for efficient sorted insertions

  - collections.deque for fast front-element removals

  - copy for deep-copying node state

### **Next Steps / To-Do**

- Perhaps removing the retroactive aspect to simplify the merging of the versions.

- Refactor merge_versions() to:

  - Properly merge operations in correct chronological order.

  - Avoid duplicates and restore queue semantics.

  - Correctly rebuild pointer references across merged nodes.

- Separate mod merging from pointer management for clarity.

- Introduce unit tests to validate correctness of versions and merge output.

## **(Some) Challenges Faced**
**In no particular order we found it difficult to:**
- Updating the pointers  efficiently and correctly
- Keep track of every update without taking space and time
- Shuffle between versions and timestamps
- Adapting Persistence and Retroactive data structures to the use case

## **License**

This project is open-source and provided for educational purposes. You are welcome to participate and collaborate with us to improve this!

(Credits are appreciated ^-^)
