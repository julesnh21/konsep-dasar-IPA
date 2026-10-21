# Konsep Dasar IPA — PGMI

Portal satu semester dengan 16 topik konseptual, 48 keadaan visual yang dapat dipilih, kegiatan mahasiswa, cek pemahaman, dan refleksi. Materi fisika memakai teori serta aplikasi sehari-hari tanpa rumus; perhitungan sederhana dibatasi pada jarak, waktu, dan kelajuan rata-rata.

Website: https://julesnh21.github.io/konsep-dasar-IPA/

## Peta semester

`semester.html` memuat rancangan 16 pertemuan: 14 sesi pembelajaran, UTS, dan UAS. Gelombang–bunyi dengan cahaya, serta struktur tumbuhan dengan hewan, digabung pada dua sesi dengan batas konsep inti dan bacaan pengayaan yang dijelaskan pada peta. Peta ini bukan RPS resmi.

## Menjalankan dan mengubah

Gunakan `python3 -m http.server 8000`, lalu buka `http://localhost:8000`.

- `course_data.py`: naskah seluruh materi, kasus visual, kegiatan, pertanyaan, dan peta pertemuan.
- `course_visuals.py`: diagram SVG konseptual yang dapat diubah secara presisi.
- `build-site.py`: pembangun halaman statis, peta semester, asesmen, dan catatan kalibrasi.
- `learn.js`: pergantian visual, penyimpanan/unduhan catatan, dan kalkulator kelajuan.
- `styles.css` dan `course.css`: tampilan responsif.

Sesudah mengubah sumber Python, jalankan `python3 build-site.py`. Tidak perlu paket npm atau framework untuk menjalankan website. Halaman HTML hasil build turut disimpan agar dapat langsung diterbitkan di GitHub Pages.

## Pemeriksaan

```
python3 build-site.py
python3 tests/course.test.py
python3 tests/check_links.py
node --check learn.js
```

GitHub Actions menjalankan pemeriksaan tersebut serta memastikan hasil build konsisten. Pemeriksaan peramban desktop dan ponsel juga dilakukan pada versi ini; catatannya ada di `KALIBRASI.md`.

## Penggunaan oleh mahasiswa

Pilih topik, buat dugaan sebelum membuka penjelasan visual, kerjakan kegiatan, lalu periksa alasan melalui pembahasan. Catatan disimpan lokal per topik jika penyimpanan peramban tersedia dan dapat diunduh sebagai teks. Tidak ada login, pengiriman nilai, atau pencatatan kehadiran.

Latihan esai UTS/UAS adalah bahan terbuka beserta rubrik, bukan ujian daring terkendali atau naskah rahasia. Dosen menentukan pelaksanaan dan penilaian.

## Batas bahan

Visual merupakan skema, bukan ukuran anatomi, lintasan, atau jarak yang selalu berskala. Batas model dijelaskan di halaman. Kalibrasi internal tidak menggantikan penilaian ahli eksternal dan belum menunjukkan efektivitas belajar pada mahasiswa.

## Publikasi

Settings → Pages → Deploy from a branch → `main` → `/ (root)`. Materi lama Zat dan Perubahannya pada alamat subhalaman tetap diarahkan ke halaman terpadu. Repositori lama yang terpisah tidak diubah.
