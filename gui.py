# gui.py

import tkinter as tk
from backup_app import BackupApp

class BackupAppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Backup Application")
        self.root.geometry("400x250")
        self.root.configure(bg="#2C3E50")  # Set background color

        # Welcome message
        self.welcome_label = tk.Label(self.root, text="Welcome to Backup Application", font=("Helvetica", 18, "bold"), fg="white", bg="#2C3E50")
        self.welcome_label.pack(pady=10)

        # Source directory input
        self.source_label = tk.Label(self.root, text="Source Directory:", font=("Helvetica", 12), fg="white", bg="#2C3E50")
        self.source_label.pack()
        self.source_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.source_entry.pack()

        # Backup directory input
        self.backup_label = tk.Label(self.root, text="Backup Directory:", font=("Helvetica", 12), fg="white", bg="#2C3E50")
        self.backup_label.pack()
        self.backup_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.backup_entry.pack()

        # Backup time input
        self.time_label = tk.Label(self.root, text="Backup Time (HH:MM):", font=("Helvetica", 12), fg="white", bg="#2C3E50")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.time_entry.pack()

        # Run backup button
        self.run_button = tk.Button(self.root, text="Run Backup", font=("Helvetica", 14, "bold"), bg="#3498DB", fg="white", relief="raised", command=self.run_backup)
        self.run_button.pack(pady=15)

    def run_backup(self):
        source_dir = self.source_entry.get()
        backup_dir = self.backup_entry.get()
        backup_time = self.time_entry.get()

        # Create BackupApp instance and run backup
        app = BackupApp(source_dir, backup_dir, backup_time)
        app.run_backup()

    def run(self):
        self.root.mainloop()
