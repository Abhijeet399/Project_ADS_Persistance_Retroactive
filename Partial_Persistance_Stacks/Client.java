package Partial_Persistance_Stacks;

public class Client {

public class Main {
    public static void main(String[] args) {
    	Persistance_Stacks<Integer> stack1 = new Persistance_Stacks<>();
        stack1.push(50);
        stack1.push(40);
        stack1.push(30);
        stack1.push(20);
        stack1.push(10);

        Persistance_Stacks<Integer> stack2 = stack1.makePersistent(5);

        System.out.print("Stack1: ");
        stack1.printStack(stack1.top);

        System.out.print("Stack2: ");
        stack2.printStack(stack2.top);

        Integer popped = stack1.pop();
        System.out.println("Popped from Stack1: " + popped);

        System.out.print("Stack1 after pop: ");
        stack1.printStack(stack1.top);

        System.out.print("Stack1 at version 3: ");
        stack1.printStack(stack1.getVersion(3));
    }
}

}
