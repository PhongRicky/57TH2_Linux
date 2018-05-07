#!/bin/sh
#Chuong trinh hien thi noi dung cua 1 file (ten file la 1 tham so)  
if [ ! –f"$1" ]; then
  echo " $1 not exists"
  exit 1
fi
echo "file sau khi chuyen doi: "
tr ‘[a-z]’ ‘[A-Z]’ <$1
exit 0
