
# Latihan 4 - Bug Rata-rata

def rata_rata(data):
    if len(data) == 0:
        return 0

    total = sum(data)
    return total / len(data)


nilai = [80, 90, 70]

print("Data nilai:", nilai)
print("Rata-rata:", rata_rata(nilai))