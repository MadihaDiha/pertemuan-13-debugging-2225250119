Pertemuan 13 — Debugging, Tracing, Testing, dan Test Case
Identitas Mahasiswa
Nama: Madiha
NIM: 2225250119
Kelas: 3E
Program Studi: S1 Pendidikan Matematika
Fakultas: FKIP
Universitas: Universitas Sultan Ageng Tirtayasa
Mata Kuliah: Algoritma dan Pemrograman
Dosen Pengampu: Dr. Aan Hendrayana, S.Si., M.Pd.
Tahun Ajaran: 2026/2027 Ganjil
Deskripsi Praktikum
Praktikum ini membahas proses debugging, tracing, testing, dan penyusunan test case menggunakan Python. Tujuannya adalah mengidentifikasi bug berdasarkan bukti, memperbaiki penyebab masalah, dan memastikan program berjalan sesuai hasil yang diharapkan melalui pengujian ulang.

Struktur Folder
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
Materi Praktikum
Membedakan syntax error, runtime error atau exception, dan logical error.
Membaca traceback untuk menemukan lokasi terjadinya exception.
Melakukan tracing nilai variabel dan alur kontrol program.
Menggunakan breakpoint dan debugger di VS Code.
Menyusun test case normal, batas, kosong, dan tidak valid.
Membandingkan expected result dengan actual result.
Mengidentifikasi akar penyebab bug dan memperbaiki kode.
Melakukan retest untuk memastikan tidak terjadi regresi.
Praktik 4: Investigasi dan Perbaikan Bug
Praktik ini menggunakan program yang memiliki bug pada perhitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi.

Bug yang Diinvestigasi
Bug rata-rata: program menggunakan pembagi tetap sehingga hasilnya salah ketika jumlah data berubah.
Bug batas kelulusan: program menggunakan operator > sehingga nilai 60 tidak dianggap lulus.
Bug nilai tertinggi: kondisi perbandingan pada perulangan salah sehingga nilai tertinggi tidak diperbarui dengan benar.
Test Case
ID	Pengujian	Input	Expected Result
T1	Rata-rata	[80, 60, 90, 70]	75.0
T2	Rata-rata	[100, 80]	90.0
T3	Status kelulusan	60	Lulus
T4	Status kelulusan	59	Tidak lulus
T5	Nilai tertinggi	[80, 60, 90, 70]	90
Cara Menjalankan Program
Jalankan perintah berikut dari folder utama proyek:

python praktik/praktik_4_debugging.py
Hasil Retest
Bagian ini diisi berdasarkan hasil pengujian setelah kode diperbaiki. Pastikan seluruh test case telah dijalankan kembali dan hasil aktual sesuai dengan hasil yang diharapkan.

ID	Expected Result	Actual Result	Status
T1	75.0	Isi setelah pengujian	PASS/FAIL
T2	90.0	Isi setelah pengujian	PASS/FAIL
T3	Lulus	Isi setelah pengujian	PASS/FAIL
T4	Tidak lulus	Isi setelah pengujian	PASS/FAIL
T5	90	Isi setelah pengujian	PASS/FAIL
Bug Report
Setiap bug didokumentasikan dengan gejala, test case yang membuktikannya, lokasi bug, akar penyebab, perbaikan, dan hasil retest.

Refleksi
Melalui praktikum ini, saya mempelajari bahwa program yang dapat dijalankan belum tentu menghasilkan output yang benar. Tracing dan test case membantu menemukan kesalahan secara sistematis. Setelah melakukan perbaikan, program perlu diuji kembali untuk memastikan hasilnya sesuai dan tidak menimbulkan bug baru.
