# DDA Monitor Optimized

## Cara Jalankan:
1. Install dependensi:
   pip install opencv-python

2. Jalankan:
   python main.py

## Struktur Folder
- main.py : Entry point
- src/
  - capture.py : Video capture thread
  - detector.py : Deteksi wajah
  - visual.py : Gambar bounding box
- utils/
  - timer.py : (Opsional) hitung FPS
- models/
  - haarcascade_frontalface_default.xml : Model deteksi wajah
