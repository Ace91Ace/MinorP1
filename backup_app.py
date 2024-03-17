# backup_app.py

import time
import datetime
import utils

class BackupApp:
    def __init__(self, source_dir, backup_dir, backup_time):
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.backup_time = backup_time

    def run_backup(self):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == self.backup_time:
                utils.backup_files(self.source_dir, self.backup_dir)
                print("Backup completed.")
                break
            time.sleep(60)  # Check every minute if it's time to backup
