package Partial_persistance_Queues;

public class Client {
	// Driver Code
	    public static void main(String[] args) {
	        PersistentQueue<Integer> pq = new PersistentQueue<>();

	        // Perform operations
	        pq.enqueue(10);
	        pq.enqueue(20);
	        pq.enqueue(30);
	        
	        pq.printQueue(1);  // Output: [10]
	        pq.printQueue(2);  // Output: [10, 20]
	        pq.printQueue(3);  // Output: [10, 20, 30]

	        pq.dequeue();  // Remove 10
	        pq.printQueue(4);  // Output: [20, 30]

	        pq.enqueue(40);
	        pq.printQueue(5);  // Output: [20, 30, 40]
	    
	}
}
