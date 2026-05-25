aras_nilai = []

def display_menu():
    print("\n*=== DATA NILAI SISWA ===*")
    print("1. Tambah Data")
    print("2. Tampilkan Semua Data")
    print("3. Hitung Rata-Rata")
    print("4. Total Nilai")
    print("5. Keluar")

def tambah_data():
    print("\n--- Tambah Data Nilai ---")
    mapel = input("Masukkan nama mata pelajaran: ")

    while True:
        try:
            nilai = float(input(f"Masukkan nilai untuk {mapel}: "))

            if nilai <= 100:
                aras_nilai.append([mapel, nilai])
            else:
                print("Angka yang kamu masukan tidak valid. Silahkan coba lagi")

        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")


def lihat_data():
    print("\n--- Data Nilai Mata Pelajaran ---")
    
    if not aras_nilai:
        print("Tidak ada data.")
        return
    
    for mapel, nilai in aras_nilai:
        print(f"- {mapel}: {nilai:g}")

def hitung_rata_rata():
    print("\n--- Rata-Rata Nilai ---")
    if not aras_nilai:
        print("Tidak ada data untuk dihitung.")
        return
    
    total = sum(nilai for mapel, nilai in aras_nilai)
    rata_rata = total / len(aras_nilai)
    print(f"Rata-rata dari {len(aras_nilai)} mata pelajaran adalah: {rata_rata:.2f}")

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
            kembali = input("\nKembali ke menu utama? (y/n): ").lower()
            if kembali != 'y':
                print("Terimakasih telah menggunakan layanan kami.")
                break
                
        elif choice == '2':
            lihat_data()
            kembali = input("\nKembali ke menu utama? (y/n): ").lower()
            if kembali != 'y':
                print("Terimakasih telah menggunakan layanan kami.")
                break
                
        elif choice == '3':
            hitung_rata_rata()
            
        elif choice == '4':
            total_nilai_keseluruhan()
            
        elif choice == '5':
            print("Terimakasih telah menggunakan layanan kami.")
            break 
        else:
            print("Input anda tidak valid, silahkan gunakan opsi angka 1 hingga 5.")

if __name__ == "__main__":
    main()