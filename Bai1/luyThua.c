#include<stdio.h>

int luythua(int x, int n)
{	int S=1;
	for(int i=1; i<=n; i++)
	{
		S*=x;
	}
	return S;
}
