
"""
BENCHMARK SISTEM MANAJEMEN INVENTARIS PRODUK
Membandingkan:
1. Hash Table (dict)
2. Array-based List (list)
3. Linked List (Custom ADT)
"""

from time import perf_counter_ns
from statistics import median


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedListADT:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        node = Node(key, value)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def search(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def delete(self, key):
        previous = None
        current = self.head

        while current is not None:
            if current.key == key:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                if current is self.tail:
                    self.tail = previous

                return True

            previous = current
            current = current.next

        return False


def buat_data(jenis, jumlah):
    if jenis == "dict":
        return {f"P{i}": i for i in range(jumlah)}

    if jenis == "list":
        return [(f"P{i}", i) for i in range(jumlah)]

    data = LinkedListADT()

    for i in range(jumlah):
        data.append(f"P{i}", i)

    return data


def cari(data, jenis, key):
    if jenis == "dict":
        return data.get(key)

    if jenis == "list":
        for id_produk, nilai in data:
            if id_produk == key:
                return nilai
        return None

    return data.search(key)


def tambah(data, jenis, key, nilai):
    if jenis == "dict":
        data[key] = nilai
    elif jenis == "list":
        data.append((key, nilai))
    else:
        data.append(key, nilai)


def hapus(data, jenis, key):
    if jenis == "dict":
        return data.pop(key, None) is not None

    if jenis == "list":
        for indeks, (id_produk, nilai) in enumerate(data):
            if id_produk == key:
                del data[indeks]
                return True
        return False

    return data.delete(key)


def ukur_waktu(jenis, jumlah_data, operasi, pengulangan=5):
    hasil = []

    for putaran in range(pengulangan):
        data = buat_data(jenis, jumlah_data)

        if operasi == "cari":
            jumlah_operasi = 100
            key = f"P{jumlah_data - 1}"

            mulai = perf_counter_ns()

            for _ in range(jumlah_operasi):
                cari(data, jenis, key)

            selesai = perf_counter_ns()

        elif operasi == "tambah":
            jumlah_operasi = 100

            mulai = perf_counter_ns()

            for nomor in range(jumlah_operasi):
                key = f"BARU_{putaran}_{nomor}"
                tambah(data, jenis, key, nomor)

            selesai = perf_counter_ns()

        elif operasi == "hapus":
            jumlah_operasi = 100

            mulai = perf_counter_ns()

            for nomor in range(jumlah_operasi):
                key = f"P{jumlah_data - 1 - nomor}"
                hapus(data, jenis, key)

            selesai = perf_counter_ns()

        else:
            raise ValueError("Operasi tidak dikenal")

        waktu = (
            (selesai - mulai) /
            jumlah_operasi /
            1_000_000
        )

        hasil.append(waktu)

    return median(hasil)


def main():
    ukuran = [1000, 5000, 10000]

    struktur = [
        ("dict", "Hash Table (dict)"),
        ("list", "Array-based List"),
        ("linked", "Linked List"),
    ]

    operasi = [
        ("cari", "PENCARIAN ID"),
        ("tambah", "PENYISIPAN PRODUK"),
        ("hapus", "PENGHAPUSAN PRODUK"),
    ]

    print("=" * 78)
    print("BENCHMARK SISTEM MANAJEMEN INVENTARIS PRODUK")
    print("Median waktu per operasi (ms)")
    print("=" * 78)

    for jenis_operasi, judul in operasi:
        print(f"\n{judul}")
        print("-" * 78)

        print(
            f"{'Struktur Data':32}"
            f"{'1.000 data':>14}"
            f"{'5.000 data':>14}"
            f"{'10.000 data':>14}"
        )

        for jenis, nama in struktur:
            waktu = [
                ukur_waktu(jenis, n, jenis_operasi)
                for n in ukuran
            ]

            print(
                f"{nama:32}"
                f"{waktu[0]:14.6f}"
                f"{waktu[1]:14.6f}"
                f"{waktu[2]:14.6f}"
            )

    print("\nKOMPLEKSITAS TEORITIS")
    print("Dict: tambah/cari/hapus rata-rata O(1), terburuk O(n).")
    print("List: pencarian O(n), append O(1) amortisasi,")
    print("      penghapusan berdasarkan ID O(n).")
    print("Linked List: pencarian O(n), append O(1) dengan tail,")
    print("             penghapusan berdasarkan ID O(n).")


if __name__ == "__main__":
    main()
