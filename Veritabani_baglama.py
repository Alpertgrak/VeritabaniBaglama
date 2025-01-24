import tkinter as tk
from tkinter import messagebox
import pyodbc


class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL Server Bağlantısı Kontrolü")
        self.root.geometry("400x300")

        self.title_label = tk.Label(root, text="SQL Server Bağlantısı Kontrolü", font=("Helvetica", 14))
        self.title_label.pack(pady=10)

        self.server_label = tk.Label(root, text="Server")
        self.server_label.pack(pady=5)

        self.server_entry = tk.Entry(root, width=30)
        self.server_entry.pack(pady=5)
        self.server_entry.insert(0, "ALPERTGRAK")

        self.database_label = tk.Label(root, text="Database")
        self.database_label.pack(pady=5)

        self.database_entry = tk.Entry(root, width=30)
        self.database_entry.pack(pady=5)
        self.database_entry.insert(0, "KutuphaneDB1")

        self.connect_button = tk.Button(root, text="Bağlan", command=self.baglanti_kontrol)
        self.connect_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def baglan(self):
        server = self.server_entry.get()
        database = self.database_entry.get()

        # Create connection string
        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        try:
            # Attempt to connect to the SQL server
            conn = pyodbc.connect(conn_str)
            print("Veritabanına başarıyla bağlandı")
            return conn
        except Exception as e:
            print(f"Bağlantı hatası: {e}")
            return None

    def baglanti_kontrol(self):
        conn = self.baglan()

        if conn:
            self.result_label.config(text="Bağlantı başarılı", fg="green")
        else:
            self.result_label.config(text="Bağlantı hatası", fg="red")
            messagebox.showerror("Bağlantı Hatası", "Veritabanına bağlanılamadı")



if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()