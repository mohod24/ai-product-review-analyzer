# AI Product Review Analyzer - Frontend Client

Antarmuka pengguna (User Interface) modern yang dibangun menggunakan **React** dan **Vite**. Aplikasi ini memungkinkan pengguna memasukkan ulasan produk dan melihat hasil analisis AI secara real-time dengan tampilan yang responsif.

![React](https://img.shields.io/badge/React-18-blue)
![Vite](https://img.shields.io/badge/Build_Tool-Vite-purple)
![CSS](https://img.shields.io/badge/Style-Responsive_CSS-orange)

## Fitur Antarmuka

- **Responsive Design:** Tampilan otomatis menyesuaikan layar Desktop (Layout Horizontal) dan Mobile (Layout Vertikal).
- **Real-time Feedback:** Indikator loading saat AI sedang memproses data.
- **Dynamic Styling:** Badge warna (Hijau/Merah/Biru) berubah otomatis sesuai hasil sentimen [cite: 667-668].
- **History Log:** Menampilkan riwayat analisis sebelumnya yang diambil dari database.

## Teknologi yang Digunakan

- **Framework:** React JS.
- **Build Tool:** Vite (untuk performa development yang cepat).
- **HTTP Client:** Axios (untuk komunikasi dengan Backend Pyramid).
- **Styling:** Custom CSS (Flexbox, CSS Variables, Media Queries).

## Struktur Folder

```bash
tugas_individu_3/
└── frontend/               # Client Side Interface
    ├── src/
    │   ├── components/     # ReviewForm, AnalysisResult, ReviewList
    │   ├── App.css         # Styling Responsif
    │   └── App.jsx         # Komponen Utama
    └── package.json        # Daftar Pustaka JavaScript
```

## Prasyarat

- Node.js (v16 atau lebih baru).
- npm (Node Package Manager).

## Langkah Instalasi & Menjalankan

### 1. Masuk ke Folder Frontend

```bash
cd frontend
```

### 2. Masuk ke Folder Frontend

```bash
npm install
```

### 3. Konfigurasi Environment Variables (.env)

Buat file bernama .env di dalam folder frontend/ untuk menyimpan URL Backend:

```bash
# Pastikan port sesuai dengan port Backend Pyramid Anda
VITE_API_URL=http://localhost:6543/api
```

### 4. Menjalankan Development Server

```bash
npm run dev
```

Akses aplikasi melalui browser di alamat yang muncul (biasanya http://localhost:5173).

## Kontribusi & Credits

Project ini dikembangkan sebagai Tugas Praktikum Mata Kuliah Pengembangan Aplikasi Web.

- Sentiment Model: DistilBERT SST-2 English
- Summarization API: Google Gemini.

## Identitas Mahasiswa

- Nama: Mohd.Musyaffa Alief Athallah
- NIM: 123140184
- Kelas: Praktikum Pemrograman Web RB
