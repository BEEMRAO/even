#include<stdio.h>
int main()
{
  int factorial=1;
  int x,i;
    scanf("%d",&x);
  if(x<=20)
  {
    for(i=1;i<=x;i++)
  {
    factorial=factorial*i;
  }
  print("%d",factorial);
  }
  }
