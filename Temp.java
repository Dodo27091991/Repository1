import java.io.*;

class Temp
{
public static void main(String ar[])
{
System.out.println("Hello java");
String s;
int i=0;
for(i=0;i<=10;i++)
{
System.out.println("This is updated");
Bufferedreader br=new BufferedReader(new InputStreamReader(System.in))
s=br.readLine();
System.out.println(s);
}
}
}