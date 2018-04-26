#Bai 4
clear

echo "--------------------------------------"
echo "---------Cac phep toan so hoc---------"
echo "--------------------------------------"
echo "Cong (+)"
echo "Tru (-)"
echo "Nhan (*)"
echo "Chia (/)"
echo "Ket thuc (q)"
echo "--------------------------------------"

read -p "Ban chon phep tinh nao?: " chon
read -p "Nhap vao 2 so nguyen"
read -p "a= " a
read -p "b= " b
case $chon in
"+") 
	let "tong=$a+$b"
	echo "$a + $b = " $tong;;
"-")
	let "hieu=$a-$b"
	echo "$a - $b = " $hieu;;
"*")
	let "tich=$a*$b"
	echo "$a * $b = " $tich;;
"/")
	let "thuong=$a/$b"
	echo "$a / $b = " $thuong;;
"q")
	echo "Ket thuc"
	exit;;
esac 
