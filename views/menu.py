class Menu:

    def __init__(self, inventaris):
        self.inventaris = inventaris

    def tampilkan_menu(self):
        print("\n================================")
        print(" SISTEM MANAJEMEN INVENTARIS")
        print("================================")
        print("1. Tambah Produk")
        print("2. Cari Produk")
        print("3. Hapus Produk")
        print("4. Tampilkan Semua Produk")
        print("0. Keluar")
        print("================================")

    def jalankan(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.tambah()

            elif pilihan == "2":
                self.cari()

            elif pilihan == "3":
                self.hapus()

            elif pilihan == "4":
                self.tampilkan_semua()

            elif pilihan == "0":
                print("Program selesai.")
                break

            else:
                print("Pilihan tidak valid!")

    def tambah(self):
        from models.produk import Produk

        try:
            id_produk = input("ID Produk: ").strip()
            nama = input("Nama: ").strip()
            kategori = input("Kategori: ").strip()
            harga = float(input("Harga: "))
            stok = int(input("Stok: "))

            if not id_produk or not nama or not kategori:
                print("Data tidak boleh kosong!")
                return

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif!")
                return

            produk = Produk(
                id_produk, nama, kategori, harga, stok
            )

            if self.inventaris.tambah_produk(produk):
                print("Produk berhasil ditambahkan!")
            else:
                print("ID produk sudah terdaftar!")

        except ValueError:
            print("Input harga atau stok tidak valid!")

    def cari(self):
        id_produk = input("Masukkan ID Produk: ").strip()
        produk = self.inventaris.cari_produk(id_produk)

        if produk:
            print("\nProduk ditemukan!")
            print("ID       :", produk.id_produk)
            print("Nama     :", produk.nama)
            print("Kategori :", produk.kategori)
            print("Harga    :", produk.harga)
            print("Stok     :", produk.stok)
        else:
            print("Produk tidak ditemukan!")

    def hapus(self):
        id_produk = input("Masukkan ID Produk: ").strip()

        if self.inventaris.hapus_produk(id_produk):
            print("Produk berhasil dihapus!")
        else:
            print("Produk tidak ditemukan!")

    def tampilkan_semua(self):
        produk_list = self.inventaris.tampilkan_produk()

        if not produk_list:
            print("Inventaris masih kosong!")
            return

        for produk in produk_list:
            print("-----------------------------")
            print("ID       :", produk.id_produk)
            print("Nama     :", produk.nama)
            print("Kategori :", produk.kategori)
            print("Harga    :", produk.harga)
            print("Stok     :", produk.stok)