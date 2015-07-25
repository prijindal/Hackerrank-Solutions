import java.io.*;

public class Insert_Sort
{
	public static void main(String[] args) throws IOException
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		//BufferedOutputStream out = new BufferedOutputStream(System.out);

		int n=Integer.parseInt(in.readLine());

		String A[] = in.readLine().split(" ");
		int a[]=new int[n];
		for(int i=0;i<n;++i)
		{
			a[i]=Integer.parseInt(A[i]);
		}
		int value=a[n-1];
		int i=n-1;
		while((value<=a[i])&&(i>0))
		{
			a[i]=a[i-1];
			i--;
			if(a[i]>value)
			{
				for(int j=0;j<n;++j)
				{
					System.out.print(a[j]+" ");
				}
				System.out.println();
			}
		}
		if(a[i]<value)
		{
			a[i+1]=value;
		}
		else
		{
			a[i]=value;
		}
		for(int j=0;j<n;++j)
			{
				System.out.print(a[j]+" ");
			}
			System.out.println();
	}
}


			
