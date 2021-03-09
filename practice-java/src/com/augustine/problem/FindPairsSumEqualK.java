package com.augustine.problem;

import java.util.*;

/*
Problem: Array of integers (positive and negative), m. Finds all the pairs of integers whose sum is k
1. HashMap
2. Loop over array: check complement = k - element put to HashMap
    - If complement exists --> return indices.
 */
public class FindPairsSumEqualK {
    public static int[] pairs(int[] m, int k) {
        if (m.length == 0) {
            throw new IllegalArgumentException("The given array is empty");
        }
        Map<Integer, Integer> hash = new HashMap<>();
        for (int i = 0; i < m.length; i++) {
            int complement = k - m[i];
            if (hash.containsKey(complement)) {
                return new int[] {hash.get(complement), i};
            } else {
                hash.put(m[i], i);
            }
        }
        return new int[] {};
    }

    public static HashMap pairsAll(int[] m, int k) {
        if (m.length == 0) {
            throw new IllegalArgumentException("The given array is empty");
        }
        HashMap<Integer, Integer> hash = new HashMap<>();
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < m.length; i++) {
            int complement = k - m[i];
            list.add(complement);
            if (list.contains(m[i])) {
                hash.put(m[i], complement);
            }
        }
        return hash;

    }
    public static void main(String[] args) {
        int[] m1 = {2, 4, 5, 1};
        var result1 = pairs(m1, 6);
        System.out.println(Arrays.toString(result1));

        var resultAll1 = pairsAll(m1, 6);
        System.out.println(Arrays.asList(resultAll1));

        int[] m2 = {2, 7, 11, 15};
        var result2 = pairs(m2, 9);
        System.out.println(Arrays.toString(result2));
    }
}
