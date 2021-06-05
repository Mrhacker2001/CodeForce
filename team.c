#include <stdio.h>
 
int main(){
    int n,i,count=0,increase=0,temp=0;
    scanf("%d",&n);
    int a[n*3];
    for(i=0;i<n*3;i++)
    {
        scanf("%d",&a[i]);
    }
    
    for(i=0;i<n*3;i++)
    {   
        temp=temp+a[i];
        count=1+count;
        if(count==3)
            {
            count=0;
            if(temp>=2)
                increase=1+increase;
            temp=0;
            }
    }
    printf("%d",increase);
    return 0;
}

