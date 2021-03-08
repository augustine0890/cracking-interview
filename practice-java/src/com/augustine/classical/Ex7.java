package com.augustine.classical;

import java.util.*;

class EntryComparator implements Comparator<Map.Entry<String, Integer>> {

    @Override
    public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
        return o1.getValue().compareTo(o2.getValue());
    }
}

public class Ex7 {
    /*
    HashMap, consider a labyrinth of paths. How can we know which ones we have already traveled down?
    A HashMap could allow us to record these paths and not follow them again.
     */

    public static void ex1() {
        HashMap<String, Integer> hash = new HashMap<>();
        hash.put("dog", 1);
        hash.put("cat", 2);
        hash.put("bird", 3);

        int result = hash.get("cat");
        System.out.println("RESULT: " + result);
    }

    public static void ex2() {
        HashMap<String, Integer> h = new HashMap<>();
        h.put("apple", 1);
        h.put("peach", 2);
        h.put("guava", 3);
        // Get keys
        Set<String> keys = h.keySet();
        for (String key : keys) {
            System.out.println(key);
        }
    }

    public static void ex3() {
        HashMap<String, Integer> values = new HashMap<>();
        values.put("Java", 6);
        values.put("Python", 5);
        values.put("Rust", 7);

        // loop over HashMap with entrySet. The ordering is not maintained.
        for (Map.Entry<String, Integer> pair : values.entrySet()) {
            System.out.println(pair.getKey() + "::" + pair.getValue());
        }
    }

    public static void ex4() {
        HashMap<Integer, Integer> h = new HashMap<>();
        h.put(1, 1000);
        h.put(20, 1001);
        h.put(300, 1003);

        if (h.containsKey(1)) {
            System.out.println("1 was found");
        }
        if (h.containsKey(300)) {
            System.out.println("300 was found");
        }
        if (!h.containsKey(400)) {
            System.out.println("400 was not found");
        }
    }

    public static void ex5() {
        HashMap<String, String> hash = new HashMap<>();
        hash.put("cat", "black");
        hash.put("dog", "brown");
        hash.put("bird", "blue");

        // Get all values from the HashMap
        Collection<String> values = hash.values();
        for (String value : values) {
            System.out.println(value);
        }
    }

    public static void ex6() {
        HashMap<Integer, Integer> hash = new HashMap<>();
        hash.put(10, 10);

        int result = hash.getOrDefault(10, -1);
        int result2 = hash.getOrDefault(1, -1); // does not exist
        System.out.println(result);
        System.out.println(result2);
    }

    public static void ex7() {
        HashMap<String, Double> hash = new HashMap<>();

        hash.putIfAbsent("cat", 1.5);
        hash.putIfAbsent("cat", 2.5);

        double value = hash.get("cat");
        System.out.println(value);
    }

    public static void ex8() {
        HashMap<String, String> hash = new HashMap<>();
        hash.put("red", "color");
        hash.put("tomato", "fruit");
        hash.put("pizza", "lunch");

        // Put keys into an ArrayList and sort it.
        Set<String> set = hash.keySet();
        ArrayList<String> list = new ArrayList<String>();

        list.addAll(set);
        Collections.sort(list);

        for (String key : list) {
            System.out.println(key + ": " + hash.get(key));
        }
    }

    public static void ex9() {
        HashMap<String, Integer> hash = new HashMap<>();
        hash.put("bird", 500);
        hash.put("zebra", 2);
        hash.put("cat", 10);
        hash.put("dog", 5);

        // Copy keySet into ArrayList. Sort with EntryComparator
        ArrayList<Map.Entry<String, Integer>> copy = new ArrayList<>();
        copy.addAll(hash.entrySet());
        copy.sort(new EntryComparator());

        // Display
        for (Map.Entry<String, Integer> e : copy) {
            System.out.println(e.getKey() + "..." + e.getValue());
        }
    }

    static HashMap<String, String> map = new HashMap<>();
    static void addAnimals() {
        map.putIfAbsent("cat", "black");
        map.putIfAbsent("bird", "blue");
    }
    static void testAnimals() {
        System.out.println(map.getOrDefault("cat", "missing"));
        System.out.println(map.getOrDefault("?", "missing"));
    }

    public static void ex10() throws Exception {
        HashMap<Integer, Boolean> hash = new HashMap<>();
        hash.put(100, true);
        hash.put(1000, true);
        hash.put(50, true);

        ArrayList<Integer> array = new ArrayList<>();
        array.add(100);
        array.add(1000);
        array.add(50);

        long t1 = System.currentTimeMillis();

        // Version 1: do HashMap lookups
        for (int i = 0; i < 10000000; i++) {
            if (!hash.containsKey(50)) {
                throw new Exception();
            }
        }
        long t2 = System.currentTimeMillis();

        // Version 2: do ArrayList lookups
        for (int i = 0; i < 10000000; i++) {
            if(!array.contains(50)) {
                throw new Exception();
            }
        }
        long t3 = System.currentTimeMillis();

        // Times
        System.out.printf("HashMap: (containsKey) %d ms\n", t2 - t1);
        System.out.printf("ArrayList: (contains) %d ms", t3 - t2);
    }

    public static void main(String[] args) throws Exception {
        // uses HashMap
        ex1();

        // loops over keys
        ex2();

        // loops over HashMap, entrySet
        ex3();

        // uses containsKey
        ex4();

        // use containsValue
        ex5();

        // getOrDefault
        ex6();

        // uses putIfAbsent
        ex7();

        // sorts HashMap
        ex8();

        // sorts EntrySets
        ex9();

        // uses static HashMap
        // Use static HashMap in static methods
        addAnimals();
        testAnimals();

        // times HashMap, ArrayList
        ex10();
    }
}
