package com.augustine.classical;

import java.util.Scanner;

public class Ex4 {
    static void sumDigit() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input an integer: ");
        long num = scanner.nextLong();

        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        System.out.println("The sum of the digits is: " + sum);
    }

    static void reverseString() {
        Scanner scanner = new Scanner(System.in);
        String string = "";
        System.out.println("Input a string: ");
        string += scanner.nextLine();
        for (int i = string.length() - 1; i >= 0; i--) {
            System.out.print(string.charAt(i));
        }
        System.out.println("\n");
    }

    static void countAll() {
        Scanner scanner = new Scanner(System.in);
        String string = "";
        System.out.println("Input a string: ");
        string += scanner.nextLine();
        char[] ch = string.toCharArray();
        int letter = 0;
        int space = 0;
        int num = 0;
        int other = 0;
        for (int i = 0; i < ch.length; i++) {
            if (Character.isLetter(ch[i])) {
                letter ++;
            } else if (Character.isDigit(ch[i])) {
                num ++;
            } else if (Character.isSpaceChar(ch[i])) {
                space ++;
            } else {
                other ++;
            }
        }

        System.out.print(string);
        System.out.println("\nletter: " + letter);
        System.out.println("space: " + space);
        System.out.println("number: " + num);
        System.out.println("other: " + other);

    }
    public static void main(String[] args) {
        // Sum of the digits
        sumDigit();
        // Reverse string
        reverseString();
        // Count the letters, spaces, numbers
        countAll();
    }
}
