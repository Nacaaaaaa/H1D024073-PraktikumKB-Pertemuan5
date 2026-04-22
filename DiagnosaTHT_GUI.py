import tkinter as tk
from tkinter import messagebox

# Knowledge base
# Struktur: "Nama Penyakit": ["daftar_gejala"]
database_penyakit = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

# Daftar pertanyaan semua gejala untuk GUI
semua_gejala = [
    ("G1", "Apakah Anda mengalami nafas abnormal?"),
    ("G2", "Apakah suara Anda menjadi serak?"),
    ("G3", "Apakah ada perubahan pada kulit Anda?"),
    ("G4", "Apakah telinga terasa penuh?"),
    ("G5", "Apakah Anda merasa nyeri saat bicara atau menelan?"),
    ("G6", "Apakah Anda mengalami nyeri tenggorokan?"),
    ("G7", "Apakah Anda mengalami nyeri leher?"),
    ("G8", "Apakah Anda mengalami pendarahan hidung (mimisan)?"),
    ("G9", "Apakah telinga Anda berdenging?"),
    ("G10", "Apakah air liur Anda sering menetes?"),
    ("G11", "Apakah ada perubahan pada suara Anda?"),
    ("G12", "Apakah Anda mengalami sakit kepala?"),
    ("G13", "Apakah ada rasa nyeri di pinggir hidung?"),
    ("G14", "Apakah Anda mengalami serangan vertigo?"),
    ("G15", "Apakah ada masalah pada kelenjar getah bening?"),
    ("G16", "Apakah leher Anda bengkak?"),
    ("G17", "Apakah hidung Anda tersumbat?"),
    ("G18", "Apakah Anda memiliki infeksi sinus?"),
    ("G19", "Apakah berat badan Anda turun drastis?"),
    ("G20", "Apakah Anda mengalami nyeri telinga?"),
    ("G21", "Apakah selaput lendir Anda berwarna merah?"),
    ("G22", "Apakah terdapat benjolan di leher?"),
    ("G23", "Apakah tubuh terasa tidak seimbang?"),
    ("G24", "Apakah bola mata Anda bergerak tidak terkendali?"),
    ("G25", "Apakah Anda mengalami nyeri di wajah?"),
    ("G26", "Apakah dahi Anda terasa sakit?"),
    ("G27", "Apakah Anda mengalami batuk?"),
    ("G28", "Apakah ada sesuatu yang tumbuh di mulut Anda?"),
    ("G29", "Apakah ada benjolan di leher Anda?"),
    ("G30", "Apakah ada rasa nyeri di antara mata?"),
    ("G31", "Apakah Anda mengalami radang gendang telinga?"),
    ("G32", "Apakah tenggorokan terasa gatal?"),
    ("G33", "Apakah hidung Anda meler?"),
    ("G34", "Apakah Anda mengalami tuli atau penurunan pendengaran?"),
    ("G35", "Apakah Anda merasa mual dan muntah?"),
    ("G36", "Apakah Anda merasa letih dan lesu?"),
    ("G37", "Apakah Anda mengalami demam?")
]

class SistemPakarTHT:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # Label pertanyaan
        self.label_tanya = tk.Label(root, text="Diagnosa Penyakit THT", font=("Times New Roman", 14, "bold"))
        self.label_tanya.pack(pady=20)

        # Tombol mulai
        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", bg="lightblue", font=("Times New Roman", 12), command=self.mulai_tanya)
        self.btn_mulai.pack(pady=10)

        # Frame tombol jawaban
        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=10, bg="lightgreen", command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=10, bg="salmon", command=lambda: self.jawab('t'))

        self.btn_ya.pack(side=tk.LEFT, padx=15)
        self.btn_tidak.pack(side=tk.LEFT, padx=15)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks, wraplength=350, font=("Times New Roman", 12, "normal"))
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)
        
        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        hasil_diagnosa = []

        # Inferensi sistem pakar
        for penyakit, syarat_gejala in database_penyakit.items():
            # Pengecekan semua syarat gejala dari penyakit ada di gejala_terpilih pengguna
            if all(s in self.gejala_terpilih for s in syarat_gejala):
                hasil_diagnosa.append(f"- {penyakit}")

        # Output hasil diagnosa
        if hasil_diagnosa:
            kesimpulan = "\n".join(hasil_diagnosa)
            pesan = f"Berdasarkan input gejala Anda, kemungkinan penyakit yang dialami adalah:\n\n{kesimpulan}\n\n*Harap segera konsultasikan ke dokter THT untuk penanganan lebih lanjut."
        else:
            pesan = "Penyakit tidak terdeteksi.\nGejala yang Anda masukkan tidak mengarah pada penyakit spesifik di database kami. Silakan periksa ulang atau hubungi dokter terdekat."

        messagebox.showinfo("Hasil Diagnosa", pesan)

        # Reset ke awal
        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai. Ingin mencoba lagi?", font=("Times New Roman", 12, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x250")
    app = SistemPakarTHT(root)
    root.mainloop()
