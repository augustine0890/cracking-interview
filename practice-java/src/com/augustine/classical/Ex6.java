package com.augustine.classical;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/*
ArrayList, int.
An ArrayList contains many elements. But in Java 8 it cannot store values. It can hold classes (like Integer) but not values (like int).
 */
public class Ex6 {
    public static void ex1() {
        int[] ids = {-3, 0, 200};
        // This does not compile
        // ... Integer must be used, not int.
//        ArrayList<int> test = new ArrayList<>();

        ArrayList<Integer> values = new ArrayList<>();
        for (int id : ids) {
            values.add(id);
        }
        System.out.println(values);
        System.out.println(values.size());
        System.out.println(ids.length);
    }

    public static void ex2() {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(2);
        list.add(5);
        list.add(9);

        for (int value: list) {
            System.out.println("FOR 1: " + value);
        }

        for (int i = 0; i < list.size(); i++) {
            System.out.println("FOR 2: " + list.get(i));
        }
    }

    public static void ex3() {
        ArrayList<Integer> elements = new ArrayList<>();
        elements.add(23);
        elements.add(32);
        elements.add(53);
        System.out.println("Count: " + elements.size());
        elements.clear();
        System.out.println("Count: " + elements.size());
    }

    public static void ex4() {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(100);
        list.add(101);
        list.add(99);
        list.add(100);
        list.add(99);

        int index = list.indexOf(100);
        int lastIndex = list.lastIndexOf(100);
        int notFound = list.indexOf(200);
        System.out.println("INDEX: " + index);
        System.out.println("LASTINDEX: " + lastIndex);
        System.out.println("NOTFOUND: " + notFound);
    }

    public static void ex5() {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(5);
        list.add(10);
        list.add(15);
        list.add(20);
        list.add(25);

        List<Integer> sub = list.subList(1, 3);
        for (int value : sub) {
            System.out.println(value);
        }

        // This is reflected in the original ArrayList
        sub.set(0, -1);
        System.out.println(list.get(1));
    }

    public static void ex6() {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(1);
        list.add(100);
        list.add(5);

        // Mix and max
        int minimum = Collections.min(list);
        int maximum = Collections.max(list);

        System.out.println(minimum);
        System.out.println(maximum);
    }

    public static void ex7() {
        ArrayList<Integer> values = new ArrayList<>();
        Integer[] array = { 10, 20, 30 };

        int[] ids = {-10, 20, -30};
        // This does not compile. ... Integer is not the same as int
//        Collections.addAll(values, ids);

        // Add all elements in array to ArrayList
        Collections.addAll(values, array);
        for (int value : values) {
            System.out.print(value);
            System.out.print(" ");
        }
        System.out.println();

        Collections.addAll(values, 40, 50);
        for (int value : values) {
            System.out.print(value);
            System.out.print(" ");
        }
        System.out.println();
    }

    public static void ex8() {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(7);
        list.add(8);
        list.add(9);

        Integer[] array = {};
        array = list.toArray(array);

        for (int elem : array) {
            System.out.println(elem);
        }
    }
    public static void main(String[] args) {
        // Example 1
        ex1();

        // Loops over ArrayList
        ex2();

        // Clear array
        ex3();

        // indexOf, lastIndexOf
        ex4();

        // subList
        ex5();

        // Collections.min, max
        ex6();

        // Collections.addAll
        ex7();

        // toArray
        ex8();
    }
}
