package com.augustine.classical;

import java.util.Scanner;

public class Ex3 {
    static void swap(int x, int y) {
        int temp = x;
        x = y;
        y = temp;
        System.out.printf("x: %d, y: %d\n", x, y);
    }

    static void dec2bin() {
        int dec_num, quot, i = 1, j;
        int bin_num[] = new int[20];
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input a Decimal Number: ");
        dec_num = scanner.nextInt();

        quot = dec_num;

        while (quot != 0) {
            bin_num[i++] = quot%2;
            quot = quot/2;
        }

        System.out.println("Binary number is: ");
        for (j=i-1; j>0; j--) {
            System.out.print(bin_num[j]);
        }
        System.out.println("\n");
    }

    static void dec2hex() {
        int dec_num, rem;
        String hexdec_num = "";

        char hex[] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input a Decimal Number: ");
        dec_num = scanner.nextInt();

        while (dec_num > 0) {
            rem = dec_num%16;
            hexdec_num = hex[rem] + hexdec_num;
            dec_num = dec_num/16;
        }
        System.out.println("Hexadecimal number is: " + hexdec_num + "\n");
    }

    public static void main(String[] args) {
        swap(12, 32);
        // Decimal to binary
        dec2bin();
        // Decimal to hexadecimal
        dec2hex();
    }
}
