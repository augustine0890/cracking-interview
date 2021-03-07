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

        // DoublyLinkedList
        DoublyLinkedList subway = new DoublyLinkedList();
        subway.addToHead("Times Square");
        subway.addToHead("Grand Central");
        subway.addToHead("Central Park");
        subway.printList();

        subway.addToTail("Penn Station");
        subway.addToTail("Wall Street");
        subway.addToTail("Brooklyn Bridge");
        subway.printList();

        subway.removeHead();
        subway.removeTail();
        subway.printList();

        subway.removeByData("Times Square");
        subway.printList();
    }
}
