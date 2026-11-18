# Tugas Kelompok: Evaluasi Model Data Science

Tugas kelompok mata kuliah Sains Data Terapan (SVPL261506), materi **DS 11 Evaluasi Model**
(Dr. Muhammad Fakhrurrifqi dan Anindita Suryarasmi, Ph.D.).

## Anggota Kelompok

| No | Nama | NIM |
|----|------|-----|
| 1  | Hafidz Rizqullah Prasetya | 24/535493/SV/24243 |
| 2  | Pralambang Bhayangkara Yhudanto | 24/536223/SV/24414 |
| 3  | Alfiz Desta Ariant Permana | 24/543220/SV/25173 |
| 4  | Danny Setiawan | 24/541304/SV/24894 |

## Instruksi Tugas

Sesuai slide terakhir materi (`DS 11 Evaluasi.pptx.pdf`, halaman 25):

1. Bentuk kelompok berisi 3-4 mahasiswa.
2. Buat contoh kasus sendiri, berisi nilai **aktual** dan **hasil prediksi** model
   (kecuali clustering, yang tidak punya label aktual).
3. Hitung evaluasinya untuk empat jenis model:
   - Regresi
   - Clustering
   - Klasifikasi dengan **3 kategori kelas**
   - Deteksi objek

## Cakupan per Bagian

Metrik di bawah diambil dari slide. Metrik **tebal** adalah inti yang wajib dihitung;
sisanya opsional sebagai pelengkap.

### 1. Regresi

Pertanyaan: seberapa dekat prediksi dengan nilai sebenarnya? Error = aktual − prediksi.

- Data: tabel `n` baris berisi `y_aktual` dan `y_prediksi` (contoh slide: aktual 7 jam tidur, prediksi 6 jam).
- Metrik inti: **MAE**, **MSE**, **RMSE**, **R²**.
- Opsional: RAE, RSE, MAPE, MPE.

| Metrik | Rumus | Interpretasi |
|--------|-------|--------------|
| MAE  | `(1/n) Σ \|y − ŷ\|` | rata-rata error absolut, makin kecil makin baik |
| MSE  | `(1/n) Σ (y − ŷ)²` | error besar lebih dihukum |
| RMSE | `√MSE` | satuan sama dengan `y`, makin kecil makin baik |
| R²   | `1 − Σ(y − ŷ)² / Σ(y − ȳ)²` | proporsi variasi yang dijelaskan, mendekati 1 lebih baik |

### 2. Clustering

Pertanyaan: apakah kelompok yang terbentuk bermakna? Tidak ada label aktual.

- Data: titik 2D beserta label cluster hasil algoritma (contoh slide: X = jam tidur, Y = screen time mahasiswa).
- Metrik inti: **Silhouette**, **Inertia**, **Davies-Bouldin Index**.
- Opsional: Calinski-Harabasz, Dunn Index, Rand Index, Mutual Information.
- Tambahkan validasi bisnis: apakah tiap cluster mudah dijelaskan dan berguna?

| Metrik | Rumus | Interpretasi |
|--------|-------|--------------|
| Silhouette (per titik) | `s = (b − a) / max(a, b)` | rentang −1 s.d. +1, makin tinggi makin kompak dan terpisah |
| Inertia | `Σ jarak² titik ke centroid cluster-nya` | makin kecil makin rapat |
| Davies-Bouldin | `(1/k) Σ max_{j≠i} (sᵢ + sⱼ) / d(cᵢ, cⱼ)` | kemiripan antarcluster, makin kecil makin baik |

`a` = rata-rata jarak ke titik lain dalam cluster yang sama, `b` = rata-rata jarak ke cluster terdekat lainnya.

### 3. Klasifikasi (3 kelas)

Pertanyaan: apakah model memilih kelas yang tepat?

- Data: tabel aktual vs prediksi untuk 3 kelas (contoh slide: mangga, jeruk, apel).
- Langkah: susun **confusion matrix 3×3**, lalu hitung TP, FP, FN per kelas (one-vs-rest).
- Metrik inti: **Accuracy**, **Precision**, **Recall**, **F1-Score** per kelas, lalu rata-rata **macro** (dan boleh **weighted**).
- Catatan dari slide: accuracy bisa menipu pada data tidak seimbang, jadi tampilkan juga metrik per kelas.

| Metrik | Rumus |
|--------|-------|
| Accuracy  | `jumlah diagonal / total data` |
| Precision | `TP / (TP + FP)` |
| Recall    | `TP / (TP + FN)` |
| F1-Score  | `2 · P · R / (P + R)` |

