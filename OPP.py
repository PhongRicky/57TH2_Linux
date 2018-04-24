#!/usr/bin/python
class SinhVien:
	def __init__(self,maSV,hoTen,maKhoa):
		self.maSV = maSV
		self.hoTen = hoTen
		self.maKhoa = maKhoa

	def printSV(self):
		print self.maSV, '\t', self.hoTen, '\t', self.maKhoa

	def get_maKhoa(seft):
		return seft.maKhoa

class Khoa:
	def __init__(self,maKhoa,tenKhoa):
		self.maKhoa = maKhoa
		self.tenKhoa = tenKhoa

	def printKhoa(self):
		print self.maKhoa, '\t', self.tenKhoa
	

sv=[]
sv.append(SinhVien('001','Mai A','01'))
sv.append(SinhVien('002','Tran B','01'))
sv.append(SinhVien('003','Van C','02'))
sv.append(SinhVien('004','Thi K','01'))
print 'MSSV\tHo ten\tMa khoa'
for i in sv:
	i.printSV()

k=[]
k.append(Khoa('01','CNTT'))
k.append(Khoa('02','KToan'))
k.append(Khoa('03','Co Khi'))
k.append(Khoa('04','Nuoi'))
print'------------------------'
print 'Ma khoa\tTen khoa'
for j in k:
	j.printKhoa()

print'------------------------'
print 'SV thuoc khoa CNTT'
print 'MSSV\tHo ten\tMa khoa'
for h in sv:
	if(h.get_maKhoa()=='01'):
		h.printSV()
