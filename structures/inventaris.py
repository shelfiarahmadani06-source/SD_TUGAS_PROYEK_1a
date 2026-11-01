class InventarisADT:

    def __init__(self):
        self._data = {}

    # INSERTION
    def tambah_produk(self, produk):
        if produk.id_produk in self._data:
            return False

        self._data[produk.id_produk] = produk
        return True

    # SEARCHING
    def cari_produk(self, id_produk):
        return self._data.get(id_produk)

    # DELETION
    def hapus_produk(self, id_produk):
        if id_produk in self._data:
            del self._data[id_produk]
            return True

        return False

    # MENAMPILKAN DATA
    def tampilkan_produk(self):
        return list(self._data.values())