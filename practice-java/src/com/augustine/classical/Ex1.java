package com.augustine.classical;

import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input first number: ");
        int first = scanner.nextInt();
        System.out.println("Input second number: ");
        int second = scanner.nextInt();

        System.out.printf("%d + %d = %d\n", first, second, first + second);

        if (first > second) {
            System.out.printf("%d - %d = %d\n", first, second, first - second);
        } else {
            System.out.printf("%d - %d = %d\n", second, first, second - first);
        }

        System.out.printf("%d x %d = %d\n", first, second, first * second);
        System.out.printf("%d / %d = %d\n", first, second, first / second);
        System.out.printf("%d mode %d = %d\n", first, second, first % second);

    }
}
