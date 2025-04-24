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
(https://courses.csail.mit.edu/6.851/fall17/scribe/lec1.pdf)

(https://erikdemaine.org/papers/Retroactive_TALG/paper.pdf)

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

- Demonstrates the application of PersistentQueue by performing a sequence of operations.

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

- **Python 3.6** or higher

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

- **getLatestQueue()**
  - Returns the most recent state of the queue after applying all retroactive operations.

### **Requirements**

- **Python 3.6** or above

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
