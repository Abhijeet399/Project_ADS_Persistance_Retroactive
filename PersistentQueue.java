package Partial_persistance_Queues;

import java.util.*;

class PersistentQueue<T> {
	private Map<Integer, LinkedList<T>> versions; 
	private int currentVersion;

	public PersistentQueue() {
		this.versions = new HashMap<>();
		this.versions.put(0, new LinkedList<>());
		this.currentVersion = 0;
	}

	private LinkedList<T> getLatestQueue() {
		return new LinkedList<>(versions.get(currentVersion));
	}

	public void enqueue(T value) {
		LinkedList<T> newQueue = getLatestQueue();
		newQueue.add(value);
		currentVersion++;
		versions.put(currentVersion, newQueue);
	}

	public void dequeue() {
		if (versions.get(currentVersion).isEmpty()) {
			System.out.println("Queue is empty.");
			return;
		}
		LinkedList<T> newQueue = getLatestQueue();
		newQueue.removeFirst();
		currentVersion++;
		versions.put(currentVersion, newQueue);
	}

	public void printQueue(int version) {
		if (!versions.containsKey(version)) {
			System.out.println("Version " + version + " does not exist.");
			return;
		}
		System.out.println("Queue (Version " + version + "): " + versions.get(version));
	}

	public int getCurrentVersion() {
		return currentVersion;
	}
}
