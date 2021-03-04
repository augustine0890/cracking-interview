package com.augustine.classical;

public class Ex5 {
    static int sumInteger(String str1, String str2) {
        int num1 = Integer.parseInt(str1);
        int num2 = Integer.parseInt(str2);
        return num1 + num2;
    }

    static void countRepeat(String str, char ch) {
        int count = 0;

        for (int i = 0; i < str.length(); i++) {
           if (str.charAt(i) == ch) {
               count++;
           }
        }
        System.out.println("The '" + ch + "' are occurrences " + count + " time(s).");

    }
    public static void main(String[] args) {
        // Sum of two non-negative integers
        int sumResult = sumInteger("571", "433");
        System.out.println(sumResult);
        // Count occurrences
        String str = "somethingthing";
        countRepeat(str, 't');
    }
}
