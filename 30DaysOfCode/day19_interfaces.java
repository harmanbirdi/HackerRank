/*
 * Problem: https://www.hackerrank.com/challenges/30-interfaces
 * Author : Harman Birdi
 */

import java.io.*;
import java.util.*;

// Interface for divisorSum that returns the sum of all divisors
// for a given integer
interface AdvancedArithmetic{
   int divisorSum(int n);
}

// Write your code here
class Calculator implements AdvancedArithmetic {

    @Override
    public int divisorSum(int n) {
        int sum = 0;

        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                sum += i;
            }
        }

        return sum;
    }
}


// Provided by HackerRank template
//class Solution {
class day19_interfaces {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();

      	AdvancedArithmetic myCalculator = new Calculator();
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}
