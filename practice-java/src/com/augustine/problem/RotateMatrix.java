package com.augustine.problem;

import java.util.Arrays;

/*
Problem: m x n matrix of integers --> rotate the matrix by 90 degrees in a counterclockwise direction (No extra space)
- Transpose matrix: Mij == Mji
- Reversing the column (flip vertically)
 */
public class RotateMatrix {
    private static void transpose(int[][] matrix) {
        int N = matrix.length;
//        int M = matrix[0].length;
        for (int i = 0; i < N; i++) {
            for (int j = i; j < N; j++) {
                int temp = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = temp;
            }
        }
    }

    public static void rotateMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0) {
            throw new IllegalArgumentException("The given matrix cannot be null or empty");
        }

        if (matrix.length != matrix[0].length) {
            throw new IllegalArgumentException("The given matrix must be of type nxn");
        }
        // Transposing
        transpose(matrix);

        int N = matrix.length;
        // Flip vertically (Rotated 90 degrees in counterclockwise)
//        for (int i = 0; i < N/2; i++) {
//            for (int j = 0; j < N; j++) {
//                int temp = matrix[i][j];
//                matrix[i][j] = matrix[N - 1 - i][j];
//                matrix[N - 1 - i][j] = temp;
//            }
//        }

        // Flip horizontally (Rotated 90 degrees in clockwise)
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N/2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][N - 1 - j];
                matrix[i][N - 1 - j] = temp;
            }
        }
    }

    public static void main(String[] args) {
        int[][] m1 = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}};

//        transpose(m1);
        rotateMatrix(m1);
        int s = m1.length;
        for (int i = 0; i < s; i++) {
            for (int j = 0; j < s; j++) {
                System.out.format("%4s", m1[i][j]);
            }
            System.out.println();
        }
    }
}
