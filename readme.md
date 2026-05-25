# 📚 Data Nilai Siswa

Aplikasi berbasis terminal sederhana untuk mencatat dan mengelola nilai mata pelajaran siswa menggunakan Python.

## 🚀 Fitur

| Menu | Fitur |
|------|-------|
| 1 | **Tambah Data** — Menambahkan nilai mata pelajaran baru |
| 2 | **Tampilkan Semua Data** — Melihat seluruh data nilai yang tersimpan |
| 3 | **Hitung Rata-Rata** — Menghitung rata-rata dari semua nilai |
| 4 | **Total Nilai** — Menampilkan total keseluruhan nilai |
| 5 | **Keluar** — Keluar dari program |

---

## 🛠️ Cara Menjalankan

### Prasyarat
- Python 3.x sudah terinstal di komputer kamu

### Langkah-langkah

1. **Clone atau download** file `main.py` ke komputermu

2. **Jalankan program** lewat terminal:

```bash
python main.py
```

3. **Ikuti instruksi** yang muncul di layar

---

## 📖 Cara Penggunaan

### Menambah Data Nilai
```
Pilih menu di atas (1-5): 1

--- Tambah Data Nilai ---
Masukkan nama mata pelajaran: Matematika
Masukkan nilai untuk Matematika: 90
Nilai Matematika berhasil ditambahkan!
```

### Menampilkan Data
```
Pilih menu di atas (1-5): 2

--- Data Nilai Mata Pelajaran ---
- Matematika: 90
- Bahasa Indonesia: 85
- IPA: 78
```

### Menghitung Rata-Rata
```
Pilih menu di atas (1-5): 3

--- Rata-Rata Nilai ---
Rata-rata dari 3 mata pelajaran adalah: 84.33
```

### Melihat Total Nilai
```
Pilih menu di atas (1-5): 4

--- Total Keseluruhan Nilai ---
Total nilai keseluruhan adalah: 253
```

---

## ✅ Validasi Input

Program dilengkapi dengan beberapa validasi agar data yang dimasukkan selalu benar:

- **Nama mata pelajaran tidak boleh kosong** — jika hanya menekan Enter, program akan memberi peringatan
- **Nama mata pelajaran tidak boleh duplikat** — mata pelajaran yang sama tidak bisa dimasukkan dua kali
- **Nilai harus berupa angka** — jika dimasukkan huruf, program akan meminta input ulang
- **Nilai harus antara 0 sampai 100** — nilai negatif atau di atas 100 tidak akan diterima

---

## 📁 Struktur File

```
project/
└── main.py       # File utama program
└── README.md     # Dokumentasi ini
```

---

## 🧩 Struktur Fungsi

```
main.py
├── display_menu()           # Menampilkan menu utama
├── tanya_kembali()          # Menanyakan apakah user ingin kembali ke menu
├── tambah_data()            # Logika menambah data nilai
├── lihat_data()             # Menampilkan semua data nilai
├── hitung_rata_rata()       # Menghitung dan menampilkan rata-rata
├── total_nilai_keseluruhan() # Menampilkan total keseluruhan nilai
└── main()                   # Fungsi utama & loop menu
```

---

## ⚠️ Catatan

- Data **tidak tersimpan permanen** — jika program ditutup, semua data akan hilang
- Untuk menyimpan data secara permanen, diperlukan integrasi dengan file atau database

---

## 👨‍💻 Dibuat dengan Python

<!-- README MAKE USE AI -->