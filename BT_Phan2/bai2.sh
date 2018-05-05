clear 
echo "Nhap so nguyen a= " 
read a 
echo "Nhap so nguyen b= "
read b 

let "tong= $a+$b"
echo "Tong: $a + $b = $tong" 

let "hieu= $a-$b"
echo "Hieu: $a - $b = $hieu"

let "tich= $a*$b"
echo "Tich: $a * $b = $tich"

if test $b -eq 0; then
echo "So bi chia phai khac 0" 
else
let "thuong= $a/$b"
echo "Thuong: $a / $b = $thuong"

let "du= $a%$b"
echo "Chia lay du: $a % $b = $du"
fi 
