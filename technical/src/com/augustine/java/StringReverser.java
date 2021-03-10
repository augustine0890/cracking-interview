package com.augustine.java;

import java.util.Stack;

public class StringReverser {
    public static String reverse(String input) {
        if (input == null) {
            throw new IllegalArgumentException();
        }
        Stack<Character> stack = new Stack<>();
//        for (int i = 0; i < input.length(); i++) {
//            stack.push(input.charAt(i));
//        }

        for (Character ch : input.toCharArray()) {
            stack.push(ch);
        }
        StringBuffer reversed = new StringBuffer();
        while (!stack.empty()) {
            reversed.append(stack.pop());
        }
        return reversed.toString();
    }

    public static void main(String[] args) {
        String str = "abcd";
        String strEmpt = "";
        String strNull = null;

        String result = reverse(str);
        System.out.println(result);
        String result1 = reverse(strEmpt);
        System.out.println(result1);
        String result2 = reverse(strNull);
        System.out.println(result2);
    }
}
