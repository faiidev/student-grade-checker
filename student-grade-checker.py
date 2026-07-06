print("========================")
print("STUDENT GRADE CHECKER")
print("========================")

nama = input("Masukkan Nama  : ")
nilai = int(input("Masukkan Nilai : "))

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

if nilai >= 75:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print("========================")
print("Nama     : ", nama)
print("Nilai    : ", nilai)
print("Grade    : ", grade)
print("Status   : ", status)
print("========================")