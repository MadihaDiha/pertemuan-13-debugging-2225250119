def baca_nilai(nama_file):
    nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if baris:
                    nilai.append(int(baris))

    except FileNotFoundError:
        print("File tidak ditemukan.")
    except ValueError:
        print("Data nilai harus berupa bilangan bulat.")

    return nilai


hasil = baca_nilai("nilai.txt")
print("Daftar nilai:", hasil)
