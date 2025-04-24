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

  - git clone [[https://github.com/Abhijeet399/Project_ADS_Persistance_Retroactive.git]](https://github.com/Abhijeet399/Project_ADS_Persistance_Retroactive.git)

- **Compile both Java files**:

  - `javac Partial_persistance_Queues/PersistentQueue.java Partial_persistance_Queues/Client.java`

- **Run the main program**:

  - `java Partial_persistance_Queues.Client`
