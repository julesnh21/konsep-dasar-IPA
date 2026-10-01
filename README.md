# Konsep Dasar IPA

Portal pembelajaran statis untuk mahasiswa PGMI. Beranda memuat peta 16 topik; Zat dan Perubahannya serta Gaya dan Gerak tersedia. Topik lain ditandai belum tersedia.

## Menjalankan lokal

Gunakan server HTTP, misalnya `python3 -m http.server 8000`, lalu buka `http://localhost:8000`. JavaScript module memerlukan HTTP, bukan membuka file langsung.

## Publikasi GitHub Pages

Di Settings → Pages → Build and deployment, pilih Deploy from a branch, branch `main`, folder `/ (root)`, lalu Save. Situs: https://julesnh21.github.io/konsep-dasar-IPA/ setelah proses deployment selesai.

## Struktur

- `index.html`: menu topik.
- `topik/gaya/index.html`, `motion.js`, `physics.js`: materi, simulasi gaya satu dimensi, latihan, dan refleksi.
- `topik/zat/`: materi sebelumnya yang diintegrasikan. Ilustrasi tetap bersumber dari repositori asal melalui URL mentah GitHub.
- `styles.css`: gaya portal dan topik Gaya dan Gerak.

## Batas model dan data

Model menggunakan bidang horizontal, g = 9.8 m/s², dan koefisien gesek statis serta kinetis yang disamakan. Tidak mencakup gerak rotasi atau hambatan udara. Catatan refleksi tersimpan lokal di peramban dan dapat diunduh; nilai latihan tidak terkirim ke server atau dosen.

Untuk menambah topik: buat folder di `topik/`, gunakan navigasi relatif, dan aktifkan kartu topik di beranda. Berkas `build-site.py` membangun beranda dan halaman Gaya; jika mengedit HTML langsung, selaraskan juga skrip tersebut sebelum menjalankannya lagi.
