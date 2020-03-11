'''
Refresh materi semester 1
Cara menghitung nilai akhir dan gradenya
'''
bobot_hadir = 0.15
bobot_tugas = 0.25
bobot_uts = 0.3
bobot_uas = 0.3

nilai_hadir = 100
nilai_tugas = 82
nilai_uts = 60
nilai_uas = 55

nilai_akhir = bobot_hadir * nilai_hadir + bobot_tugas * nilai_tugas + bobot_uts * nilai_uts + bobot_uas * nilai_uas

grade = 'E'
if nilai_akhir >= 85:
    grade = 'A'
elif nilai_akhir >= 70:
    grade = 'B'
elif nilai_akhir >= 50:
    grade = 'C'
elif nilai_akhir >= 40:
    grade = 'D'

print('Nilai akhir= {}, grade= {}'.format(nilai_akhir,grade))