### 4. Deteksi Objek

Pertanyaan: di mana objeknya, dan apakah bounding box beserta kelasnya benar?

- Data: beberapa gambar, masing-masing berisi bounding box ground truth (GT) dan prediksi (koordinat `x1, y1, x2, y2`, kelas, confidence score).
- Langkah:
  1. Hitung **IoU** tiap pasangan prediksi-GT: `luas irisan / luas gabungan`.
  2. Tentukan TP/FP/FN dengan ambang **IoU ≥ 0,50** (prediksi tanpa GT cocok = FP, GT tanpa prediksi = FN).
  3. Hitung **Precision** dan **Recall**.
  4. Urutkan prediksi berdasarkan confidence, buat kurva precision-recall, hitung **AP** (luas di bawah kurva PR) per kelas.
  5. **mAP** = rata-rata AP antar kelas.
- Contoh slide: 1 gambar, 3 objek GT, hasilnya 2 cocok, 1 terlewat (FN), 1 deteksi palsu (FP).

## Studi Kasus: Pengawasan Truk ODOL

Keempat bagian memakai tema truk ODOL (*Over Dimension Over Load*), melanjutkan tugas YOLO sebelumnya.

| Bagian | Kasus | Hasil utama |
|---|---|---|
| Regresi | Sensor WIM vs jembatan timbang, 10 truk | MAE 1,370 ton, RMSE 1,544 ton, R² 0,9714, MAPE 6,09 % |
| Clustering | Rasio dimensi & muatan terhadap batas izin, 12 truk, K-Means k=3 | Inertia 952,5, Silhouette 0,6294, DBI 0,4627 |
| Klasifikasi | Status `normal` / `overload` / `overdimension`, 30 truk | Accuracy 0,7667, macro F1 0,7442 |
| Deteksi objek | YOLO11n (`roda`, `truk_normal`, `truk_odol`) pada 5 gambar test asli | Precision 0,7222, recall 0,8125, mAP@0.50 0,6919 |

Data regresi, clustering, dan klasifikasi adalah data karangan. Data deteksi memakai gambar, anotasi, dan prediksi asli dari model `tugas/best.pt`.
Semua metrik dihitung manual di notebook lalu dicocokkan dengan `scikit-learn` / `ultralytics`.

## Struktur Folder

```
kelompok-evaluasi-model/
├── README.md
├── DS 11 Evaluasi.pptx.pdf          # materi dan instruksi tugas
├── evaluasi_model.ipynb             # perhitungan manual + verifikasi library
├── requirements.txt
├── data/
│   ├── regresi_berat_truk.csv
│   ├── clustering_truk.csv
│   ├── klasifikasi_status_muatan.csv
│   └── deteksi/
│       ├── images/                  # 5 gambar test
│       ├── labels/                  # ground truth format YOLO
│       └── prediksi_yolo.csv        # prediksi model (conf ≥ 0,25)
├── scripts/
│   └── prediksi_deteksi.py          # membuat ulang prediksi_yolo.csv
├── figures/                         # grafik yang dipakai laporan
└── laporan/
    ├── Laporan_Evaluasi_Model_Kelompok_SDT.tex   # XeLaTeX, format standar Word
    ├── Laporan_Evaluasi_Model_Kelompok_SDT.pdf
    └── logo_ugm.png
```

## Cara Menjalankan

```bash
cd kelompok-evaluasi-model
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/jupyter nbconvert --to notebook --execute --inplace evaluasi_model.ipynb   # atau buka di Jupyter/Colab
cd laporan && latexmk -xelatex Laporan_Evaluasi_Model_Kelompok_SDT.tex                # kompilasi ulang laporan
```

Membuat ulang prediksi deteksi dari model: `.venv/bin/python scripts/prediksi_deteksi.py ../tugas/best.pt`.

## Checklist

- [x] Isi nama dan NIM anggota kelompok (README dan sampul `laporan/Laporan_Evaluasi_Model_Kelompok_SDT.tex`)
- [x] Regresi: dataset contoh + perhitungan MAE, MSE, RMSE, R² (plus MAPE, MPE, RAE, RSE)
- [x] Clustering: dataset contoh + perhitungan Inertia, Silhouette, Davies-Bouldin
- [x] Klasifikasi 3 kelas: confusion matrix 3×3 + accuracy, precision, recall, F1 (per kelas, macro, weighted)
- [x] Deteksi objek: IoU, TP/FP/FN, precision, recall, AP, mAP
- [x] Interpretasi singkat hasil tiap bagian
