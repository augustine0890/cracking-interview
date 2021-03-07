package com.augustine.java;

import java.util.Dictionary;
import java.util.Hashtable;

public class DictionaryCreation {
    public static void main(String[] args) {
        Dictionary<Integer, String> dict = new Hashtable<>();
        // add key-value pairs to dict
        dict.put(1, "hello");
        dict.put(7, "goodbye");
        // access the values using the keys
        System.out.println("Value at key 1: " + dict.get(1));
        System.out.println("Value at key 7: " + dict.get(7));
    }
}
