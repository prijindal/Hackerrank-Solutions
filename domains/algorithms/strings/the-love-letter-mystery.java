import java.io.*;

public class LetMys
{
	public static void main(String[] args) throws IOException
	{
		BufferedReader in =new BufferedReader(new InputStreamReader(System.in));
		BufferedOutputStream out =new BufferedOutputStream(System.out);

		int t=Integer.valueOf(in.readLine());

		int ans[]=new int[t];

		for(int i=0;i<t;++i)
		{
			ans[i]=0;
			char s[]=in.readLine().toCharArray();

			int l=s.length;
			for(int j=0;j<=(l/2);++j)
			{
				if(s[j]>s[l-j-1])
				{
					ans[i]+=s[j]-s[l-j-1];
					s[j]=s[l-j-1];

				}
				else if(s[j]<s[l-j-1])
				{
					ans[i]+=s[l-j-1]-s[j];
					s[l-j-1]=s[j];
				}
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
