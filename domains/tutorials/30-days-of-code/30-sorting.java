import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        bubbleSort(a, n);
    }

    static void bubbleSort(int a[], int n) {
      int nSwaps = 0;
      for(int i = 0;i < n; i += 1) {
        int numberOfSwaps = 0;
        for(int j = 0;j < n - 1;j += 1) {
          if (a[j] > a[j+1]) {
            int temp = a[j];
            a[j] = a[j + 1];
            a[j + 1] = temp;
            numberOfSwaps+=1;
          }
        }
        if (numberOfSwaps == 0) {
          break;
        }
        nSwaps+=numberOfSwaps;
      }
      System.out.println("Array is sorted in " + nSwaps + " swaps.");
      System.out.println("First Element: " + a[0]);
      System.out.println("Last Element: " + a[n - 1]);
    }
}
