import unittest

from models.produk import Produk
from structures.inventaris import InventarisADT


class TestInventaris(unittest.TestCase):

    def setUp(self):
        self.inventaris = InventarisADT()
        self.produk = Produk(
            "P001", "Laptop", "Elektronik", 8500000, 10
        )

    def test_tambah_produk(self):
        self.assertTrue(
            self.inventaris.tambah_produk(self.produk)
        )

    def test_id_duplikat(self):
        self.inventaris.tambah_produk(self.produk)

        self.assertFalse(
            self.inventaris.tambah_produk(self.produk)
        )

    def test_cari_produk(self):
        self.inventaris.tambah_produk(self.produk)

        hasil = self.inventaris.cari_produk("P001")

        self.assertEqual(hasil.nama, "Laptop")

    def test_produk_tidak_ditemukan(self):
        self.assertIsNone(
            self.inventaris.cari_produk("P999")
        )

    def test_hapus_produk(self):
        self.inventaris.tambah_produk(self.produk)

        self.assertTrue(
            self.inventaris.hapus_produk("P001")
        )

        self.assertIsNone(
            self.inventaris.cari_produk("P001")
        )


if __name__ == "__main__":
    unittest.main()