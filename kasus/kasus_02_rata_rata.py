def rata_rata(data):
    if len(data) == 0:
        return 0

    total = sum(data)
    return total / len(data)


# Pengujian
print("Rata-rata 1:", rata_rata([80, 90, 70]))
print("Rata-rata 2:", rata_rata([100, 80]))
print("Rata-rata 3:", rata_rata([70, 80, 90, 100, 60]))
print("Rata-rata data kosong:", rata_rata([]))