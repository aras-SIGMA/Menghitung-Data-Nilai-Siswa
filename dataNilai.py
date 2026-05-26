aras_nilai = []

def display_menu():
    print("\n*=== DATA NILAI SISWA ===*")
    print("1. Tambah Data")
    print("2. Tampilkan Semua Data")
    print("3. Hitung Rata-Rata")
    print("4. Total Nilai")
    print("5. Keluar")

def tanya_kembali():
    kembali = input("\nKembali ke menu utama? (y/n): ").lower()
    if kembali != 'y':
        print("Terimakasih telah menggunakan layanan kami.")
        return False
    return True
# selesai melakukan satu tugas maka user akan diatanyai, apakah ingin mengunakan aplikasi lagi?

def tambah_data():
    print("\n--- Tambah Data Nilai ---")

    mapel = input("Masukkan nama mata pelajaran: ").strip()
    if not mapel:
        print("Nama mata pelajaran tidak boleh kosong.")
        return

# cara untuk membuat data list yang isinya semua mapel yang sudah di input user 
    mapel_sudah_ada = [m.lower() for m, n in aras_nilai] 
    if mapel.lower() in mapel_sudah_ada:
        print(f"Mata pelajaran '{mapel}' sudah ada!")
        return

    while True:
        try:
            nilai = float(input(f"Masukkan nilai untuk {mapel}: "))
            if 0 <= nilai <= 100:
                aras_nilai.append([mapel, nilai])
                print(f"Nilai {mapel} berhasil ditambahkan!")
                break 
            else:
                print("Nilai tidak valid. Silakan coba lagi.")

        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

def lihat_data():
    print("\n--- Data Nilai Mata Pelajaran ---")
    
    if not aras_nilai:
        print("Tidak ada data.")
        return
    
    for mapel, nilai in aras_nilai:
        print(f"- {mapel}: {nilai:g}")
        # pakai f biar bisa langsung menyelipkan variabel di dalam string 

def hitung_rata_rata():
    print("\n--- Rata-Rata Nilai ---")
    if not aras_nilai:
        print("Tidak ada data untuk dihitung.")
        return
    
    total = sum(nilai for mapel, nilai in aras_nilai)
    rata_rata = total / len(aras_nilai)
    print(f"Rata-rata dari {len(aras_nilai)} mata pelajaran adalah: {rata_rata:.2f}")
    # :.2f berguna untuk mmebuat batasan ppada angka desimal, jadi mereka hanya punya 2 angka di belakang koma

def total_nilai_keseluruhan():
    print("\n--- Total Keseluruhan Nilai ---")
    if not aras_nilai:
        print("Tidak ada data untuk dihitung.")
        return

    total = sum(nilai for mapel, nilai in aras_nilai)
    print(f"Total nilai keseluruhan adalah: {total:g}")


def main():
    while True:
        display_menu()
        choice = input("Pilih menu di atas (1-5): ")

        if choice == '1':
            tambah_data()
            if not tanya_kembali(): 
                break
                
        elif choice == '2':
            lihat_data()
            if not tanya_kembali():
                break
                
        elif choice == '3':
            hitung_rata_rata()
            if not tanya_kembali():
                break

        elif choice == '4':
            total_nilai_keseluruhan()
            if not tanya_kembali(): 
                break
            
        elif choice == '5':
            print("Terimakasih telah menggunakan layanan kami.")
            break 
        else:
            print("Input anda tidak valid, silahkan gunakan opsi angka 1 hingga 5.")

if __name__ == "__main__": # memastikan hanya fungsi main yang dijalankan saat file dieksekusi langsuung, bukan saat diimport jadi modul
    main()