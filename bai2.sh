#Bai 2
clear
echo "Nhap ho: "
read h
echo "Nhap ten: "
read t 
str1="Vu Hung Phong" 
if [[ $h && $t ] = $str1 ]; 
then 
	echo "Ten trung khop" 
else 
	echo "Ten khong khop" 
fi 
