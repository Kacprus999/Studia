package pierwszy;

import java.util.*;

public class sortbystring {
	
	

    public static void main(String[] args) 
    {
        	sortStringArrayByLength_7(args);  
    }
    
 // od Java 8 - wyra�enia lambda  
    private static void sortStringArrayByLength(String[] stringArray) 
    {      
        Arrays.sort(stringArray, Comparator.comparing(String::length).reversed());
        for (String str : stringArray)
        	System.out.println(str + " " + str.length());
    }
    
 // Przed Java 8
    private static void sortStringArrayByLength_7(String[] stringArray) 
    {      
    	Comparator<String> byLength = new Comparator<String>()
    	{
    	      @Override
    	      public int compare(String s1, String s2) 
    	      {
    	        return s2.length() - s1.length();
    	      }
    	};
    	
    	Arrays.sort(stringArray, byLength);
        for (String str : stringArray)
        	System.out.println(str + " " + str.length());
    }
}