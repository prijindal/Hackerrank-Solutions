/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
package HackerRank;


 *
 * @author Priyanshu
 */
import java.util.*;
public class Solution
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int n=input.nextInt();
        int a[] = new int[n];
        for(int i=0;i<n;++i)
        {
            a[i]=input.nextInt();
        }
        int c=n;
        while(c>0)
        {
            int count=0;
            int b[] = new int[n];
            for(int j=0;j<n;++j)
            {
                b[j]=a[j];
            }
            for(int j=0;j<n-1;++j)
            {
                for(int k=0;k<n-1-j;++k)
                {
                    if(b[k]>b[k+1])
                    {
                        int t=b[k];
                        b[k]=b[k+1];
                        b[k+1]=t;
                    }
                }
            }
            int min=b[0];
            for(int j=0;j<n;++j)
            {
                //System.out.println("\t" + b[j]);
                if(b[j]!=0)
                {
                    min=b[j];
                    break;
                }
            }
            //System.out.println("Min : "+ min);
            for(int j=0;j<n;++j)
            {
                //System.out.println(a[j]);
                if(a[j]>=min)
                {
                    a[j]-=min;
                    if(a[j]==0)
                    {
                        c--;
                    }
                    count++;
                }
                else if(a[j]==0)
                {}
                else
                {
                    //System.out.print("ERROR!");
                }
            }
            System.out.println(count);
            //System.out.println("c : \n" + c);
        }

    }
}
