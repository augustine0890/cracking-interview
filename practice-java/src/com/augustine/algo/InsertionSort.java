package com.augustine.algo;

import java.util.Arrays;

public class InsertionSort {
    public static void sort(int[] array){
        int N = array.length;
        for (int i = 0; i < N; i++) {
            int key = array[i];
            int j = i - 1;

            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = key;
        }
    }
    public static void main(String[] args) {
        int[] array = { 2, 4, 5, 1, 9, 7, 2 };
        sort(array);
        System.out.println(Arrays.toString(array));
    }
}
