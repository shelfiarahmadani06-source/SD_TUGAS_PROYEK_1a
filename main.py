from models.produk import Produk
from structures.inventaris import InventarisADT
from views.menu import Menu


def main():

    inventaris = InventarisADT()

    # Data awal
    inventaris.tambah_produk(
        Produk("P001", "Laptop", "Elektronik", 8500000, 10)
    )

    inventaris.tambah_produk(
        Produk("P002", "Mouse", "Aksesori", 150000, 25)
    )

    inventaris.tambah_produk(
        Produk("P003", "Keyboard", "Aksesori", 350000, 15)
    )

    aplikasi = Menu(inventaris)
    aplikasi.jalankan()


if __name__ == "__main__":
    main()