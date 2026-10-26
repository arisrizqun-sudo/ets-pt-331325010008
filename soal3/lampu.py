class Lampu:
    """Kelas Lampu dengan atribut kelas jumlah_lampu dan metode __str__."""

    jumlah_lampu = 0

    def __init__(self, nama):
        self.nama = nama
        self.aktif = False
        self.kecerahan = 0
        Lampu.jumlah_lampu += 1

    def nyalakan(self):
        self.aktif = True
        self.kecerahan = 100

    def matikan(self):
        self.aktif = False
        self.kecerahan = 0

    def atur(self, nilai):
        if self.aktif and (0 <= nilai <= 100):
            self.kecerahan = nilai

    def __str__(self):
        """Menghasilkan teks berformat: Lampu L1: aktif = True, kecerahan = 60"""
        return f"Lampu {self.nama}: aktif = {self.aktif}, kecerahan = {self.kecerahan}"