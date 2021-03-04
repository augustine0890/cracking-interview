package com.augustine.classical;
import java.util.Scanner;

public class Ex2 {
    static double average(double...doubleArray) {
        double total = 0;
        if (doubleArray.length == 0) return 0;
        for (int i = 0; i < doubleArray.length; i++) {
            total += doubleArray[i];
        }
        return total/(double) doubleArray.length;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input a number: ");
        int num = scanner.nextInt();
        for (int i = 1; i <= 10; i++) {
            System.out.printf("%d x %d = %d\n", num, i, num*i);
        }

        double avg = average(23.32, 24.4, 54.7);
        System.out.printf("Average: %f%n", avg);
    }
}
