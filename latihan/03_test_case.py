
# Latihan 3 - Bug Batas Kelulusan

def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


# Test case
test_nilai = [59, 60, 61]

for nilai in test_nilai:
    print(f"Nilai: {nilai} -> {status_lulus(nilai)}")