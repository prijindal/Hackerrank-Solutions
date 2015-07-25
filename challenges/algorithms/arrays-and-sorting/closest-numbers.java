import java.io.*;

public class Closest
{
	static int arr[];
	static int helper[];
	public static void main(String[] args) throws IOException
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedOutputStream out = new BufferedOutputStream(System.out);

		int n=Integer.valueOf(in.readLine());

		String s[]=in.readLine().split(" ");

		arr=new int[n];
		for(int i=0;i<n;++i)
		{
			arr[i]=Integer.valueOf(s[i]);
		}
		helper=new int[n];
		merge_sort(0,n-1);

		int min=arr[1]-arr[0];
		for(int i=1;i<n-1;++i)
		{
			if((arr[i+1]-arr[i])<min)
			{
				min=arr[i+1]-arr[i];
			}
		}

		for(int i=1;i<n;++i)
		{
			if(min==arr[i]-arr[i-1])
			{
				char c[]=Integer.toString(arr[i-1]).toCharArray();
				for(int j=0;j<c.length;++j)
				{
					out.write(c[j]);
				}
				out.write(' ');
				char d[]=Integer.toString(arr[i]).toCharArray();
				for(int j=0;j<d.length;++j)
				{
					out.write(d[j]);
				}
				out.write(' ');
			}
		}
		out.flush();
	}

	static void merge_sort(int low,int high)
	{
		if(low<high)
		{
			int mid=(low+high)/2;

			merge_sort(low,mid);
			merge_sort(mid+1,high);

			for(int i=low;i<=high;++i)
			{
				helper[i]=arr[i];
			}

			int i=low;
			int j=mid+1;
			int k=low;

			while((i<=mid)&&(j<=high))
			{
				if(helper[i]<helper[j])
				{
					arr[k]=helper[i];
					i++;
				}
				else
				{
					arr[k]=helper[j];
					j++;
				}
				k++;
			}

			while(i<=mid)
			{
				arr[k]=helper[i];
				i++;
				k++;
			}

			while(j<=high)
			{
				arr[k]=helper[j];
				j++;
				k++;
			}
		}
	}
}
			
