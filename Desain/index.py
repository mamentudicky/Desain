import tkinter as tk
from PIL import Image, ImageTk

# Fungsi untuk memperbarui ukuran gambar saat jendela diubah ukurannya
def resize_image(event):
    new_width = event.width
    new_height = event.height

    # Resize gambar asli ke dimensi baru
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    new_photo = ImageTk.PhotoImage(resized_image)

    # Perbarui gambar pada label
    label.config(image=new_photo)
    label.image = new_photo  # Simpan referensi ke objek gambar agar tidak terhapus oleh garbage collector

# Buat jendela utama
root = tk.Tk()
root.title("Dynamic Image Display")

# Buka file gambar (sesuaikan jalur ke lokasi gambar Anda)
image = Image.open("image/gambar.jpg")  # Jalur relatif ke folder 'image'

# Konversi gambar ke objek PhotoImage awal
photo = ImageTk.PhotoImage(image)

# Buat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack(fill=tk.BOTH, expand=True)

# Kaitkan event resize dengan fungsi resize_image
root.bind("<Configure>", resize_image)

# Jalankan aplikasi
root.mainloop()
