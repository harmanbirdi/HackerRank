/*
 * Problem: https://www.hackerrank.com/challenges/30-generics
 * Author : Harman Birdi
 */

import java.lang.reflect.Method;

Class Solution {
    // Write your code here - Start
    public static <E> void printArray(E[] array) {
        for (E element : array) {
            System.out.println(element);
        }
    }
    // Write your code here - End

    // Provided by HackerRank template
    public static void main(String args[]){
        Integer[] intArray = { 1, 2, 3 };
        String[] stringArray = { "Hello", "World" };

        printArray( intArray  );
        printArray( stringArray );

        if (Solution.class.getDeclaredMethods().length > 2) {
            System.out.println("You should only have 1 method named printArray.");
        }
    }
}