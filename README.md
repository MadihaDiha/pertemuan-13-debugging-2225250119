# Pertemuan 13 — Debugging, Tracing, Testing, dan Test Case

## Identitas Mahasiswa

- **Nama:** Madiha
- **NIM:** 2225250119
- **Kelas:** 3E
- **Program Studi:** S1 Pendidikan Matematika


## Deskripsi Praktikum

Praktikum ini membahas proses debugging, tracing, testing, dan penyusunan test case menggunakan Python. Tujuannya adalah mengidentifikasi bug berdasarkan bukti, menemukan akar penyebab masalah, memperbaiki kode, dan memastikan program berjalan sesuai dengan hasil yang diharapkan melalui pengujian ulang (*retest*).

## Tujuan Praktikum

1. Memahami konsep debugging, tracing, testing, dan test case.
2. Mengidentifikasi berbagai jenis kesalahan dalam program Python.
3. Menelusuri alur eksekusi program dan perubahan nilai variabel.
4. Menggunakan breakpoint dan debugger di Visual Studio Code.
5. Menyusun test case untuk membuktikan adanya bug.
6. Memperbaiki kesalahan logika pada program.
7. Melakukan pengujian ulang untuk memastikan perbaikan berhasil.
8. Mendokumentasikan hasil investigasi dan perbaikan bug.

## Struktur Folder

```text
pertemuan-13-debugging-2225250042/
├── README.md
├── .gitignore
├── kasus/
│   ├── kasus_01_batas_kelulusan.py
│   ├── kasus_02_rata_rata.py
│   └── kasus_03_file_nilai.py
├── latihan/
│   ├── 01_trace_loop.py
│   ├── 02_trace_fungsi.py
│   ├── 03_test_case.py
│   └── 04_debug_breakpoint.py
└── praktik/
    └── praktik_4_debugging.py
```

## Materi Praktikum

1. Membedakan *syntax error*, *runtime error* atau exception, dan *logical error*.
2. Membaca traceback untuk menemukan lokasi terjadinya exception.
3. Melakukan tracing terhadap nilai variabel dan alur kontrol program.
4. Menggunakan breakpoint dan debugger di Visual Studio Code.
5. Menyusun test case normal, batas, kosong, dan tidak valid.
6. Membandingkan *expected result* dengan *actual result*.
7. Mengidentifikasi akar penyebab bug dan memperbaiki kode.
8. Melakukan retest untuk memastikan perbaikan berhasil dan tidak menimbulkan regresi.

## Deskripsi Latihan

| **File** | **Keterangan** |
|---|---|
| `01_trace_loop.py` | Menelusuri perubahan nilai variabel dalam perulangan dan mengamati hasil setiap iterasi. |
| `02_trace_fungsi.py` | Menelusuri pemanggilan fungsi, parameter, proses perhitungan diskon, dan nilai `return`. |
| `03_test_case.py` | Menguji status kelulusan menggunakan beberapa nilai untuk memeriksa batas kelulusan. |
| `04_debug_breakpoint.py` | Mengidentifikasi dan memperbaiki kesalahan perhitungan rata-rata. |
| `praktik_4_debugging.py` | Menginvestigasi, memperbaiki, dan menguji ulang bug pada pengolahan nilai mahasiswa. |

## Praktik 4: Investigasi dan Perbaikan Bug

Praktik ini menggunakan program pengolahan nilai mahasiswa yang memiliki tiga kesalahan logika, yaitu pada perhitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi.

### Bug yang Diinvestigasi

- **Bug rata-rata:** Program menggunakan pembagi tetap sehingga hasil perhitungan tidak sesuai ketika jumlah data berubah.
- **Bug batas kelulusan:** Program menggunakan operator `>` sehingga nilai 60 tidak dianggap lulus.
- **Bug nilai tertinggi:** Program menggunakan operator pembanding yang salah sehingga nilai tertinggi tidak diperbarui dengan benar.

