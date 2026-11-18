"""Jalankan model YOLO11n ODOL pada gambar di data/deteksi/images dan simpan prediksinya.

Pemakaian (dari folder kelompok-evaluasi-model):
    .venv/bin/python scripts/prediksi_deteksi.py ../tugas/best.pt
"""
import sys
from pathlib import Path

import pandas as pd
from ultralytics import YOLO

KELAS = {0: "roda", 1: "truk_normal", 2: "truk_odol"}
base = Path(__file__).resolve().parent.parent / "data" / "deteksi"
model = YOLO(sys.argv[1] if len(sys.argv) > 1 else "../tugas/best.pt")

rows = []
for img in sorted((base / "images").glob("*.jpg")):
    hasil = model.predict(img, conf=0.25, verbose=False)[0]
    for cls, box, conf in zip(hasil.boxes.cls, hasil.boxes.xyxy, hasil.boxes.conf):
        x1, y1, x2, y2 = (round(v, 1) for v in box.tolist())
        rows.append({"gambar": img.stem, "kelas": KELAS[int(cls)], "confidence": round(float(conf), 3),
                     "x1": x1, "y1": y1, "x2": x2, "y2": y2})

df = pd.DataFrame(rows)
df.to_csv(base / "prediksi_yolo.csv", index=False)
print(df.to_string(index=False))
