package com.augustine;

public class Starter {

    static void greet() {
        System.out.println("Hello, World!");
    }

    static void java() {
        System.out.println("\nJava Version: " + System.getProperty("java.version"));
        System.out.println("Java Runtime Version: " + System.getProperty("java.runtime.version"));
        System.out.println("Java Home: " + System.getProperty("java.version"));
        System.out.println("Java Class Path: " + System.getProperty("java.class.path") + "\n");
    }
    static int addIntegers(int a, int b) {
        return(a + b);
    }

    static long addIntegers(int... intArray) {
        if (intArray.length == 0) return (0);
        long total = 0;
        for (int i = 0; i < intArray.length; i++) {
            total =+ intArray[i];
        }
        return (total);
    }

    public static void main(String[] args) {
        greet();

        // Check Java Env
        java();

        // Functions
        int result = addIntegers(3, 4);
        System.out.println(result);

        long result1, result2, result3, result4 = 0;
        result1 = addIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9);
        System.out.println(result1);
        result2 = addIntegers(22, 43, 12, 53);
        System.out.println(result2);
        result3 = addIntegers(23, 35);
        System.out.println(result3);

        int[] intArray1 = {1, 3, 5, 7, 9};
        result4 = addIntegers(intArray1);
        System.out.println(result4);
    }
}
