package com.augustine.linds;

public class Main {
    public static void main(String[] args) {
        // Linked List
        LinkedList seasons = new LinkedList();
        seasons.printList();
        seasons.addToHead("summer");
        seasons.addToHead("spring");
        seasons.printList();

        seasons.addToTail("fall");
        seasons.addToTail("winter");
        seasons.printList();

        seasons.removeHead();
        seasons.printList();
    }
}
