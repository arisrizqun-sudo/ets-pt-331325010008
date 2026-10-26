def rentang(data):
    """Mengembalikan tuple (nilai terkecil, nilai terbesar) dari data."""
    if not data:
        return (0, 0)
    return (min(data), max(data))


def ringkasan(data):
    """Mengembalikan dictionary berkunci 'jumlah', 'min', 'maks', dan 'rata'."""
    if not data:
        return {"jumlah": 0, "min": 0, "maks": 0, "rata": 0}

    jml = len(data)
    mn = min(data)
    mx = max(data)
    rt = sum(data) / jml

    return {"jumlah": jml, "min": mn, "maks": mx, "rata": rt}


if __name__ == "__main__":
    data_uji = [12.0, 15.0, 15.0]

    print(rentang(data_uji))

    r = ringkasan(data_uji)
    print(r)

    print(r["rata"])