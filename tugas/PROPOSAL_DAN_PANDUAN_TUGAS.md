# Tugas Sains Data Terapan (SVPL261506) — Deteksi Komputer Vision & CRISP-DM
**Topik:** Lalu Lintas (Traffic AI) — *Unconventional & High-Impact Domain*  
**Platform Anotasi:** Roboflow (`hafidz-prasetya/sains-data-terapan/upload`)  
**Metodologi:** CRISP-DM (Cross Industry Standard Process for Data Mining)  
**Dosen:** Dr. Muhammad Fakhrurrifqi, S.Kom., M.Cs.  

---

## 1. MENGAPA BUKAN TEMA LALU LINTAS BIASA? (FIRST PRINCIPLES)

Mayoritas tugas computer vision lalu lintas terjebak pada tema klise:
- *Menghitung mobil/motor (vehicle counting)*: Tidak memiliki novelty karena model YOLO bawaan COCO (`car`, `motorcycle`, `bus`, `truck`) sudah bisa tanpa perlu dilatih ulang.
- *Deteksi helm*: Komoditas umum sejak 2018.
- *Deteksi pelanggaran lampu merah*: Sudah menjadi fitur baku ETLE konvensional.

Untuk menghasilkan **Business Understanding** yang berbobot dan menonjol di hadapan dosen Sains Data Terapan, kita memilih sudut pandang yang menyelesaikan masalah nyata dengan dampak terukur (*asymmetric value*).

---

## 2. PILIHAN TEMA UNIK (REKOMENDASI UTAMA)

### 🥇 Pilihan 1 (Rekomendasi Utama): Urban Sidewalk Inclusivity & Pedestrian Space Hijacking
**"Deteksi Invasi Trotoar, Penyerobotan Guiding Block Disabilitas, dan Hambatan Pejalan Kaki oleh Kendaraan"**

- **Latar Belakang Masalah:**
  Kota-kota modern mengklaim ramah pejalan kaki dan inklusif bagi penyandang disabilitas (*walkable & inclusive city*). Namun realitas di lapangan (khususnya kota-kota di Indonesia seperti Yogyakarta dan Jakarta), trotoar dan *guiding block* (jalur ubin kuning pemandu tuna netra) secara kronis diserobot sepeda motor saat macet, dijadikan tempat parkir liar, atau terhalang lapak/banner pedagang. Pejalan kaki dan difabel terpaksa turun ke badan jalan dan bertaruh nyawa dengan kendaraan berkecepatan tinggi.
- **Kelas Deteksi di Roboflow (4 Kelas Presisi):**
  1. `motor_on_sidewalk` : Sepeda motor yang melintas atau berjalan di atas trotoar/jalur pedestrian.
  2. `illegal_parking_curb` : Kendaraan (motor/mobil) yang parkir di atas trotoar atau memakan bahu jalan aktif.
  3. `obstructed_guiding_block` : Jalur pemandu tuna netra (kuning bergaris/berbintik) yang tertimpa atau terhalang benda fisik.
  4. `vendor_blocking_path` : Lapak jualan, gerobak, meja, atau spanduk promosi yang memblokir ruang bebas pejalan kaki.

---

### 🥈 Pilihan 2 (Alternatif Logistik & Safety): Hazardous Cargo & Micro-ODOL Risk Detection
**"Deteksi Muatan Berbahaya, Muatan Menjuntai Tanpa Tanda Pengaman, dan Angkutan Liar di Jalan Arteri"**

- **Latar Belakang Masalah:**
  Masalah ODOL (*Overdimension Overload*) bukan hanya tentang tonase di jembatan timbang tol, melainkan risiko kecelakaan fatal di jalan raya arteri dan non-tol. Pick-up bermuatan barang melebihi kabin hingga menutupi spion, truk pengangkut bambu/besi beton yang menjuntai keluar bak tanpa kain merah pengaman, serta truk pasir/puing terbuka tanpa terpal penutup yang menyemburkan batu/debu ke pengendara di belakang.
- **Kelas Deteksi di Roboflow (4 Kelas Presisi):**
  1. `overheight_cargo` : Muatan pick-up/truk yang tingginya melampaui batas wajar kabin (>1.5x tinggi kabin).
  2. `unmarked_overhang_cargo` : Batang besi/kayu/bambu yang menjuntai ke belakang tanpa tanda kain merah/lampu darurat.
  3. `uncovered_bulk_cargo` : Truk pasir/tanah/puing terbuka yang tidak ditutup terpal pengaman.
  4. `tilted_unstable_load` : Tumpukan muatan miring yang berisiko terguling di tikungan.

---

## 3. DOKUMEN BUSINESS UNDERSTANDING (CRISP-DM FASE 1)
*(Format siap pakai untuk laporan/presentasi tugas SDT)*

