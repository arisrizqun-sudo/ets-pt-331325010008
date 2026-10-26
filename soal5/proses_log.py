def baca_log(nama_file):
    data_valid = []
    data_ditolak = []

    with open(nama_file, "r") as file:
        lines = file.readlines()

    for nomor_baris in range(1, len(lines)):
        baris_teks = lines[nomor_baris].strip()
        if not baris_teks:
            continue

        kolom = baris_teks.split(",")

        if len(kolom) != 2:
            data_ditolak.append(
                (nomor_baris + 1, baris_teks, "Jumlah kolom bukan dua")
            )
            continue

        waktu_str, debit_str = kolom[0].strip(), kolom[1].strip()

        try:
            debit = float(debit_str)
        except ValueError:
            data_ditolak.append(
                (nomor_baris + 1, baris_teks, "Nilai debit bukan angka")
            )
            continue

        if not (5 <= debit <= 25):
            data_ditolak.append(
                (
                    nomor_baris + 1,
                    baris_teks,
                    "Nilai di luar rentang valid (5 - 25)",
                )
            )
            continue

        # Jika lolos semua validasi
        data_valid.append((waktu_str, debit))

    return data_valid, data_ditolak


def galat_absolut(hasil, acuan):
    return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
    if acuan == 0:
        raise ValueError("Nilai acuan tidak boleh nol.")
    return (abs(hasil - acuan) / abs(acuan)) * 100


if __name__ == "__main__":
    valid, ditolak = baca_log("log_debit.csv")

    print(f"Jumlah data valid: {len(valid)}")
    print(f"Jumlah data ditolak: {len(ditolak)}")

    print("\nAlasan penolakan:")
    for no, isi, alasan in ditolak:
        print(f"Baris {no} ({isi}): {alasan}")

    # Menghitung rata-rata data valid
    if valid:
        total_debit = sum([item[1] for item in valid])
        rata_rata = total_debit / len(valid)
        print(f"\nRata-rata data valid (2 desimal): {rata_rata:.2f}")
    else:
        rata_rata = 0.0
        print("\nTidak ada data valid.")