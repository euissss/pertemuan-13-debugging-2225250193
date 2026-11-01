def baca_nilai(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, nilai = baris.split(",")
                    nilai = float(nilai)

                    if nilai < 0 or nilai > 100:
                        print(f"Nilai tidak valid pada baris {nomor}")
                        continue

                    data.append((nim, nilai))

                except ValueError:
                    print(f"Format data salah pada baris {nomor}")

    except FileNotFoundError:
        print("File tidak ditemukan.")

    return data


hasil = baca_nilai("data/nilai.txt")

print("\nData nilai yang valid:")
for nim, nilai in hasil:
    print(nim, nilai)