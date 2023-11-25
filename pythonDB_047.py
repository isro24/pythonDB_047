import sqlite3
import tkinter as tk

def prediksi_fakultas(bio, fis, ing):
    if bio > fis and bio > ing:
        return 'Kedokteran'
    elif fis > bio and fis > ing:
        return 'Teknik'
    elif ing > bio and ing > fis:
        return 'Bahasa'
    else:
        return 'Tidak dapat diprediksi'

def tambah_data():
    nama = entry_nama.get()
    bio = float(entry_biologi.get())
    fis = float(entry_fisika.get())
    ing = float(entry_inggris.get())
    
    simpan_data_ke_sqlite(nama, bio, fis, ing)

    prediksi = prediksi_fakultas(bio, fis, ing)

    luaran_hasil.config(text=f"Fakultas yang direkomendasikan: {prediksi}")

def simpan_data_ke_sqlite(nama, bio, fis, ing):
    conn = sqlite3.connect("data_siswa.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nama_siswa TEXT,
            Biologi INTEGER,
            Fisika INTEGER,
            Inggris INTEGER,
            Prediksi_fakultas TEXT
        )
    ''')

    prediksi = prediksi_fakultas(bio, fis, ing)

    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, bio, fis, ing, prediksi))

    conn.commit()
    conn.close()

sql = tk.Tk()
sql.config(background='white')
sql.geometry('430x370')
sql.resizable(False, False)
sql.title("Aplikasi Prediksi Prodi Pilihan")

label_nama = tk.Label(sql, text="Nama Siswa:")
label_nama.pack(pady=5, padx=10)

entry_nama = tk.Entry(sql)
entry_nama.pack(pady=5, padx=10)

label_biologi = tk.Label(sql, text="Nilai Biologi:")
label_biologi.pack(pady=5, padx=10)
entry_biologi = tk.Entry(sql)
entry_biologi.pack(pady=5, padx=10)

label_fisika = tk.Label(sql, text="Nilai Fisika:")
label_fisika.pack(pady=5, padx=10)
entry_fisika = tk.Entry(sql)
entry_fisika.pack(pady=5, padx=10)

label_inggris = tk.Label(sql, text="Nilai Inggris:")
label_inggris.pack(pady=5, padx=10)
entry_inggris = tk.Entry(sql)
entry_inggris.pack(pady=5, padx=10)

button_submit = tk.Button(sql, text="Submit", command=tambah_data)
button_submit.pack(pady=10)

luaran_hasil = tk.Label(sql, text="", font=("Times New Roman", 14))
luaran_hasil.pack(pady=10)

sql.mainloop()
