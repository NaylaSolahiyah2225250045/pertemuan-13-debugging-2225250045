# Pertemuan 13 - Debugging dan Testing
**Nama**:Nayla Solahiyah  
**NIM**: 2225250045  
**Kelas**: 3A

## Kasus
Pada tugas ini, ada tiga program yang diuji. Kasus pertama tentang menentukan kelulusan berdasarkan nilai minimal 60. Kasus kedua tentang menghitung rata-rata dari beberapa data nilai. Kasus ketiga tentang menyimpan dan membaca data nilai menggunakan file.
Pada praktik utama, dilakukan pengujian terhadap fungsi rata-rata, status kelulusan, dan nilai tertinggi untuk menemukan kesalahan pada program dan memperbaikinya.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | Nilai 59 | Tidak lulus | Tidak lulus | PASS |
| T2 | Nilai 60 | Lulus | Tidak lulus | FAIL |
| T3 | Nilai 61 | Lulus | Lulus | PASS |
| T4 | [80, 90, 70] | Rata-rata 80.0 | 48.0 | FAIL |
| T5 | [80, 100] | Rata-rata 90.0 | 36.0 | FAIL |
| T6 | [80, 60, 90, 70] | Rata-rata 75.0 | 60.0 | FAIL |
| T7 | Nilai 60 | Lulus | Tidak lulus | FAIL |
| T8 | [80, 60, 90, 70] | Nilai tertinggi 90 | 0 | FAIL |

## Bug Report
### 1. Kesalahan Menentukan Kelulusan
- **Gejala:** Nilai 60 masih dinyatakan tidak lulus.
- **Lokasi:** Fungsi `status_lulus()` dan `status()`.
- **Penyebab:** Kondisi menggunakan operator `>` sehingga nilai 60 tidak ikut dinyatakan lulus.
- **Perbaikan:** Mengganti operator `>` menjadi `>=` agar nilai 60 juga dinyatakan lulus.
### 2. Kesalahan Menghitung Rata-rata
- **Gejala:** Hasil rata-rata tidak sesuai dengan data yang dimasukkan.
- **Lokasi:** Fungsi `rata_rata()`.
- **Penyebab:** Jumlah nilai selalu dibagi 5, meskipun jumlah datanya berbeda.
- **Perbaikan:** Mengganti angka 5 dengan `len(data)` agar pembagi mengikuti jumlah data. Daftar kosong juga perlu diperiksa agar program tidak mengalami kesalahan.
### 3. Kesalahan Mencari Nilai Tertinggi
- **Gejala:** Hasil nilai tertinggi tidak sesuai dengan data.
- **Lokasi:** Fungsi `nilai_tertinggi()`.
- **Penyebab:** Cara menentukan nilai tertinggi belum menggunakan perbandingan data dengan benar.
- **Perbaikan:** Mengambil nilai pertama sebagai nilai tertinggi awal, kemudian membandingkannya dengan nilai berikutnya. Jika daftar kosong, fungsi mengembalikan `None`.
## Retest
Setelah kode diperbaiki, dilakukan pengujian ulang pada praktik utama.

| Pengujian | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| Rata-rata [80, 60, 90, 70] | 75.0 | 75.0 | PASS |
| Status nilai 60 | Lulus | Lulus | PASS |
| Nilai tertinggi [80, 60, 90, 70] | 90 | 90 | PASS |

Hasil pengujian ulang menunjukkan bahwa ketiga fungsi sudah memberikan hasil yang sesuai dengan harapan untuk data yang diuji.
## Cara Menjalankan
Untuk menjalankan program praktik utama, buka terminal di folder utama proyek, lalu ketik perintah berikut:
```bash
python3 praktik/praktik_4_debugging.py
untuk menjalankan latihan, gunakan perintah:
python3 latihan/01_trace_loop.py
python3 latihan/02_trace_fungsi.py
python3 latihan/03_test_case.py
python3 latihan/04_debug_breakpoint.py

## Refleksi
Menurut saya, breakpoint dan menjalankan program langkah demi langkah sangat membantu untuk menemukan kesalahan. Saya bisa melihat perubahan nilai variabel saat program berjalan. Test case juga membantu memeriksa apakah hasil program sudah benar, terutama saat nilai berada di batas kelulusan atau jumlah datanya berbeda.