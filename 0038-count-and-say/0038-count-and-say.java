class Solution {
    public String countAndSay(int n) {
        if(n<0)
        {
            return "0";
        }
        if(n==1)
        {
            return "1";
        }
       StringBuilder sb=new StringBuilder("1");
       int tot=1;
       while(tot!=n)
       {
             StringBuilder sb1=new StringBuilder();
             int count=1;
             char curr=sb.charAt(0);
             for(int i=1;i<sb.length();i++)
               {
                  if(sb.charAt(i)==curr)
                    {
                       count++;
                    }
                  else
                    {
                      String s2=Integer.toString(count)+String.valueOf(curr);
                      sb1.append(s2);
                      count=1;
                      curr=sb.charAt(i);
                    }
               } 
            String s2=Integer.toString(count)+String.valueOf(curr);
            sb1.append(s2);
            sb.setLength(0);
            sb.append(sb1.toString());
            tot++;
       }
       return sb.toString();
    }
}