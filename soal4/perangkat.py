class Perangkat:
    """Kelas Induk Perangkat Pengukuran"""

    def __init__(self, nama):
        self.nama = nama
        self.data = []  

    def baca(self, nilai):
        """Menambahkan nilai ke dalam list data."""
        self.data.append(nilai)

    def proses(self):
        """Metode abstrak yang harus di-override oleh kelas anak."""
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini.")


class SensorSuhu(Perangkat):
    """Kelas SensorSuhu mewarisi Perangkat.
    Tanpa constructor sendiri. proses() mengembalikan nilai tertinggi pada data.
    """

    def proses(self):
        if not self.data:
            return 0
        return max(self.data)


class SensorDebit(Perangkat):
    """Kelas SensorDebit mewarisi Perangkat.
    Constructor menggunakan super().__init__ dan menambah atribut satuan.
    proses() mengembalikan nilai rata-rata data.
    """

    def __init__(self, nama, satuan):
        super().__init__(nama)
        self.satuan = satuan

    def proses(self):
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)