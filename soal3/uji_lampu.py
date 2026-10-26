from lampu import Lampu

l1 = Lampu("L1")
print(f"Awal -> aktif: {l1.aktif}, kecerahan: {l1.kecerahan}")

l1.nyalakan()
print(f"Setelah nyalakan() -> aktif: {l1.aktif}, kecerahan: {l1.kecerahan}")

for _ in range(3):
    nilai_input = int(input("Masukkan nilai kecerahan: "))
    l1.atur(nilai_input)
    print(
        f"Setelah atur({nilai_input}) -> aktif: {l1.aktif}, kecerahan: {l1.kecerahan}"
    )

l1.matikan()
print(f"Setelah matikan() -> aktif: {l1.aktif}, kecerahan: {l1.kecerahan}")