### A. Background & Problem Statement
Trotoar perkotaan dirancang sebagai ruang aman pejalan kaki dan fasilitas aksesibilitas bagi penyandang disabilitas (UU No. 22 Tahun 2009 & Permen PUPR No. 14/PRT/M/2017). Namun, pemantauan manual oleh Dinas Perhubungan dan Satpol PP memiliki keterbatasan cakupan (*temporal & spatial coverage*). Pelanggaran terjadi sporadis dan berulang, menurunkan indeks kenyamanan pejalan kaki (*Walkability Index*) dan meningkatkan risiko fatalitas kelompok rentan.

### B. Business Objectives & Criteria (Ukuran Keberhasilan Bisnis)
- **Business Goal:** Mengembangkan sistem audit visual otomatis berbasis CCTV jalan/kamera patroli untuk mengukur tingkat kepatuhan dan keselamatan ruang pejalan kaki secara kontinu tanpa patroli fisik 24/7.
- **Business Success Criteria:**
  1. Mampu mengidentifikasi 90% insiden invasi trotoar pada ruas jalan target.
  2. Menghasilkan metrik *Sidewalk Obstruction Rate* per jam untuk pelaporan mingguan Dinas Perhubungan.
  3. Menurunkan latensi respon penertiban parkir liar dan pembebasan jalur difabel dari hitungan hari menjadi < 30 menit.

### C. Data Mining Goals & Technical Criteria (Ukuran Keberhasilan Teknis)
- **Technical Goal:** Melatih model object detection (YOLOv11/v8) berbasis dataset citra jalanan perkotaan untuk mengklasifikasi dan melokalisasi 4 kategori anomali ruang pedestrian.
- **Technical Success Criteria:**
  - Mean Average Precision (mAP@50) $\ge 0.80$ pada validation/test set.
  - Precision $\ge 0.85$ pada kelas `motor_on_sidewalk` untuk mencegah *false accusations*.
  - Kecepatan inferensi $\ge 30$ FPS pada resolusi input standar (640x640) untuk kesiapan *real-time deployment*.

### D. Inventory of Resources & Constraints
- **Hardware/Software:** Roboflow Annotator, Google Colab / Local GPU, Python 3.12, Ultralytics YOLO.
- **Constraints:** Variasi pencahayaan (siang/malam/hujan), oklusi antar pejalan kaki dan pepohonan peneduh jalan, variasi desain trotoar lokal.

---

## 4. WORKFLOW ANOTASI DI ROBOFLOW (LANGKAH DEMI LANGKAH)

### Langkah 1: Pengumpulan Data Gambar (Data Understanding)
- Kumpulkan **40 - 60 gambar** representatif.
- Sumber terbaik:
  - Screenshot video YouTube dashcam/CCTV jalanan kota (misal: "kondisi trotoar jakarta / jogja", "motor serobot trotoar", "kemacetan gejayan/malioboro").
  - Foto langsung di sekitar trotoar kampus UGM/Jalan Kaliurang/Gejayan.
- Pastikan resolusi gambar jelas, objek tidak terlalu kabur/blur.

### Langkah 2: Upload ke Roboflow
1. Buka link project: `https://app.roboflow.com/hafidz-prasetya/sains-data-terapan/upload`
2. Drag and drop file gambar (40-60 file JPG/PNG).
3. Klik **Save and Continue** ke tahap Annotate.

### Langkah 3: Melakukan Labeling / Bounding Box (Anotasi)
Penting: Tetapkan nama kelas persis sama (lowercase, pakai underscore):
- `motor_on_sidewalk`
- `illegal_parking_curb`
- `obstructed_guiding_block`
- `vendor_blocking_path`

*Aturan Labeling yang Baik:*
- Buat kotak (bounding box) ketat menempel pada tepi objek (*tight bounding box*).
- Jangan sertakan trotoar kosong ke dalam box jika yang dideteksi adalah motornya.
- Jika guiding block tertutup sebagian oleh motor, beri box `obstructed_guiding_block` pada area ubin kuning yang terhalang, dan box `motor_on_sidewalk` pada motornya.

### Langkah 4: Generate Version & Dataset Split
1. Setelah semua gambar selesai dilabel, klik menu **Generate**.
2. Split standar yang direkomendasikan:
   - **Train:** 70%
   - **Valid:** 20%
   - **Test:** 10%
3. Preprocessing (disarankan default):
   - Auto-Orient
   - Resize to 640x640 (Stretch atau Fit with white/black edge)
4. Augmentasi ringan (opsional tapi bagus untuk nilai):
   - Horizontal Flip
   - Brightness (-15% s.d. +15%)
5. Klik **Create / Generate Version**.

### Langkah 5: Export Dataset
1. Pilih **Export Dataset**.
2. Format: **YOLOv11** (atau YOLOv8).
3. Pilih "show download code" (bisa kita tarik langsung via terminal/Colab script).
