from lampu import Lampu


class PanelLampu:
    """Kelas PanelLampu yang menerapkan komposisi menyimpan dua objek Lampu."""

    def __init__(self):
        self.lampu_merah = Lampu("merah")
        self.lampu_hijau = Lampu("hijau")

    def nyalakan_semua(self):
        """Menyalakan kedua lampu pada panel."""
        self.lampu_merah.nyalakan()
        self.lampu_hijau.nyalakan()

    def tampilkan(self):
        """Mencetak kondisi kedua lampu."""
        print(self.lampu_merah)
        print(self.lampu_hijau)


if __name__ == "__main__":
    panel = PanelLampu()

    panel.nyalakan_semua()

    panel.lampu_hijau.atur(30)

    panel.tampilkan()