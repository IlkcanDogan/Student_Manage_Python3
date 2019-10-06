class Exam():
	score = 0 
	def __init__(self,dogru_sayisi, yanlis_sayisi):
		self.dogru_sayisi = dogru_sayisi
		self.yanlis_sayisi = yanlis_sayisi
		self.score = self.dogru_sayisi * 4 #Her soru 4 puan


	def __int__(self):
		return self.score


class Student():
	ogrenci_adi = None
	not_listesi = []
	avg_score = 0
	def __init__(self,ogrenci_adi):
		self.ogrenci_adi = ogrenci_adi

	def add_exam(self,sinav_notu):
		self.sinav_notu = int(sinav_notu)
		self.not_listesi.append(self.sinav_notu)
		
		self.avg_score += self.sinav_notu
		adet = len(self.not_listesi)
		self.avg_score = self.avg_score / adet

	def __float__(self):
		return float(self.avg_score)

class Class():
	not_listesi = []
	class_avg = 0

	def add_student(self,ogr_not):
		self.ogr_not = int(float(ogr_not))
		self.not_listesi.append(self.ogr_not)

		self.class_avg += self.ogr_not
		adet = len(self.not_listesi)
		self.class_avg = self.class_avg / adet

