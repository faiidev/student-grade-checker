print("========================")
print("STUDENT GRADE CHECKER V2")
print("========================")

nama = input("Masukkan Nama  : ")
nilai = int(input("Masukkan Nilai : "))

if nilai >= 0 and nilai <= 100:

    # Menentukan Grade
    if nilai >= 90:
        grade = "A"
    elif nilai >= 80:
        grade = "B"
    elif nilai >= 70:
        grade = "C"
    elif nilai >= 60:
        grade = "D"
    else:
        grade = "E"

    # Menentukan Status
    if nilai >= 75:
        status = "LULUS"
    else:
        status = "TIDAK LULUS"

    # Menampilkan Hasil
    print("========================")
    print("Nama     :", nama)
    print("Nilai    :", nilai)
    print("Grade    :", grade)
    print("Status   :", status)
    print("========================")

else:
    print("Nilai tidak valid. Masukkan nilai antara 0 sampai 100.")