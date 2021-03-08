package com.augustine.problem;

import java.util.HashMap;
import java.util.Map;

/*
Problem: Returns true if this string contains unique characters. (The whitespaces can be ignored)
Using Map<Character, Boolean>.
1. While loop the characters of given string via charAt(int index) method.
2. Put the character form index into map and flip the corresponding boolean value false to true
    Returns null if there was no mapping for given key(character) --> return true if associated key.
3. When null --> contain unique characters.
String#codePointAt(index i) --> returns the Unicode character at the specified index as an int.
 */
public class UniqueChars {
    private static final int MAX_CODE = 65535;

    public static boolean isUnique(String str) {
        Map<Character, Boolean> chars = new HashMap<>();

        for (int i = 0; i < str.length(); i++) {
            if (str.codePointAt(i) <= MAX_CODE) {
                char ch = str.charAt(i);
                if (!Character.isWhitespace(ch)) {
                    if (chars.put(ch, true) != null) {
                        return false;
                    }
                }
            } else {
                System.out.println("The given string contains un-allowed characters");
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String text = "a b c d";
        String unicode = "豈 更 車 賈 滑 更"; // 更 is repeated
        String mixed = "a 豈 b 更 ￦";
        String korean = "사전에 업";
        String nonASCII = "Ξ";

        boolean resultText = isUnique(text);
        System.out.println("resultText: " + resultText);
        boolean resultUnicode = isUnique(unicode);
        System.out.println("resultUnicode: " + resultUnicode);
        boolean resultKorean = isUnique(korean);
        System.out.println("resultKorean: " + resultKorean);
        boolean resultNonASCII = isUnique(nonASCII);
        System.out.println("resultNonASCII: " + resultNonASCII);
        boolean resultMixed = isUnique(mixed);
        System.out.println("resultMixed: " + resultMixed);
    }
}
