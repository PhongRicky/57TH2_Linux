#Bai 3
clear 
t= date +%H
if [ $t-ge 1 ] && [ $t-le 11 ]; then 
	echo "Chao buoi sang"
elif [ $t-eq 12 ]; then 
	echo "Chao buoi trua"
elif [ $t-ge 13 ] && [ $t-le 17 ]; then 
	echo "Chao buoi chieu" 
else 
	echo "Chao buoi toi"
fi 
