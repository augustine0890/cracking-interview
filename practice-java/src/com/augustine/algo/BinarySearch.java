package com.augustine.algo;

public class BinarySearch {

    public static int binarySearch(int[] a, int key) {
        int low = 0;
        int high = a.length - 1;

        while (low <= high) {
//            int mid = (low + high) / 2;
            int mid = low + ((high - low) / 2);
            int midVal = a[mid];

            if (midVal < key)
                low = mid + 1;
            else if (midVal > key)
                high = mid - 1;
            else
                return mid; // key found
        }
        return -(low + 1);  // key not found.
    }

    private static int binarySearchRecursive(int[] list, int item, int start, int end) {
        if (end >= start) {
            int mid = start + (end - start) / 2;
            if (list[mid] == item)
                return mid;
            if (list[mid] > item)
                return binarySearchRecursive(list, item, start, mid - 1);
                return binarySearchRecursive(list, item, mid + 1, end);
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] myList = {11, 32, 53, 74, 94, 234, 324};

        System.out.println(binarySearch(myList, 53)); // 1
        System.out.println(binarySearch(myList, 94)); // 4
        System.out.println(binarySearch(myList, 324)); // 6
        System.out.println(binarySearch(myList, 24)); // -2

        int num = myList.length;
        System.out.println(binarySearchRecursive(myList, 74, 0, num));
        System.out.println(binarySearchRecursive(myList, 324, 0, num));
    }
}
