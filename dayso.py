#!/usr/bin/python
n= input('Nhap so nguyen n= ')
for i in range(1,n+1):
	print i
S=0
for i in range(1,n+1):
	if(i%2==0):
		S=S+i
print 'Tong cac so chan S= %d'%(S)