### Test Case

Test case digunakan untuk membuktikan kesalahan pada program awal dan memeriksa apakah hasil perbaikan sudah sesuai dengan yang diharapkan.

| **ID** | **Pengujian** | **Input** | **Expected Result** |
|---|---|---|---|
| T1 | Rata-rata | `[80, 60, 90, 70]` | `75.0` |
| T2 | Rata-rata | `[100, 80]` | `90.0` |
| T3 | Status kelulusan | `60` | `Lulus` |
| T4 | Status kelulusan | `59` | `Tidak lulus` |
| T5 | Nilai tertinggi | `[80, 60, 90, 70]` | `90` |

### Cara Menjalankan Program

Pastikan Python sudah terpasang dan terminal VS Code berada di folder utama proyek.

Jalankan program praktik menggunakan perintah berikut:

```bash
python praktik/praktik_4_debugging.py
```

Untuk menjalankan latihan secara terpisah, gunakan perintah berikut:

```bash
python latihan/01_trace_loop.py
python latihan/02_trace_fungsi.py
python latihan/03_test_case.py
python latihan/04_debug_breakpoint.py
```

## Hasil Retest

Retest dilakukan setelah bug diperbaiki untuk memastikan bahwa setiap fungsi menghasilkan keluaran sesuai dengan hasil yang diharapkan.

| **ID** | **Expected Result** | **Actual Result** | **Status** |
|---|---|---|---|
| T1 | `75.0` | `75.0` | PASS |
| T2 | `90.0` | Belum diuji secara terpisah | Belum diuji |
| T3 | `Lulus` | `Lulus` | PASS |
| T4 | `Tidak lulus` | Belum diuji secara terpisah | Belum diuji |
| T5 | `90` | `90` | PASS |

**Catatan:** T1, T3, dan T5 sesuai dengan hasil program yang telah dijalankan. T2 dan T4 perlu diuji secara terpisah sebelum dinyatakan berhasil.

## Bug Report

Setiap bug didokumentasikan berdasarkan gejala, test case, akar penyebab, perbaikan, dan hasil pengujian ulang.

| **Bug** | **Gejala** | **Akar Penyebab** | **Perbaikan** |
|---|---|---|---|
| Bug rata-rata | Hasil rata-rata tidak sesuai dengan jumlah data. | Menggunakan pembagi tetap `5`. | Menggunakan `len(nilai)` sebagai pembagi. |
| Bug batas kelulusan | Nilai 60 dinyatakan tidak lulus. | Menggunakan operator `>`. | Mengganti operator menjadi `>=`. |
| Bug nilai tertinggi | Fungsi tidak menemukan nilai tertinggi dengan benar. | Menggunakan operator `<` untuk mencari nilai terbesar. | Menggunakan operator `>` dan menginisialisasi nilai tertinggi dari elemen pertama. |

## Kesimpulan

Berdasarkan praktikum yang dilakukan, debugging membantu menemukan dan memperbaiki kesalahan logika dalam program Python. Tracing digunakan untuk menelusuri alur eksekusi, sedangkan test case digunakan untuk membuktikan adanya bug dan memeriksa hasil perbaikan.

Pengujian ulang diperlukan untuk memastikan bahwa perbaikan menghasilkan keluaran yang sesuai dengan harapan. Dokumentasi bug report juga membantu menjelaskan penyebab kesalahan, langkah perbaikan, dan hasil pengujian secara sistematis.

## Refleksi

Melalui praktikum ini, saya mempelajari bahwa program yang dapat dijalankan belum tentu menghasilkan output yang benar. Tracing dan test case membantu menemukan kesalahan secara sistematis. Saya juga memahami pentingnya memperbaiki akar penyebab bug dan melakukan pengujian ulang untuk memastikan hasilnya sesuai dengan yang diharapkan serta mengurangi risiko munculnya kesalahan baru.

---
