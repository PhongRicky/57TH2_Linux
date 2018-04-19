#!/usr/bin/python
class SinhVien:
	def __init__(self,maSV,hoTen,maKhoa):
		self.maSV = maSV
		self.hoTen = hoTen
		self.maKhoa = maKhoa
	def printSV(self):
		print self.maSV, '\t', self.hoTen, '\t', self.maKhoa

class Khoa:
	def __init__(self,maKhoa,tenKhoa):
		self.maKhoa = maKhoa
		self.tenKhoa = tenKhoa
	def printKhoa(self):
		print self.maKhoa, '\t', self.tenKhoa


sv1= SinhVien('001','Mai A','01')
sv2= SinhVien('002','Tran B','01')
sv3= SinhVien('003','Van C','02')
sv4= SinhVien('004','Thi K','001') 

k1= Khoa('01','CNTT')
k2= Khoa('02','KToan')
k3= Khoa('03','Co Khi')
k4= Khoa('04','Nuoi')

print 'MSSV\tHo ten\tMa khoa'
sv1.printSV()
sv2.printSV()
sv3.printSV()
sv4.printSV()
print'------------------------'
print 'Ma khoa\tTen khoa'
k1.printKhoa()
k2.printKhoa()
k3.printKhoa()
k4.printKhoa()

