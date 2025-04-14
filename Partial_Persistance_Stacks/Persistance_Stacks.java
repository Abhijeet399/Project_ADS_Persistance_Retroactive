package Partial_Persistance_Stacks;

import java.util.*;

class Node<T> {
    public T data; 
    public Node<T> next;

    public Node(T item) {
        data = item;
        next = null;
    }
}

class Persistance_Stacks<T> {
    public Node<T> top;
    private Map<Integer, Node<T>> versionTops; 
    private int currentVersion;

    public Persistance_Stacks() {
        top = null;
        versionTops = new HashMap<>();
        currentVersion = 0;
        versionTops.put(currentVersion, null); 
    }

    public void push(T data) {
        Node<T> newNode = new Node<>(data);
        newNode.next = top;
        top = newNode;
        currentVersion++;
        versionTops.put(currentVersion, copyStack(top));
    }

    public T pop() {
        if (top == null)
            return null;
        T data = top.data;
        top = top.next;
        currentVersion++;
        versionTops.put(currentVersion, copyStack(top));
        return data;
    }

    public Node<T> copyStack(Node<T> top) {
        if (top == null)
            return null;
        Node<T> newNode = new Node<>(top.data);
        newNode.next = copyStack(top.next);
        return newNode;
    }

    public Persistance_Stacks<T> makePersistent(T data) {
    	Persistance_Stacks<T> newStack = new Persistance_Stacks<>();
        newStack.top = copyStack(top);
        newStack.currentVersion = currentVersion;
        
        for (int v = 0; v <= currentVersion; v++) {
            newStack.versionTops.put(v, copyStack(versionTops.get(v)));
        }
        
        newStack.push(data);
        
        return newStack;
    }

    public Node<T> getVersion(int version) {
        if (version < 0 || version > currentVersion) {
            return null; // Invalid version
        }
        return versionTops.get(version);
    }

    public void printStack(Node<T> top) {
        if (top == null) {
            System.out.println("Empty stack");
            return;
        }
        Node<T> current = top;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
}
