package com.augustine.problem;

import java.util.HashMap;

/*
Problem: Returns true if the string contains unique characters. Only consider a string from a-z. Ignored whitespaces
- Characters from a-z: ASCII codes from 97(a) to 122(z)
- Loops through the string --> put to HashMap
- If HashMap return null --> contains unique --> otherwise not contains

BitMap:
- Find the int value of the character with respect to 'a'
- The bit at that int value is set to 1
- If this bit is already set in the checker --> bit AND operation would make checker > 0 --> return false
- Update the checker
 */
public class UniqueCharsAZ {
    private static final int aASCII = 97;
    private static final int zASCII = 122;

    public static boolean checkUnique(String str) {
        if (str == null || str.isBlank()) {
            throw new IllegalArgumentException("Cannot be empty string or null");
        }
        HashMap<Character, Boolean> hash = new HashMap<>();
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (!Character.isWhitespace(ch)) {
                int code = str.codePointAt(i);
                if (code >= aASCII && code <= zASCII) {
                    if (hash.put(ch, true) != null) {
                        return false;
                    }
                } else {
                    System.out.println("The given string not in range of a-z");
                    return false;
                }
            }
        }
        return true;
    }

    private static final char A_CHAR = 'a';
    public static boolean checkUniqueBitMap(String str) {
        if (str == null || str.isBlank()) {
            throw new IllegalArgumentException("Cannot be empty string or null");
        }

        int checker = 0;
        for (int i = 0; i < str.length(); i++) {
            int bitAtIndex = str.charAt(i) - A_CHAR;
            int mask = 1 << bitAtIndex;

            if ((checker & mask) > 0) {
                return false;
            }
            checker = checker | mask;
        }
        return true;
    }

    public static void main(String[] args) {
        String text1 = "abcdefhzqoc";
        String text2 = "abcd efhz qow";

        boolean resultText1 = checkUnique(text1);
        boolean resultText2 = checkUnique(text2);
        System.out.println("Text1 has unique characters? " + resultText1);
        System.out.println("Text2 has unique characters? " + resultText2);

        boolean resultBitMapText1 = checkUniqueBitMap(text1);
        boolean resultBitMapText2 = checkUniqueBitMap(text2);
        System.out.println("(BitMap) Text1 has unique characters? " + resultBitMapText1);
        System.out.println("(BitMap) Text2 has unique characters? " + resultBitMapText2);
    }
}
