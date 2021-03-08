package com.augustine.problem;

import java.util.ArrayList;
import java.util.List;

public class SherlockArray {
    /**
     1. Calculate the sum of all elements of array and store it as sum
     2. Loop through all elements of array. Check for every element
        if (2*x == sum - y) is true
            return YES
        Add current element y to the x and go to step 2
     3. return NO
     **/
    static String balancedSums(List<Integer> arr) {
        int sum = 0;
        int total = 0;
        for (int a: arr) {
            total += a;
        }

        for (int ele: arr) {
            if (2*sum == total - ele) {
                return "YES";
            }
            sum = sum + ele;
        }
        return "NO";
    }

    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(2);
        list.add(3);
        list.add(7);
        list.add(4);
        list.add(1);
        System.out.println(balancedSums(list));
    }
}
