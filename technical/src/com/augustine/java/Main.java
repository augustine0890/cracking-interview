package com.augustine.java;

public class Main {

    public static void main(String[] args) {
        // double to int
        double doubleNum = 19.93;
        System.out.println("The double value: " + doubleNum);
        int intNum = (int) doubleNum;
        System.out.println("The int value: " + intNum);

        // int to double
        int intNum2 = 34;
        System.out.println("The int value2: " + intNum2);
        double doubleNum2 = intNum2;
        System.out.println("The double value2: " + doubleNum2);

        // String to int
        String s = "32";
        System.out.println("The string value: " + s);
        int intStr = Integer.parseInt(s);
        System.out.println("The int from string value: " + intStr);

        // int to String
        int intNum3 = 45;
        System.out.println("The int value3: " + intNum3);
        String sInt = String.valueOf(intNum3);
        System.out.println("The String value: " + sInt);
    }
}
