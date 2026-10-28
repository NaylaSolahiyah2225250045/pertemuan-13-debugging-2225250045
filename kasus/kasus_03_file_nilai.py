def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)

def tentukan_status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

nilai_mahasiswa = [80, 60, 90, 70]

with open("nilai.txt", "w") as file:
    for nilai in nilai_mahasiswa:
        file.write(str(nilai) + "\n")

with open("nilai.txt", "r") as file:
    data_nilai = [int(baris.strip()) for baris in file]

print("Data nilai:", data_nilai)
print("Rata-rata:", hitung_rata_rata(data_nilai))

for nilai in data_nilai:
    print("Nilai", nilai, ":", tentukan_status(nilai))