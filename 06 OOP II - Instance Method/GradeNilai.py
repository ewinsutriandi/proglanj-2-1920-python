class NilaiMataKuliah:
    def __init__(self, nama, mata_kuliah, nilai_hadir,nilai_tugas,nilai_uts,nilai_uas):
        self.nama = nama
        self.mata_kuliah = mata_kuliah
        self.nilai_hadir = nilai_hadir
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
    
    def hitung_nilai_akhir(self):
        bobot_hadir = 0.15
        bobot_tugas = 0.25
        bobot_uts = 0.3
        bobot_uas = 0.3    
        nilai_akhir = bobot_hadir * self.nilai_hadir + bobot_tugas * self.nilai_tugas + bobot_uts * self.nilai_uts + bobot_uas * self.nilai_uas
        return nilai_akhir    

    def grade_nilai(self):
        nilai_akhir = self.hitung_nilai_akhir()
        grade = 'E'
        if nilai_akhir >= 85:
            grade = 'A'
        elif nilai_akhir >= 70:
            grade = 'B'
        elif nilai_akhir >= 50:
            grade = 'C'
        elif nilai_akhir >= 40:
            grade = 'D'
        return grade
    
obj = NilaiMataKuliah("Agus","Pemrograman Lanjut",80,75,85,70)
nilai_akhir = obj.hitung_nilai_akhir()
grade = obj.grade_nilai()

print('{} pada mata kuliah {} mendapatkan nilai akhir = {}, grade= {}'.format(obj.nama,obj.mata_kuliah,nilai_akhir,grade))
