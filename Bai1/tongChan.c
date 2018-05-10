#include<stdio.h>
int tongChan(int n)
{
	int S=0;
	for(int i=1; i<=n; i++)
	{
		if(i%2==0)
			S+=i;
	}
	return S;
}
