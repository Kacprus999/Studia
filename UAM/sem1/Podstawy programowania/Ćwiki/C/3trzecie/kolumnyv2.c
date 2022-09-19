#include <stdio.h>
#include <stdlib.h>

int main()
{

   int a=1;
   while (a<37)
   {
       printf("%4d ",a);
       if(a%6==0)
            putchar('\n');
        a++;

   }
   return 0;
}

