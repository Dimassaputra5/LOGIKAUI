import os
import shutil
import random

def split_image_dataset(source_dir, dest_dir, val_ratio=0.2):
    """
    Memisahkan dataset gambar ke dalam folder train dan validation.

    Args:
        source_dir (str): Path ke direktori utama yang berisi folder-folder kelas (misal: '.../Train/Train').
        dest_dir (str): Path ke direktori tujuan di mana folder 'train_final' dan 'validation' akan dibuat.
        val_ratio (float): Rasio data yang akan dialokasikan untuk validation set.
    """
    
    # Membuat direktori tujuan jika belum ada
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Path untuk folder train dan validation baru
    train_path = os.path.join(dest_dir, 'train_final')
    val_path = os.path.join(dest_dir, 'validation')
    
    # Membuat folder train_final dan validation
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(val_path, exist_ok=True)

    # Mendapatkan daftar nama kelas (nama folder)
    list_kelas = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))]
    
    print(f"Ditemukan {len(list_kelas)} kelas: {list_kelas}")
    
    for nama_kelas in list_kelas:
        # Membuat subfolder kelas di dalam train_final dan validation
        os.makedirs(os.path.join(train_path, nama_kelas), exist_ok=True)
        os.makedirs(os.path.join(val_path, nama_kelas), exist_ok=True)
        
        # Path ke folder kelas sumber
        sumber_kelas_dir = os.path.join(source_dir, nama_kelas)
        
        # Mendapatkan semua file gambar di dalam folder kelas
        daftar_gambar = [f for f in os.listdir(sumber_kelas_dir) if os.path.isfile(os.path.join(sumber_kelas_dir, f))]
        
        # Mengacak urutan gambar
        random.shuffle(daftar_gambar)
        
        # Menghitung jumlah data untuk validation
        split_point = int(len(daftar_gambar) * val_ratio)
        
        # Memisahkan daftar file
        val_files = daftar_gambar[:split_point]
        train_files = daftar_gambar[split_point:]
        
        # Menyalin file ke folder validation
        for file_name in val_files:
            shutil.copy(os.path.join(sumber_kelas_dir, file_name), os.path.join(val_path, nama_kelas, file_name))
            
        # Menyalin file ke folder train
        for file_name in train_files:
            shutil.copy(os.path.join(sumber_kelas_dir, file_name), os.path.join(train_path, nama_kelas, file_name))
            
        print(f"Kelas '{nama_kelas}': {len(train_files)} train, {len(val_files)} validation")
        
    print("\nProses pemisahan data selesai!")


# --- Konfigurasi Path ---
# Berdasarkan gambar Anda, path sumber memiliki subfolder 'Train' lagi di dalamnya.
SOURCE_DIRECTORY = 'dsc-logika-ui-2025/Train/Train'
DESTINATION_DIRECTORY = 'dataset_split' # Nama folder baru untuk menampung hasil split

# --- Jalankan Fungsi ---
split_image_dataset(SOURCE_DIRECTORY, DESTINATION_DIRECTORY, val_ratio=0.2)