import java.io.*;

public class Utopian
{
	public static void main(String[] args) throws IOException
	{
		BufferedReader in =new BufferedReader(new InputStreamReader(System.in));
		BufferedOutputStream out =new BufferedOutputStream(System.out);

		int t=Integer.valueOf(in.readLine());

		int ans[]=new int[t];

		for(int i=0;i<t;++i)
		{
			ans[i]=1;
			int n=Integer.valueOf(in.readLine());
			int j=0;
			while(j<n)
			{
				if(j%2==0)
				{
					ans[i]*=2;
				}
				else
				{
					ans[i]+=1;
				}
				j++;
			}
		}

		for(int i=0;i<t;++i)
		{
			char c[]=Integer.toString(ans[i]).toCharArray();
			for(int j=0;j<c.length;++j)
			{
				out.write(c[j]);
			}
			out.write('\n');
		}
		out.flush();
	}
}
