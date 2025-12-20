class Solution {
    public String intToRoman(int num) {
        String s1=Integer.toString(num);
        int len=s1.length()-1;
        StringBuilder sb=new StringBuilder();
        for(char c1:s1.toCharArray())
        {
           if(c1=='4' || c1=='9')
           {
              int num1=Character.getNumericValue(c1);
              int val=(int)(num1*Math.pow(10,len));
              if(val>=1000)
              {
                 for(int i=0;i<num1;i++)
                 {
                    sb.append('M');
                 }
              }
              else
              {
                if(val==400)
                {
                   sb.append("CD");
                }
                else if(val==900)
                {
                    sb.append("CM");
                }
                else if(val==90)
                {
                    sb.append("XC");
                }
                else if(val==40)
                {
                    sb.append("XL");
                }
                else if(val==9)
                {
                    sb.append("IX");
                }
                else if(val==4)
                {
                    sb.append("IV");
                }
              }

           }
           else
           {
                int num1=Character.getNumericValue(c1);
                int val=(int)(num1*Math.pow(10,len));
                 if(val>=1000)
                {
                    for(int i=0;i<num1;i++)
                    {
                        sb.append('M');
                    }
                }
                else if(val>=500 && val<900)
                {
                    sb.append('D');
                    num1=num1-5;
                    for(int i=0;i<num1;i++)
                    {
                        sb.append('C');
                    }
                }
                else if(val>=100 && val<400)
                {
                    for(int i=0;i<num1;i++)
                    {
                        sb.append('C');
                    }
                }
                else if(val>=50 && val<90)
                {
                    sb.append('L');
                    num1=num1-5;
                    for(int i=0;i<num1;i++)
                    {
                        sb.append('X');
                    }
                }
                else if(val>=10 && val<40)
                {
                    for(int i=0;i<num1;i++)
                    {
                        sb.append('X');
                    }
                }
                else if(val>=5 && val<9)
                {
                    sb.append('V');
                    num1=num1-5;
                    for(int i=0;i<num1;i++)
                    {
                        sb.append('I');
                    }
                }
                else if(val>=1 && val<4)
                {
                    for(int i=0;i<num1;i++)
                    {
                        sb.append('I');
                    }
                }
           }
           len--;
        }
        return sb.toString();
    }
}