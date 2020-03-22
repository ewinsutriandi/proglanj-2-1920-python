def hitung_nilai_akhir(nilai_hadir,nilai_tugas,nilai_uts,nilai_uas):
    bobot_hadir = 0.15
    bobot_tugas = 0.25
    bobot_uts = 0.3
    bobot_uas = 0.3    
    nilai_akhir = bobot_hadir * nilai_hadir + bobot_tugas * nilai_tugas + bobot_uts * nilai_uts + bobot_uas * nilai_uas
    return nilai_akhir

def nilai_ke_grade(nilai_akhir):
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

nama_mhs = ["Rina","Agus","Surti"]
nilai_mhs = [[90, 95, 80, 80],[80, 75, 30, 70],[100, 75, 60, 65]];

for i in range(len(nama_mhs)):
    nama = nama_mhs[i]
    nilai = nilai_mhs[i]
    nilai_akhir = hitung_nilai_akhir(nilai[0],nilai[1],nilai[2],nilai[3])
    grade = nilai_ke_grade(nilai_akhir)
    print('{} mendapatkan nilai akhir = {}, grade= {}'.format(nama,nilai_akhir,grade))
