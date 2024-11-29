produk = {
    "001": {"nama": "Laptop", "harga": 10000000},
    "002": {"nama": "Smartphone", "harga": 5000000},
    "003": {"nama": "Headphone", "harga": 1500000},
    "004": {"nama": "Printer", "harga": 3000000},
}

pengguna = {
    "user1": "password1",
    "user2": "password2",
    "admin": "admin123"
}

pesanan = {}

def tampilkan_produk():
    print("\nDaftar Produk:")
    for kode, info in produk.items():
        print(f"{kode}: {info['nama']} - Rp {info['harga']:,}")

def hitung_total_harga(kode_produk, jumlah):
    harga = produk[kode_produk]["harga"]
    total = harga * jumlah
    return total

def konfirmasi_pesanan(kode_produk, jumlah):
    total_harga = hitung_total_harga(kode_produk, jumlah)
    print(f"\nAnda memesan {jumlah} {produk[kode_produk]['nama']}.")
    print(f"Total harga: Rp {total_harga:,}")
    konfirmasi = input("Apakah Anda ingin melanjutkan pesanan? (ya/tidak): ").strip()
    return konfirmasi == "ya" or konfirmasi == "Ya"

def login():
    print("=== Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in pengguna and pengguna[username] == password:
        print("Login berhasil!")
        return True
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return False

def tampilkan_pesanan():
    if pesanan:
        print("\nPesanan Anda:")
        for kode, jumlah in pesanan.items():
            print(f"{produk[kode]['nama']} - {jumlah} buah - Rp {hitung_total_harga(kode, jumlah):,}")
    else:
        print("Anda belum memesan apapun.")

def edit_pesanan():
    tampilkan_pesanan()
    kode_produk = input("\nMasukkan kode produk yang ingin diedit: ").strip()
    
    if kode_produk in pesanan:
        try:
            jumlah = int(input("Masukkan jumlah baru: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                return
            pesanan[kode_produk] = jumlah
            print(f"Pesanan untuk {produk[kode_produk]['nama']} telah diperbarui.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
    else:
        print("Produk tidak ditemukan dalam pesanan Anda.")

def hapus_pesanan():
    tampilkan_pesanan()
    kode_produk = input("\nMasukkan kode produk yang ingin dihapus dari pesanan: ").strip()
    
    if kode_produk in pesanan:
        del pesanan[kode_produk]
        print(f"Pesanan untuk {produk[kode_produk]['nama']} telah dihapus.")
    else:
        print("Produk tidak ditemukan dalam pesanan Anda.")

def main():
    while not login():
        continue  

    while True:
        print("\nMenu:")
        print("1. Tampilkan daftar produk")
        print("2. Lihat pesanan Anda")
        print("3. Edit pesanan")
        print("4. Hapus pesanan")
        print("5. Selesai (keluar)")

        pilihan = input("Pilih opsi (1/2/3/4/5): ").strip()

        if pilihan == '1':
            tampilkan_produk()
            
            kode_produk = input("\nMasukkan kode produk yang ingin dipesan (atau ketik 'keluar' untuk selesai): ").strip()
            
            if kode_produk == 'keluar' or kode_produk == 'Keluar':
                print("Terima kasih telah berbelanja!")
                break
            
            if kode_produk not in produk:
                print("Kode produk tidak valid. Silakan coba lagi.")
                continue
            
            try:
                jumlah = int(input("Masukkan jumlah yang ingin dipesan: "))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0.")
                    continue
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
                continue
            
            if konfirmasi_pesanan(kode_produk, jumlah):
                pesanan[kode_produk] = jumlah
                print(f"Pesanan {produk[kode_produk]['nama']} berhasil ditambahkan!")
            else:
                print("Pesanan dibatalkan.")
        
        elif pilihan == '2':
            tampilkan_pesanan()
        
        elif pilihan == '3':
            edit_pesanan()
        
        elif pilihan == '4':
            hapus_pesanan()
        
        elif pilihan == '5':
            print("Terima kasih telah berbelanja!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

main()
