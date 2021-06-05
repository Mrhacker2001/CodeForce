#include <stdio.h>
 
int main(){
    int n,k,temp=0,i;
    scanf("%d %d",&n,&k);
  //  printf("%d %d",n,k);
    int a[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        if(a[i]>=a[k-1] && a[i]!=0)
        {
            temp=temp+1;
        }
    }
    printf("%d",temp);
    return 0;
}

